from PIL import Image

#IMPORTANT!!!
#use raw string because python takes '\' in string as escape characters
#image = ImageHandler.importImage(r"C:\Users\krishna\Pictures\naruto.jpg")
#other option is to have '\\' or '/' instead of '\\' in image path

class ImageHandler:
    def __init__(self):
        self.image= None #instance variable image

    def import_image(self, image_path):
        #loads an image from the imagePath given
        self.image= Image.open(image_path)
        if self.image is not None:
            return "importing image success"
        else:
            return "image not imported"


    def get_image(self):
        if self.image is None:
            raise ValueError("No image has been loaded")
        return self.image

    @staticmethod
    def save_image(new_image, image_path):
        #saves the newImage (that we created post encoding) at imagePath specified
        new_image.save(image_path)
        return "image saved as "+ image_path

