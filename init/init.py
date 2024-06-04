# - - - - -  I M P O R T S  - - - - -

# - PY imports
import pygame as py
import time
import random

# - Choplifter imports
from init.asset import Vehicule, Music, add_asset
from init.background import Background
from init.chop import Chop, Pew as ChopPew
from init.tank import Tank, Pew as TankPew
from init.jet import Jet, Pew as JetPew
from init.alien import Alien, Pew as AlienPew


# - - - - -  F O N C T I O N S  - - - - -

# - Assets init
def assets_init(size : tuple):
    bg = Background(size)
    chop = Chop(size)
    pews = ChopPew(chop)

    tank1 = Tank(size)
    tank1.active_right()
    t1_pews = TankPew(tank1)

    tank2 = Tank(size)
    tank2.active_left()
    tank2.set_move(1)
    t2_pews = TankPew(tank2)

    jet1 = Jet(size)
    jet1.active_right()
    j1_pews = JetPew(jet1)

    jet2 = Jet(size)
    jet2.active_left()
    jet2.set_move(1)
    j2_pews = JetPew(jet2)

    alien = Alien(size)
    alien_pew = AlienPew(alien)

    chop.set_center(bg.get_heliport().center)
    chop.move_top(10)
    pews.reset()

    tank1.set_center((bg.get_parts()[1][1].left + int(round(0.5 * tank1.get_parts()[0][1].width, 0)), int(round(0.8 * size[1], 0))))
    tank2.set_center((3 * size[0] + tank2.get_parts()[0][1].width, int(round(0.8 * size[1], 0))))
    tank2.set_position(2 * size[0] + tank2.get_parts()[0][1].width)
    
    t1_pews.reset()
    t2_pews.reset()

    jet1.set_center((0 - jet1.get_parts()[0][1].width, random.randint(int(round(0.3 * size[1], 0)), int(round(0.9 * size[1], 0)) - 48)))
    jet2.set_center((3 * size[0] + jet2.get_parts()[0][1].width, random.randint(int(round(0.3 * size[1], 0)), int(round(0.9 * size[1], 0)) - 48)))
    jet2.set_position(3 * size[0] + jet2.get_parts()[0][1].width)

    j1_pews.reset()
    j2_pews.reset()

    alien.set_center((random.randint(int(round(0.35 * size[0], 0)), int(round(0.65 * size[0], 0))), bg.get_parts()[1][1].top - alien.get_collid().height))
    alien_pew.reset()

    assets = {
        'bg': bg,
        'chop': chop,
        'pews': pews,
        'tank1': tank1,
        't1_pews': t1_pews,
        'tank2': tank2,
        't2_pews': t2_pews,
        'jet1': jet1,
        'j1_pews': j1_pews,
        'jet2': jet2,
        'j2_pews': j2_pews,
        'alien': alien,
        'alien_pew': alien_pew
    }

    return assets


# - Bases and hostages init
def bases_init(size : tuple, bases_numbers : int):
    bases = []
    bases_lefts = []

    hostages = []
    total_hostage = 0

    for i in range(bases_numbers):
        # Création des bases
        bases.append([py.image.load('assets\\basement.png').convert_alpha()])
        bases[i][0] = py.transform.scale(bases[i][0], (81, 60))
        bases[i].append(bases[i][0].get_rect())
        bases[i].append(True)
        bases[i][1].top = size[1] - int(round(0.22 * size[1], 0))
        rdm_left = random.randint(size[0] + 100 + int(round((2 * size[0] / bases_numbers) * (i), 0)), int(round((2 * size[0] / bases_numbers) * (i + 1), 0)) + size[0] - 100)
        bases[i][1].left = rdm_left
        bases_lefts.append(rdm_left)

        # Création des otages
        hostages.append([])
        for j in range(0, random.randint(12, 32), 2):
            total_hostage += 1

            hostages[i].append([py.image.load('assets\\hostage.png').convert_alpha()])
            hostages[i].append([py.image.load('assets\\revert_hostage.png').convert_alpha()])

            hostages[i][j][0] = py.transform.scale(hostages[i][j][0], (9, 18))
            hostages[i][j].append(hostages[i][j][0].get_rect())
            hostages[i][j].append(True)

            hostages[i][j + 1][0] = py.transform.scale(hostages[i][j + 1][0], (9, 18))
            hostages[i][j + 1].append(hostages[i][j + 1][0].get_rect())

            hostages[i][j][1].top = size[1] - int(round(0.2 * size[1], 0))
            hostages[i][j + 1][1].top = hostages[i][j][1].top
            hostages[i][j][1].left = bases[i][1].left
            hostages[i][j + 1][1].left = hostages[i][j][1].left

    return bases, bases_lefts, hostages, total_hostage

