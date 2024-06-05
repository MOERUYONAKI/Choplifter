import pygame as py
from .asset import add_asset, Vehicule

class Alien(Vehicule):
    def __init__(self, size : tuple = (1280, 720)):
        self.size = size
        self.move = 0
        
        parts = []

        alien_image, alien_rect = add_asset('Windows\\assets\\saucer.png')
        parts.append([alien_image, alien_rect, True])

        self.parts = parts

    def get_move(self):
        return self.move

    def get_parts(self):
        return self.parts
    
    def get_collid(self):
        for elt in self.parts:
            if elt[2]:
                return elt[1]
    
    def get_left(self):
        return self.parts[0][1].left
    
    def get_top(self):
        return self.parts[0][1].top
    
    def get_center(self):
        return self.parts[0][1].center

    def set_move(self, move : int):
        self.move = move if move in [0, 1, 2] else 0
    
    def set_center(self, center : tuple):
        self.parts[0][1].center = center
    
    def move_left(self, px : int):
        self.parts[0][1].left += px

    def move_top(self, px : int):
        self.parts[0][1].top += px

class Pew():
    def __init__(self, saucer : Alien):
        self.alien = saucer

        parts = []

        laser_image, laser_rect = add_asset('Windows\\assets\\laser.png')
        laser_rect.center = (self.alien.get_left(), self.alien.get_top())
        parts.append([laser_image, laser_rect, False])

        self.parts = parts
        self.shot = False

    def get_parts(self):
        return self.parts

    def get_shot(self):
        return self.shot
    
    def get_collid(self):
        return self.parts[0][1]
    
    def move_left(self, px : int):
        self.parts[0][1].left += px

    def move_top(self, px : int):
        self.parts[0][1].top += px

    def reset(self):
        self.shot = False

        self.parts[0][1].center = (self.alien.get_left(), self.alien.get_top())
        self.parts[0][2] = False

    def shoot(self):
        self.get_parts()[0][1].center = self.alien.get_center()
        self.move_top(15)

        self.shot = True
        self.parts[0][2] = True