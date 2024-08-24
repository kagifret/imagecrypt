from PIL import Image

from imagehandler import ImageHandler


class Stenography:
    def __init__(self):
        self.image= ImageHandler.get_image()
        self.message= None

    def set_message(self, encrypted_message):
        self.message = encrypted_message
        if self.message != None:
            return True

    def encode_image(self, encrypted_message, final_image_path):
        # encrypt message and then call this
        # assumption is that the encrypted message is in bytes
        if not self.set_message(''.join(bin(byte)[2:].zfill(8) for byte in encrypted_message)):
            raise ValueError("Failed to set message.")
             #converting bytes to bits and putting that in the instance variable
        new_image= self.image.copy()
        pixels = self.modify_pixels(self.image.getdata())
         #get modified pixels
        w, h = new_image.size
        pixel_iter = iter(pixels)

        if len(pixels) * 3 <len(self.message):
            raise ValueError("message too long.")

        for y in range(h):
                    #assembling modified pixels into a new image
            for x in range(w):
                new_image.putpixel((x, y), next(pixel_iter))

        image_handler= ImageHandler()
        image_handler.save_image(new_image, final_image_path)

    def modify_pixels(self, pixels):
       #modify pixel data and return an 8 bit binary list