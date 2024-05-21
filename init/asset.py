import pygame as py

class Vehicule():
    def get_parts(self):
        pass
    
    def get_collid(self):
        pass
    
    def get_left(self):
        pass
    
    def get_top(self):
        pass

    def set_center(self, center : tuple):
        pass
    
    def move_left(self, px : int):
        pass

    def move_top(self, px : int):
        pass

def add_asset(image_path : str): # Add an asset by an image - return an image and the image's rect
    try:
        image = py.image.load(image_path).convert_alpha()
        rect = image.get_rect()

        return image, rect
    
    except:
        print("Erreur de génération")
        return False, False