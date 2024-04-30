import pygame as py
from .asset import add_asset, Vehicule

class Tank(Vehicule):
    def __init__(self, size : tuple = (1280, 720)):
        self.size = size
        self.position = 0
        
        parts = []

        tank_image, tank_rect = add_asset('assets\\tank.png')
        parts.append([tank_image, tank_rect, False])

        tank2_image, tank2_rect = add_asset('assets\\revert_tank.png')
        tank2_rect.center = tank_rect.center
        parts.append([tank2_image, tank2_rect, False])

        tank3_image, tank3_rect = add_asset('assets\\shooting_tank.png')
        parts.append([tank3_image, tank3_rect, False])

        tank4_image, tank4_rect = add_asset('assets\\revert_shooting_tank.png')
        tank4_rect.center = tank_rect.center
        parts.append([tank4_image, tank4_rect, False])

        self.parts = parts
        self.position = 0
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
        return True if self.parts[0][2] or self.parts[2][2] else False
    
    def is_shooting(self):
        if self.parts[2][2] or self.parts[3][2]:
            return True
            
    def active_right(self):
        self.parts[0][2] = True
        self.parts[1][2] = False
        self.parts[2][2] = False
        self.parts[3][2] = False
            
    def active_left(self):
        self.parts[0][2] = False
        self.parts[1][2] = True
        self.parts[2][2] = False
        self.parts[3][2] = False

    def active_shooting(self):
        self.parts[2][2] = True if self.is_right() else False
        self.parts[3][2] = False if self.is_right() else True
        self.parts[0][2] = False
        self.parts[1][2] = False

    def set_position(self, px : int):
        self.position = px

    def set_move(self, move : int):
        self.move = move if move in [0, 1] else 0
    
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
    def __init__(self, tank : Tank):
        self.tank = tank

        parts = []

        rightshot_image, rightshot_rect = add_asset('assets\\tank_pew.png')
        rightshot_rect.center = (self.tank.get_left(), self.tank.get_top())
        parts.append([rightshot_image, rightshot_rect, False])

        leftshot_image, leftshot_rect = add_asset('assets\\revert_tank_pew.png')
        leftshot_rect.center = (self.tank.get_left(), self.tank.get_top())
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

        self.parts[0][1].center = (self.tank.get_left(), self.tank.get_top())
        self.parts[0][2] = False

        self.parts[1][1].center = (self.tank.get_left(), self.tank.get_top())
        self.parts[1][2] = False

    def shoot(self):
        if self.tank.is_right() and not self.shot:
            self.tank.active_shooting()
            self.shot = True
            self.parts[0][2] = True

        elif not self.tank.is_right() and not self.shot:
            self.tank.active_shooting()
            self.shot = True
            self.parts[1][2] = True

        else:
            return False