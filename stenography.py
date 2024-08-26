from PIL import Image

from imagehandler import ImageHandler


class Stenography:
    def __init__(self):
        self.image= ImageHandler.get_image()
        self.message= None

    def set_message(self, encrypted_message):
        binary_message = ''.join(bin(byte)[2:].zfill(8) for byte in encrypted_message)
        if len(binary_message) > self.image.size[0] * self.image.size[1] * 3:
            raise ValueError("Message is too large to encode in this image.")
        self.message = binary_message
        return True

    def encode_image(self, encrypted_message, final_image_path):
        # encrypt message and then call this
        # assumption is that the encrypted message is in bytes
        if not self.set_message(encrypted_message):
            raise ValueError("Message setting failed")
             #converting bytes to bits and putting that in the instance variable
        new_image= self.image.copy()
        modified_pixels = self.modify_pixels(self.image.getdata())
         #get modified pixels
        w, h = new_image.size
        pixel_iter = iter(modified_pixels)

        #assembling modified image to new image
        for y in range(h):
                    #assembling modified pixels into a new image
            for x in range(w):
                new_image.putpixel((x, y), next(pixel_iter))

        image_handler= ImageHandler()
        image_handler.save_image(new_image, final_image_path)

    def modify_pixels(self, pixels):
       #modify pixel data and return an 8 bit binary list
        message_bits = list(self.message)
        message_length = len(message_bits)
        pixel = iter(pixels)

        for bit in range(message_length):
                current_pixel  = list(next(pixel)[:3]+next(pixel)[:3]+ next(pixel)[:3])

                for j in range (0, 8):
                    if (message_bits[bit] == '0') and (current_pixel[j] % 2 != 0):
                        current_pixel[j] -= 1
                    elif (message_bits[bit] == '1') and (current_pixel[j] % 2 == 0):
                        if current_pixel[j] != 0:
                            current_pixel[j] -= 1
                        else:
                            current_pixel[j] += 1

                #check if it is the last bit of the message
                if bit == message_length - 1:
                    if current_pixel[-1] % 2 == 0:
                        if current_pixel[-1] != 0:
                            current_pixel[-1] -= 1
                        else:
                            current_pixel[-1] += 1

                else:
                        if current_pixel[-1] % 2 != 0:
                            current_pixel[-1] -= 1

                # Yield the modified pixel tuples
                current_pixel= tuple(current_pixel)
                yield current_pixel[0:3]
                yield current_pixel[3:6]
                yield current_pixel[6:9]

        for pixel in pixels:
            yield pixel










