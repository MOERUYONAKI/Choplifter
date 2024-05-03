import pygame as py
from .asset import add_asset, Vehicule

class Alien(Vehicule):
    def __init__(self, size : tuple = (1280, 720)):
        self.size = size
        self.position = 0
        
        parts = []

        jet_image, jet_rect = add_asset('assets\\saucer.png')
        parts.append([jet_image, jet_rect, True])

        self.parts = parts
        self.position = 0 - self.parts[0][1].width
        self.move = 0

    def get_position(self):
        return self.position

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
    
    def is_right(self):
        return True if self.parts[0][2] else False
            
    def active_right(self):
        self.parts[0][2] = True
        self.parts[1][2] = False
            
    def active_left(self):
        self.parts[0][2] = False
        self.parts[1][2] = True

    def set_position(self, px : int):
        self.position = px

    def set_move(self, move : int):
        self.move = move if move in [0, 1, 2] else 0
    
    def set_center(self, center : tuple):
        for elt in self.parts:
            elt[1].center = center
    
    def move_left(self, px : int):
        for elt in self.parts:
            elt[1].left += px

    def move_top(self, px : int):
        for elt in self.parts:
            elt[1].top += px

class Pew():
    def __init__(self, saucer : Alien):
        self.alien = saucer

        parts = []

        rightshot_image, rightshot_rect = add_asset('assets\\jet_pew.png')
        rightshot_rect.center = (self.alien.get_left(), self.alien.get_top())
        parts.append([rightshot_image, rightshot_rect, False])

        self.parts = parts
        self.shot = False

    def get_parts(self):
        return self.parts

    def get_moves(self):
        return self.shot
    
    def get_collid(self):
        return self.parts[0][1]
    
    def move_left(self, px : int):
        self.parts[0][1].left += px
        self.parts[1][1].left += px

    def move_top(self, px : int):
        self.parts[0][1].top += px
        self.parts[1][1].top += px

    def reset(self):
        self.shot = False

        self.parts[0][1].center = (self.alien.get_left(), self.alien.get_top())
        self.parts[0][2] = False

    def shoot(self):
        self.shot = True
        self.parts[0][2] = True