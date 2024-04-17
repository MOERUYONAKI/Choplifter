import pygame as py

def add_asset(image_path : str): # Add an asset by an image - return an image and the image's rect
    try:
        image = py.image.load(image_path).convert_alpha()
        rect = image.get_rect()

        return image, rect
    
    except:
        print("Erreur de génération")
        return False, False