import threading
from encryptionhandler import EncryptionHandler
from stenography import Stenography
from imagehandler import ImageHandler
import traceback


class Controller:
    def __init__(self, gui):
        self.gui = gui # loads the GUI
        self.image_handler = ImageHandler() # loads the imagehandler

    def load_image(self, image_path): # method to load the image
        try:
            result = self.image_handler.import_image(image_path) # use import method from imagehandler
            self.gui.update_status(result) # update GUI
        except Exception as e:
            self.gui.update_status(f"Couldn't load an image (Try PNG): {str(e)}")

    def save_image(self, output_path): # save image
        try:
            result = self.image_handler.save_image(self.image_handler.get_image(), output_path) # import method from imagehandler
            self.gui.update_status(result) # GUI update
        except Exception as e:
            self.gui.update_status(f"Could not save the image, try again: {str(e)}")

    def embed_message(self, message, password, output_path): # embed the image with the encrypted message via encryption and stenography classes
        def task():
            try:
                encryption_handler = EncryptionHandler(password) # call for encryptionhandler
                encrypted_message, salt = encryption_handler.encrypt(message) # encryptionhandler method usage

                self.gui.show_salt(salt) # show the salt value to the user
                
                stenography = Stenography(self.image_handler) # call for stenography
                encoded_image = stenography.encode_image(encrypted_message) # stenograpgy method usage
                
                save_result = self.image_handler.save_image(encoded_image, output_path) # imagehandler method usage
                self.gui.update_status(f"Hidden message embedded successfully {save_result}") # success
            except Exception as e:
                self.gui.update_status(f"Could not embed the message due to: {str(e)}")

        threading.Thread(target=task).start() # run the task with a thread

    def extract_message(self, password, salt): # decryption process for an emdedded image
        def task():
            try:
                self.gui.update_status("Attempting to decode an image...") # status debug (step 1)
                stenography = Stenography(self.image_handler) # stenography call

                encrypted_message = stenography.decode_image() # stenography method usage (get the encrypted message)
                if not encrypted_message:
                    raise ValueError("No message was found in the image or the image could not be decoded") # status debug (step 2)

                self.gui.update_status("Decrypting the message...") # status debug (step 3)
                encryption_handler = EncryptionHandler(password, salt) # encryptionhandler call
                decrypted_message = encryption_handler.decrypt(encrypted_message, salt) # encryptionhandler method usage
                if not decrypted_message:
                    raise ValueError("The message could not be decrypted. It might be corrupted or the password/salt may be incorrect.") # status debug (step 4)
                
                self.gui.display_extracted_text(decrypted_message) # display the decrypted text
            except Exception as e:
                # traceback.print_exc() # debug
                error_message = str(e) or "An unknown error occurred during decryption"
                self.gui.update_status(f"Could not decrypt the hidden message due to: {error_message}") 
        
        threading.Thread(target=task).start() # run the task with a thread