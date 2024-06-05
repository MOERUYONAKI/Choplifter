import pygame as py
from .asset import add_asset, Vehicule

class Jet(Vehicule):
    def __init__(self, size : tuple = (1280, 720)):
        self.size = size
        self.position = 0
        
        parts = []

        jet_image, jet_rect = add_asset('Windows\\assets\\jet.png')
        parts.append([jet_image, jet_rect, False])

        jet2_image, jet2_rect = add_asset('Windows\\assets\\revert_jet.png')
        jet2_rect.center = jet_rect.center
        parts.append([jet2_image, jet2_rect, False])

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
        self.move = move if move in [0, 1] else 0
    
    def set_center(self, center : tuple):
        for elt in self.parts:
            elt[1].center = center
    
    def move_left(self, px : int):
        if px >= 0:
            self.active_right()
            self.last = 'd'

        else:
            self.active_left()
            self.last = 'q'
            
        for elt in self.parts:
            elt[1].left += px

    def move_top(self, px : int):
        if px >= 0:
            self.last = 's'

        else:
            self.last = 'z'

        for elt in self.parts:
            elt[1].top += px

class Pew():
    def __init__(self, jet : Jet):
        self.jet = jet

        parts = []

        rightshot_image, rightshot_rect = add_asset('Windows\\assets\\jet_pew.png')
        rightshot_rect.center = (self.jet.get_left(), self.jet.get_top())
        parts.append([rightshot_image, rightshot_rect, False])

        leftshot_image, leftshot_rect = add_asset('Windows\\assets\\revert_jet_pew.png')
        leftshot_rect.center = (self.jet.get_left(), self.jet.get_top())
        parts.append([leftshot_image, leftshot_rect, False])

        self.parts = parts
        self.shot = False

    def get_parts(self):
        return self.parts

    def get_moves(self):
        moves = ''

        if self.parts[0][2] == True:
            moves += 'r'

        elif self.parts[1][2] == True:
            moves += 'l'

        return moves
    
    def get_rs_collid(self):
        return self.parts[0][1]
    
    def get_ls_collid(self):
        return self.parts[1][1]
    
    def move_left(self, px : int):
        self.parts[0][1].left += px
        self.parts[1][1].left += px

    def move_top(self, px : int):
        self.parts[0][1].top += px
        self.parts[1][1].top += px

    def reset(self):
        self.shot = False

        self.parts[0][1].center = (self.jet.get_left(), self.jet.get_top())
        self.parts[0][2] = False

        self.parts[1][1].center = (self.jet.get_left(), self.jet.get_top())
        self.parts[1][2] = False

    def shoot(self):
        if self.jet.is_right() and not self.shot:
            self.shot = True
            self.parts[0][2] = True

        elif not self.jet.is_right() and not self.shot:
            self.shot = True
            self.parts[1][2] = True

        else:
            return False