# Chop collids
def chop_collid(chop : Chop, elts : list):
    if chop.get_collid().colliderect(elts[0].get_collid()): # Tank 1
        return True
    
    if chop.get_collid().colliderect(elts[1].get_collid()): # Tank 2
        return True
    
    if chop.get_collid().colliderect(elts[2].get_collid()): # Jet 1
        return True
    
    if chop.get_collid().colliderect(elts[3].get_collid()): # Jet 2
        return True
    
    if chop.get_collid().colliderect(elts[4].get_ls_collid()) or chop.get_collid().colliderect(elts[4].get_rs_collid()) and elts[4].shot == 1: # Tank pew 1
        return True
    
    if chop.get_collid().colliderect(elts[5].get_ls_collid()) or chop.get_collid().colliderect(elts[5].get_rs_collid()) and elts[5].shot == 1: # Tank pew 2
        return True
    
    if chop.get_collid().colliderect(elts[6].get_ls_collid()) or chop.get_collid().colliderect(elts[6].get_rs_collid()) and elts[6].shot == 1: # Jet pew 1
        return True
    
    if chop.get_collid().colliderect(elts[7].get_ls_collid()) or chop.get_collid().colliderect(elts[7].get_rs_collid()) and elts[7].shot == 1: # Jet pew 2
        return True
    
    if chop.get_collid().colliderect(elts[8].get_collid()): # Alien
        return True
    
    if chop.get_collid().colliderect(elts[9].get_collid()) and elts[9].shot == 1: # Alien Pew
        return True

    return False

# - ChopPews collids
def cps_collid(vehicule : Vehicule, pews : ChopPew, bg : Background):
    if (pews.get_rs_collid().colliderect(vehicule.get_parts()[0][1]) and bg.size[0] > vehicule.get_left()) or pews.get_drop_collid().colliderect(vehicule.get_parts()[0][1]) or (pews.get_ls_collid().colliderect(vehicule.get_parts()[0][1]) and 0 < vehicule.get_left()):
        vehicule.get_parts()[0][1].left = bg.get_parts()[0][1].left - vehicule.get_parts()[0][1].width
        vehicule.get_parts()[0][1].left = bg.get_parts()[2][1].left + bg.get_parts()[2][1].width
        
        return True
    
    else:
        return False

# - Tanks moves   
def tank_moves(chop : Chop, tank : Tank, pews : TankPew, bg : Background, bg_move : int):
    shot_timer = 0

    if tank.get_position() < (2 * bg.size[0] - tank.get_parts()[0][1].width) and tank.get_move() == 0:
        tank.set_position(tank.get_position() + 3)

        if not tank.is_shooting():
            tank.active_right()

        if not pews.shot and (75 < chop.get_left() - tank.get_left() and 750 > chop.get_left() - tank.get_left()):
            pews.shoot()
            shot_timer = time.time()

        if bg_move == 1: # Mouvement vers la droite
            tank.move_left(-2)

            if pews.parts[0][2]:
                pews.move_left(7)
                pews.move_top(-6)

            else:
                pews.reset()

        elif bg_move == 2: # Mouvement vers la gauche
            tank.move_left(8)

            if pews.parts[0][2]:
                pews.move_left(11)
                pews.move_top(-6)

            else:
                pews.reset()
        
        else:
            tank.move_left(3)

            if pews.parts[0][2]:
                pews.move_left(6)
                pews.move_top(-6)

            else:
                pews.reset()

    elif tank.get_position() > 0:
        tank.set_move(1)
        
        if not tank.is_shooting():
            tank.active_left()

        tank.set_position(tank.get_position() - 3)

        if not pews.shot and (75 < tank.get_left() - chop.get_left() and 750 > tank.get_left() - chop.get_left()):
            pews.shoot()
            shot_timer = time.time()
        
        if bg_move == 1: # Mouvement vers la droite
            tank.move_left(-8)

            if pews.parts[1][2]:
                pews.move_left(-11)
                pews.move_top(-6)

            else:
                pews.reset()

        elif bg_move == 2: # Mouvement vers la gauche
            tank.move_left(2)

            if pews.parts[1][2]:
                pews.move_left(-1)
                pews.move_top(-6)

            else:
                pews.reset()
        
        else:
            tank.move_left(-3)

            if pews.parts[1][2]:
                pews.move_left(-6)
                pews.move_top(-6)

            else:
                pews.reset()

    else:
        tank.set_move(0)

        if not 'r' in pews.get_moves() and not 'l' in pews.get_moves():
            pews.reset()

    return shot_timer

