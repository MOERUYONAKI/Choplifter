import pygame as py
from .asset import add_asset, Vehicule
    
class Chop(Vehicule):
    def __init__(self, size : tuple = (1280, 720)):
        self.size = size
        
        parts = []

        chop_image, chop_rect = add_asset('assets\\helicopter.png')
        parts.append([chop_image, chop_rect, False])

        chop2_image, chop2_rect = add_asset('assets\\revert_helicopter.png')
        chop2_rect.center = chop_rect.center
        parts.append([chop2_image, chop2_rect, False])

        chop3_image, chop3_rect = add_asset('assets\\helico_ball.png')
        chop3_rect.center = chop_rect.center
        parts.append([chop3_image, chop3_rect, False])

        chop4_image, chop4_rect = add_asset('assets\\grounded_helicopter.png')
        chop4_rect.center = chop_rect.center
        parts.append([chop4_image, chop4_rect, True])

        self.parts = parts
        self.last = 's'

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
        for elt in self.parts:
            elt[2] = False
            
        self.parts[0][2] = True
            
    def active_left(self):
        for elt in self.parts:
            elt[2] = False
            
        self.parts[1][2] = True
            
    def active_up(self):
        for elt in self.parts:
            elt[2] = False
            
        self.parts[2][2] = True
            
    def active_grounded(self):
        for elt in self.parts:
            elt[2] = False
            
        self.parts[3][2] = True
    
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
    def __init__(self, chop : Chop):
        self.chop = chop

        parts = []

        rightshot_image, rightshot_rect = add_asset('assets\\green_pewpew.png')
        rightshot_rect.center = (self.chop.get_left() + 32, self.chop.get_top() + 24)
        parts.append([rightshot_image, rightshot_rect, False])

        drop_image, drop_rect = add_asset('assets\\green_pewpew2.png')
        drop_rect.center = (self.chop.get_left() + 32, self.chop.get_top() + 24)
        parts.append([drop_image, drop_rect, False])

        leftshot_image, leftshot_rect = add_asset('assets\\green_revert_pewpew.png')
        leftshot_rect.center = (self.chop.get_left() + 32, self.chop.get_top() + 24)
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
    
    def get_drop_collid(self):
        return self.parts[1][1]
    
    def get_ls_collid(self):
        return self.parts[2][1]
    
    def move_left_rs(self, px : int):
        self.parts[0][1].left += px

    def move_top_rs(self, px : int):
        self.parts[0][1].top += px

    def reset_rs(self):
        self.parts[0][1].center = (self.chop.get_left() + 32, self.chop.get_top() + 24)
        self.parts[0][2] = False
    
    def move_left_drop(self, px : int):
        self.parts[1][1].left += px

    def move_top_drop(self, px : int):
        self.parts[1][1].top += px

    def reset_drop(self):
        self.parts[1][1].center = (self.chop.get_left() + 32, self.chop.get_top() + 24)
        self.parts[1][2] = False
    
    def move_left_ls(self, px : int):
        self.parts[2][1].left += px

    def move_top_ls(self, px : int):
        self.parts[2][1].top += px

    def reset_ls(self):
        self.parts[2][1].center = (self.chop.get_left() + 32, self.chop.get_top() + 24)
        self.parts[2][2] = False

    def reset(self):
        self.reset_rs()
        self.reset_drop()
        self.reset_ls()