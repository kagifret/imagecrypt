from PIL import Image

from imagehandler import ImageHandler


class Stenography:
    def __init__(self):
        self.image= ImageHandler.get_image()
        self.message= None

    def set_message(self, message):
        self.message = message
        if message != None:
            return True

