from PIL import Image

from imagehandler import ImageHandler

class Stenography:
    #ONLY USE PNG IMAGES !!! DO NOT USE JPG UNLESS YOU WANT TO CRY !!!!
    #when calling stenography, pass an imageHandler object
    #example (next 2 lines):
    #image_stuff = ImageHandler()
    # sten = Stenography(image_stuff)
    def __init__(self, image_handler):
        self.image= image_handler.get_image()
        if self.image is None:
            raise ValueError("Failed to load image. Please check the image path and format.")
        self.message= None

    def set_message(self, encrypted_message):
        binary_message = ''.join(bin(byte)[2:].zfill(8) for byte in encrypted_message)
            #converting message from bytes to bits (8 bits per byte)
        if len(binary_message) > self.image.size[0] * self.image.size[1] * 3:
            raise ValueError("Message is too large to encode in this image.")
        self.message = binary_message
        return True

    def encode_image(self, encrypted_message):
        # before this, import image using image_handler
        # encrypt message and then call this
        # assumption is that the encrypted message is in bytes
        if not self.set_message(encrypted_message):
            raise ValueError("Message setting failed")
             #converting bytes to bits and putting that in the instance variable
        new_image= self.image.copy() #cloning image
        modified_pixels = self.modify_pixels(self.image.getdata())
         #get modified pixels
        w = new_image.size[0]
        (x,y) = (0,0)

        #assembling modified image to new image
        #the next part replaces pixels in the cloned(new) image with modified pixels for the length of the message
        for pix in modified_pixels:
            new_image.putpixel((x, y), pix)
            if x == (w - 1):
                x = 0
                y += 1
            else:
                x += 1
        return new_image

    def modify_pixels(self, pixels):
       #modify pixel data and returns a list of tuples with RGB values changed
        message_bits = list(self.message) #list of the message in bits
        message_length = len(message_bits)
        pixel = iter(pixels)

        for i in range(0, message_length, 8):
            #when there is message left to encrypt, encodes pixels
                current_pixel  = list(next(pixel)[:3]+ next(pixel)[:3]+ next(pixel)[:3])
                #9 pixels are encoded at once: 8 bits per byte + 1 bit that lets us know if we should keep decoding
                bit = i
                for j in range (0, 8): #changing RGB values based on message
                    if (message_bits[bit] == '0') and (current_pixel[j] % 2 != 0):
                        current_pixel[j] -= 1
                    elif (message_bits[bit] == '1') and (current_pixel[j] % 2 == 0):
                        if current_pixel[j] != 0:
                            current_pixel[j] -= 1
                        else:
                            current_pixel[j] += 1
                    bit += 1

                #check if it is the last bit of the message and indicate in 9th bit
                if bit == message_length:
                    if current_pixel[-1] % 2 == 0:
                        if current_pixel[-1] != 0:
                            current_pixel[-1] -= 1
                        else:
                            current_pixel[-1] += 1
                elif current_pixel[-1] % 2 != 0:
                        current_pixel[-1] -= 1

                # Yield the modified pixel tuples
                current_pixel= tuple(current_pixel)
                yield current_pixel[0:3]
                yield current_pixel[3:6]
                yield current_pixel[6:9]

    def decode_image(self):
        # before this, import image using image_handler
        # this returns the encrypted message
        #the message needs to be decrypted
        encrypted_message = b''  # initializing a byte string
        image_data = iter(self.image.getdata())  # accessing image data into an iterator
        while (True):
            pixels = list(next(image_data)[:3]+ next(image_data)[:3]+ next(image_data)[:3])
            binstring = ''
            counter = 1
            for pixel in pixels: #decrypting all but every 9th pixel in the array
                if counter % 9 == 0:
                    continue
                if pixel % 2 == 0:
                    binstring += '0'
                else:
                    binstring += '1'
                counter += 1
            encrypted_message += bytes([int(binstring, 2)]) #will need to be decrypted
            if pixels[-1] % 2 != 0:
                return encrypted_message

'''# TESTING 1. encoding

image_stuff = ImageHandler()
import_result = image_stuff.import_image("output2.png")

if import_result == "importing image success":
    sten = Stenography(image_stuff)
    image = sten.encode_image("Hi! This is Krishna- Test #idek. Success!!".encode('utf-8'))
    if image:
        save_result = image_stuff.save_image(image, "encoded_image2.png")
        print(save_result)
    else:
        print("Failed to encode image.")
else:
    print(import_result)

# TESTING 2. decoding

image_stuff2 = ImageHandler()
    #different object from the first one. Using same object might not work
    #don't think it matters because we don't encode and decode at same time but yeah
import_result = image_stuff2.import_image("encoded_image2.png")

if import_result == "importing image success":
    print("decoding image:")
    sten = Stenography(image_stuff2)
    hidden_message = sten.decode_image()
    if hidden_message is not None:
        print(hidden_message)
    else:
        print("Failed to decode image.")
else:
    print(import_result)'''