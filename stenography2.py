'''import base64
from stegano import lsb
from PIL import Image

class Stenography:
    def __init__(self, image_handler):
        self.image_handler = image_handler # calls for the imagehandler class
        self.image = image_handler.get_image() # imports the image

    def encode_image(self, encrypted_message: bytes) -> Image:
        binary_safe_message = base64.urlsafe_b64encode(encrypted_message).decode('utf-8') # encodes the string as a base64 string
        encoded_image = lsb.hide(self.image, binary_safe_message) # using LSBSteg to embed the message
        return encoded_image

    def decode_image(self) -> bytes:
        binary_safe_message = lsb.reveal(self.image) # extracts the message via LSBSteg
        if binary_safe_message is None:
            raise ValueError("No hidden message found in the image")
        encrypted_message = base64.urlsafe_b64decode(binary_safe_message.encode('utf-8')) # decodes the message from base64
        return encrypted_message'''