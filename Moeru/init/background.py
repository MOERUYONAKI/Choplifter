import pygame as py
from .asset import add_asset
    
class Ground():
    def __init__(self, size : tuple = (1280, 720)):
        self.size = size
        
        parts = []
        i = 0

        while i < self.size[0] * 3:
            temp_image = py.image.load('assets\\G1.jpg').convert_alpha()
            temp_image = py.transform.scale(temp_image, (86, 172))
            temp_rect = temp_image.get_rect()

            temp_rect.top = self.size[1] - 172
            temp_rect.left = i

            parts.append((temp_image, temp_rect))
            i += 86

        self.parts = parts

    def get_parts(self):
        return self.parts
    
    def move_left(self, px : int):
        for elt in self.parts:
            elt[1].left += px

    def move_top(self, px : int):
        for elt in self.parts:
            elt[1].top += px