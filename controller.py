import base64
from encryptionhandler import EncryptionHandler
from stenography import Stenography
from imagehandler import ImageHandler

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

    

    def embed_message(self, message, password, output_path): #   embeds an image with an encrypted message
        try:
            self.gui.update_status("Attempting to encode the image")
            encryption_handler = EncryptionHandler(password) # call for encryptionhandler class
            encrypted_message = encryption_handler.encrypt(message)  #  encrypts the string
            
            stenography = Stenography(self.image_handler)  # calls for stenography class
            encoded_image = stenography.encode_image(encrypted_message) # encodes an image
            
            save_result = self.image_handler.save_image(encoded_image, output_path) # saving
            self.gui.update_status(f"Hidden message embedded successfully: {save_result}")
        except Exception as e:
            self.gui.update_status(f"Could not embed the message due to: {str(e)}")

    def extract_message(self, password): #  extracting the message from an image
        try:
            self.gui.update_status("Attempting to decode the image")
            
            stenography = Stenography(self.image_handler) #  calls for stenography class
            encrypted_message = stenography.decode_image() # decodes the image

            self.gui.update_status("Decrypting the message")
            encryption_handler = EncryptionHandler(password) # call for encryptionhandler
            decrypted_message = encryption_handler.decrypt(encrypted_message) #  decryption process
            
            self.gui.display_extracted_text(decrypted_message) # outputs the decrypted text
        except Exception as e:
            error_message = str(e) or "An unknown error occurred during decryption"
            self.gui.update_status(f"Could not decrypt the hidden message due to: {error_message}")