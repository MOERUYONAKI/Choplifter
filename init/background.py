import pygame as py
from .asset import add_asset
    
class Background():
    def __init__(self, size : tuple = (1280, 720)):
        self.size = size

        parts = []

        base_bg_image = py.image.load('assets\\bg1.png').convert_alpha()
        base_bg_image = py.transform.scale(base_bg_image, size)
        base_bg_rect = base_bg_image.get_rect()
        parts.append([base_bg_image, base_bg_rect])

        part1_bg_image = py.image.load('assets\\bg2.png').convert_alpha()
        part1_bg_image = py.transform.scale(part1_bg_image, size)
        part1_bg_rect = part1_bg_image.get_rect()
        part1_bg_rect.left = size[0]
        parts.append([part1_bg_image, part1_bg_rect])

        part2_bg_image = py.image.load('assets\\bg3.png').convert_alpha()
        part2_bg_image = py.transform.scale(part2_bg_image, size)
        part2_bg_rect = part2_bg_image.get_rect()
        part2_bg_rect.left = 2 * size[0]
        parts.append([part2_bg_image, part2_bg_rect])

        self.parts = parts
        self.heliport = py.Rect(int(round(0.48125 * size[0], 0)), int(round(0.764 * size[1], 0)), 15, 15)
        self.position = 0 # Min 0 - max 2 * size[0]

    def get_parts(self):
        return self.parts
    
    def get_heliport(self):
        return self.heliport
    
    def get_position(self):
        return self.position
    
    def get_left(self):
        return self.parts[0][1].left
    
    def get_right(self):
        return self.parts[2][1].left
    
    def move_left(self, px : int):
        self.position -= px
        self.heliport.left += px

        for elt in self.parts:
            elt[1].left += px