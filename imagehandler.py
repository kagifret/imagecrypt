from PIL import Image

#IMPORTANT!!!
#always use raw string because python takes '\' in string as escape characters
#image = ImageHandler.importImage(r"C:\Users\krishna\Pictures\naruto.jpg")
#other option is to have '\\' or '/' instead of '\\' in image path

class ImageHandler:
    def __init__(self):
        self.image= None #instance variable image

    def import_image(self, image_path):
        #loads an image from the imagePath given
        self.image= Image.open(image_path)
        return self.image

    @staticmethod
    def save_image(new_image, image_path):
        #saves the newImage (that we created post encoding) at imagePath specified
        new_image.save(image_path)
        return "image saved"