# - Jets moves
def jet_moves(chop: Chop, jet: Jet, pews: JetPew, bg: Background, bg_move: int):
    shot_timer = 0

    if jet.get_position() < (3 * bg.size[0] + jet.get_parts()[0][1].width) and jet.get_move() == 0:
        jet.set_position(jet.get_position() + 8)
        move = random.choice([0, 1, 3])

        if jet.get_top() > chop.get_top():
            jet.move_top(0 - move)

            if 'r' not in pews.get_moves():
                pews.move_top(0 - move)

        elif jet.get_top() < chop.get_top():
            jet.move_top(move)

            if 'r' not in pews.get_moves():
                pews.move_top(move)

        else:
            if not pews.shot and 15 < chop.get_left() - jet.get_left() < 750:
                pews.shoot()
                shot_timer = time.time()

        if bg_move == 1: # Mouvement vers la droite
            jet.move_left(3)

            if pews.parts[0][2]:
                pews.move_left(7)

            else:
                pews.reset()

        elif bg_move == 2: # Mouvement vers la gauche
            jet.move_left(13)

            if pews.parts[0][2]:
                pews.move_left(17)

            else:
                pews.reset()

        else:
            jet.move_left(8)

            if pews.parts[0][2]:
                pews.move_left(12)

            else:
                pews.reset()

    elif jet.get_position() > 0 - jet.get_parts()[0][1].width:
        jet.set_move(1)
        jet.active_left()

        jet.move_left(bg.get_parts()[2][1].left + bg.get_parts()[2][1].width if jet.get_move() == 0 else 0)
        jet.set_position(jet.get_position() - 8)
        
        move = random.choice([0, 1, 3])

        if jet.get_top() > chop.get_top():
            jet.move_top(0 - move)

            if 'l' not in pews.get_moves():
                pews.move_top(0 - move)

        elif jet.get_top() < chop.get_top():
            jet.move_top(move)

            if 'l' not in pews.get_moves():
                pews.move_top(move)

        else:
            if not pews.shot and 15 < jet.get_left() - chop.get_left() < 750:
                pews.shoot()
                shot_timer = time.time()

        if bg_move == 2: # Mouvement vers la gauche
            jet.move_left(-3)

            if pews.parts[1][2]:
                pews.move_left(-7)

            else:
                pews.reset()

        elif bg_move == 1: # Mouvement vers la droite
            jet.move_left(-13)

            if pews.parts[1][2]:
                pews.move_left(-17)

            else:
                pews.reset()

        else:
            jet.move_left(-8)

            if pews.parts[0][2]:
                pews.move_left(-12)

            else:
                pews.reset()

    else:
        jet.set_move(0)
        jet.active_right()

        if 'r' not in pews.get_moves() and 'l' not in pews.get_moves():
            pews.reset()

    return shot_timer


# - Aliens moves
def alien_moves(chop : Chop, alien : Alien, pews : AlienPew, bg : Background, bg_move : int):
    if alien.get_top() < int(round(0.1 * bg.size[1], 0)) and alien.get_move() == 1:
        alien.move_top(2)

    elif alien.get_top() >= int(round(0.1 * bg.size[1], 0)) and alien.get_move() == 1:
        move = random.randint(3, 5) if chop.get_left() > alien.get_left() else (0 - random.randint(3, 5))

        if bg_move == 1: # Mouvement vers la droite
            alien.move_left(move - 5)

            if pews.parts[0][2]:
                pews.move_left(7)

            else:
                pews.move_left(3)

        elif bg_move == 2: # Mouvement vers la gauche
            alien.move_left(move + 5)

            if pews.parts[0][2]:
                pews.move_left(17)

            else:
                pews.move_left(13)
        
        else:
            alien.move_left(move)

            if pews.parts[0][2]:
                pews.move_left(12)

            else:
                pews.move_left(8)

    elif alien.get_top() >= bg.get_parts()[1][1].top - alien.get_parts()[0][1].width and alien.get_move() == 2:
        alien.move_top(-3)

    else:
        alien.set_move(0)
        alien.set_center((random.randint(int(round(0.35 * bg.size[0], 0)), int(round(0.65 * bg.size[0], 0))), bg.get_parts()[1][1].top - alien.get_collid().height))
        pews.reset()

# - Endgame message
def end_message(base_destroyed : int, tank_destroyed : int, jet_destroyed : int, alien_destroyed : int, rescued : int):
        print(f"Ennemis éliminés : \n{base_destroyed} {'bases' if base_destroyed > 1 else 'base'} - {tank_destroyed} {'tanks' if tank_destroyed > 1 else 'tank'} - {jet_destroyed} {'jets' if jet_destroyed > 1 else 'jet'} - {alien_destroyed} {'aliens' if alien_destroyed > 1 else 'alien'}")
        print(f"{rescued} {'otages secourus' if rescued > 1 else 'otage secouru'}")