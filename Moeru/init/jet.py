import pygame as py
from .asset import add_asset
    
class Jet():
    def __init__(self, size : tuple = (1280, 720)):
        self.size = size
        
        parts = []

        jet_image, jet_rect = add_asset('assets\\jet.png')
        parts.append([jet_image, jet_rect, False])

        jet2_image, jet2_rect = add_asset('assets\\revert_jet.png')
        jet2_rect.center = jet_rect.center
        parts.append([jet2_image, jet2_rect, False])

        self.parts = parts

    def get_parts(self):
        return self.parts
    
    def get_collid(self):
        for elt in self.parts:
            if elt[2] == True:
                return elt[1]
    
    def get_left(self):
        return self.parts[0][1].left
    
    def get_top(self):
        return self.parts[0][1].top
    
    def is_grounded(self):
        for i in range(len(self.parts)):
            if self.parts[i][2] == True:
                return 0 if i != 3 else 1
            
    def active_right(self):
        self.parts[0][2] = True
        self.parts[1][2] = False
            
    def active_left(self):
        self.parts[0][2] = False
        self.parts[1][2] = True
    
    def set_center(self, center : tuple):
        for elt in self.parts:
            elt[1].center = center
    
    def move_left(self, px : int):
        if px >= 0:
            self.last = 'd'

        else:
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

        rightshot_image, rightshot_rect = add_asset('assets\\jet_pew.png')
        rightshot_rect.center = (self.jet.get_left(), self.jet.get_top())
        parts.append([rightshot_image, rightshot_rect, False])

        leftshot_image, leftshot_rect = add_asset('assets\\revert_jet_pew.png')
        leftshot_rect.center = (self.jet.get_left(), self.jet.get_top())
        parts.append([leftshot_image, leftshot_rect, False])

        self.parts = parts

    def get_moves(self):
        moves = ''

        if self.parts[0][2] == True:
            moves += 'r'

        elif self.parts[2][2] == True:
            moves += 'l'

        if self.parts[1][2] == True:
            moves += 'd'

        return moves
    
    def get_rs_collid(self):
        return self.parts[0][1]
    
    def get_ls_collid(self):
        return self.parts[2][1]
    
    def move_left_rs(self, px : int):
        self.parts[0][1].left += px

    def move_top_rs(self, px : int):
        self.parts[0][1].top += px

    def reset_rs(self):
        self.parts[0][1].center = (self.jet.get_left(), self.jet.get_top())
        self.parts[0][2] = False
    
    def move_left_ls(self, px : int):
        self.parts[2][1].left += px

    def move_top_ls(self, px : int):
        self.parts[2][1].top += px

    def reset_ls(self):
        self.parts[2][1].center = (self.jet.get_left(), self.jet.get_top())
        self.parts[2][2] = False

    def reset(self):
        self.reset_rs()
        self.reset_ls()