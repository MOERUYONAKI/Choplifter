import pygame as py
import time
import random

from init.asset import add_asset
from init.background import Ground
from init.chop import Chop, Pew

def choplifter(size : tuple = (1280, 720)):
    bg_move = 0
    lives = 3
    based = 1

    tank_position = 0
    tank_move = 0
    tank_destroyed = 0

    tank2_move = 1

    jet_move = 0
    jet_destroyed = 0

    alien_move = 0
    alien_destroyed = 0
    alien_altitude = random.randint(int(round(0.2 * size[1])), int(round(0.4 * size[1])))

    bases_numbers = random.randint(2, 3)
    bases = []
    base_destroyed = 0
    bases_lefts = []

    hostages = []
    hostages_number = 0
    total_hostage = 0
    inside = 0
    rescued = 0

    # pygame setup
    py.init()

    start_timer = time.time()

    screen = py.display.set_mode(size)

    cms_font = py.font.Font('C:\\Windows\\WinSxS\\amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404\\comicbd.ttf', 24)
    loadtxt = cms_font.render(f'CHOPLIFTER - Loading...', True, (254, 254, 254, 0))
    loadtxt_rect = loadtxt.get_rect()
    loadtxt_rect.center = (size[0] // 2, size[1] - 25)
    screen.blit(loadtxt, loadtxt_rect)
    py.display.flip()

    clock = py.time.Clock()
    running = True

    surface = py.display.get_surface()

    ground = Ground(size)
    chop = Chop(size)
    pews = Pew(chop)

    bg = py.image.load('assets\\background.png').convert_alpha()
    bg = py.transform.scale(bg, size)
    bg_rect = bg.get_rect()
    bg_rect.left += size[0]

    bg0 = py.image.load('assets\\background2.png').convert_alpha()
    bg0 = py.transform.scale(bg0, size)
    bg0_rect = bg0.get_rect()

    bg2 = py.image.load('assets\\background2.png').convert_alpha()
    bg2 = py.transform.scale(bg2, size)
    bg2_rect = bg2.get_rect()
    bg2_rect.left = bg_rect.left + size[0]

    helibase_image = py.image.load('assets\\heli_base.png').convert_alpha()
    helibase_image = py.transform.scale(helibase_image, (186, 256))
    helibase_rect = helibase_image.get_rect()
    helibase_rect.top = size[1] - (helibase_rect.height) - 60
    helibase_rect.left = int(round(0.4 * bg0_rect.width, 0)) - helibase_rect.width

    heliport_image = py.image.load('assets\\heliport.png').convert_alpha()
    heliport_image = py.transform.scale(heliport_image, (128, 45))
    heliport_rect = heliport_image.get_rect()
    heliport_rect.top = size[1] - heliport_rect.height - 32
    heliport_rect.left = int(round(0.4 * bg0_rect.width, 0)) - int(round(0.3 * helibase_rect.width))

    chop.set_center(heliport_rect.center)
    chop.move_top(10)
    pews.reset()

    title = cms_font.render(f'CHOPLIFTER - {lives} lives', True, (0, 0, 0, 0))
    title_rect = title.get_rect()
    title_rect.center = (size[0] // 2, 12)

    tank_image, tank_rect = add_asset('assets\\tank.png')
    tank_rect.top = size[1] - 75
    tank_rect.left = bg_rect.left

    tank2_image, tank2_rect = add_asset('assets\\revert_tank.png')
    tank2_rect.top = size[1] - 75
    tank2_rect.left = bg2_rect.left + bg2_rect.width - tank_rect.width

    tank3_image, tank3_rect = add_asset('assets\\tank.png')
    tank3_rect.top = size[1] - 75
    tank3_rect.left = bg_rect.left

    tank4_image, tank4_rect = add_asset('assets\\revert_tank.png')
    tank4_rect.top = size[1] - 75
    tank4_rect.left = bg2_rect.left + bg2_rect.width - tank3_rect.width
    
    tank2_position = (2 * size[0] - tank_rect.width)

    jet_image, jet_rect = add_asset('assets\\jet.png')
    jet_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0))) - 48
    jet_rect.left = jet_rect.width

    jet_position = bg0_rect.left - jet_rect.width

    jet2_image, jet2_rect = add_asset('assets\\revert_jet.png')
    jet2_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0))) - 48
    jet2_rect.left = bg2_rect.left + bg2_rect.width 

    alien_image = py.image.load('assets\\saucer.png').convert_alpha()
    alien_image = py.transform.scale(alien_image, (42, 38))
    alien_rect = alien_image.get_rect()
    alien_rect.top = bg_rect.top - alien_rect.height

    for i in range(bases_numbers):
        # Création des bases
        bases.append([py.image.load('assets\\basement.png').convert_alpha()])
        bases[i][0] = py.transform.scale(bases[i][0], (81, 60))
        bases[i].append(bases[i][0].get_rect())
        bases[i].append(True)
        bases[i][1].top = size[1] - 150
        rdm_left = random.randint(size[0] + 100 + int(round((2 * size[0] / bases_numbers) * (i), 0)), int(round((2 * size[0] / bases_numbers) * (i + 1), 0)) + size[0] - 100)
        bases[i][1].left = rdm_left
        bases_lefts.append(rdm_left)

        # Création des otages
        hostages.append([])
        for j in range(0, random.randint(4, 10), 2):
            hostages_number += 1
            total_hostage += 1

            hostages[i].append([py.image.load('assets\\hostage.png').convert_alpha()])
            hostages[i].append([py.image.load('assets\\revert_hostage.png').convert_alpha()])

            hostages[i][j][0] = py.transform.scale(hostages[i][j][0], (9, 18))
            hostages[i][j].append(hostages[i][j][0].get_rect())
            hostages[i][j].append(True)

            hostages[i][j + 1][0] = py.transform.scale(hostages[i][j + 1][0], (9, 18))
            hostages[i][j + 1].append(hostages[i][j + 1][0].get_rect())

            hostages[i][j][1].top = (size[1] - hostages[i][j][1].height) + 1
            hostages[i][j + 1][1].top = hostages[i][j][1].top
            hostages[i][j][1].left = bases[i][1].left
            hostages[i][j + 1][1].left = hostages[i][j][1].left

    while running:
        # poll for events
        pressed = py.key.get_pressed()
        bg_move = 0

        if pressed[py.K_z]: # - Haut
            based = 0

            chop.active_up()
            chop.move_top(-5)

            if 'l' not in pews.get_moves():
                pews.move_top_ls(-5)

            if 'r' not in pews.get_moves():
                pews.move_top_rs(-5)

            if 'd' not in pews.get_moves():
                pews.move_top_drop(-5)

            if chop.get_top() < 0:
                chop.move_top(0 - chop.get_top())

                if 'l' not in pews.get_moves():
                    pews.reset_ls()

                if 'r' not in pews.get_moves():
                    pews.reset_rs()

                if 'd' not in pews.get_moves():
                    pews.reset_drop()

        if pressed[py.K_s] and chop.is_grounded() == 0: # - Bas
            chop.active_up()
            chop.move_top(5)

            if 'l' not in pews.get_moves():
                pews.move_top_ls(+5)

            if 'r' not in pews.get_moves():
                pews.move_top_rs(+5)

            if 'd' not in pews.get_moves():
                pews.move_top_drop(+5)

            if chop.get_top() > size[1] - 32:
                chop.active_grounded()

                chop.move_top(size[1] - chop.get_top() - 32)

                if 'l' not in pews.get_moves():
                    pews.reset_ls()

                if 'r' not in pews.get_moves():
                    pews.reset_rs()

                if 'd' not in pews.get_moves():
                    pews.reset_drop()

        if pressed[py.K_q] and chop.is_grounded() == 0: # - Gauche  
            chop.active_left()

            if chop.get_left() < int(round(0.3 * size[0], 0)) and bg0_rect.left < 0:
                bg_move = 2

                if bg0_rect.left <= 5:
                    bg_rect.left += 5
                    bg0_rect.left += 5
                    bg2_rect.left += 5
                    ground.move_left(5)
                    for base in bases:
                        base[1].left += 5

                else:
                    bg_rect.left -= bg0_rect.left
                    bg2_rect.left -= bg0_rect.left
                    ground.move_left(0 - bg0_rect.left)
                    for base in bases:
                        base[1].left -= bg2_rect.left
                    bg0_rect.left = 0

            else:
                chop.move_left(-5)

                if 'l' not in pews.get_moves():
                    pews.move_left_ls(-5)

                if 'r' not in pews.get_moves():
                    pews.move_left_rs(-5)

                if 'd' not in pews.get_moves():
                    pews.move_left_drop(-5)

                if chop.get_left() < 0:
                    chop.move_left(0 - chop.get_left())

                    if 'l' not in pews.get_moves():
                        pews.reset_ls()

                    if 'r' not in pews.get_moves():
                        pews.reset_rs()

                    if 'd' in pews.get_moves():
                        pews.reset_drop()

        if pressed[py.K_d] and chop.is_grounded() == 0: # - Droite
            chop.active_right()

            if chop.get_left() > (size[0] - int(round(0.3 * size[0], 0))) and bg2_rect.left > 0:
                bg_move = 1

                if bg2_rect.left >= 5:
                    bg_rect.left -= 5
                    bg0_rect.left -= 5
                    bg2_rect.left -= 5
                    ground.move_left(-5)
                    for base in bases:
                        base[1].left -= 5

                else:
                    bg_rect.left -= bg2_rect.left
                    bg0_rect.left -= bg2_rect.left
                    ground.move_left(0 - bg2_rect.left)
                    for base in bases:
                        base[1].left -= bg2_rect.left
                    bg2_rect.left = 0  
            
            else:
                chop.move_left(5)

                if 'l' not in pews.get_moves():
                    pews.move_left_ls(5)

                if 'r' not in pews.get_moves():
                    pews.move_left_rs(5)

                if 'd' not in pews.get_moves():
                    pews.move_left_drop(5)

                if chop.get_left() > size[0] - 64:
                    chop.set_center(chop.get_top(), size[0] - 64)

                    if 'l' not in pews.get_moves():
                        pews.reset_ls()

                    if 'r' not in pews.get_moves():
                        pews.reset_rs()

                    if 'd' not in pews.get_moves():
                        pews.reset_drop()

        for event in py.event.get():
            if event.type == py.QUIT:
                print(f"\nEnnemis éliminés : \n{base_destroyed} bases - {tank_destroyed} tanks - {jet_destroyed} jets - {alien_destroyed} aliens")
                print(f"{rescued} otages secourus")
                running = False # end of the loop

                if event.key == py.K_z: # Haut
                    print("L'utilisateur se déplace sur le haut !")

                if event.key == py.K_q: # Gauche
                    print("L'utilisateur se déplace sur la gauche !")

                if event.key == py.K_s: # Bas
                    print("L'utilisateur se déplace sur le bas !")

                if event.key == py.K_d: # Droite
                    print("L'utilisateur se déplace sur la droite !")

            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE: # Tir bas
                    if 'd' not in pews.get_moves() and chop.is_grounded() == 0:
                        pews.parts[1][2] = True
                        print("L'utilisateur tir !")

            if event.type == py.MOUSEBUTTONDOWN:
                if 'r' not in pews.get_moves() and 'l' not in pews.get_moves() and event.button == 1: # 1 - Click gauche
                    if chop.last == 'd': # Tir droit
                        pews.parts[0][2] = True
                        basic_shot_start = time.time()
                        print("L'utilisateur tir !")

                    elif chop.last == 'q': # Tir gauche
                        pews.parts[2][2] = True
                        basic_shot_start = time.time()
                        print("L'utilisateur tir !")

                    else:
                        print("Impossible de tirer !")

        # RENDER YOUR GAME HERE
        if 'r' in pews.get_moves() or 'l' in pews.get_moves():
            if 'r' in pews.get_moves(): # mouvement du tir (droite)
                if pews.parts[0][1].left <= bg2_rect.left - 5:
                    if bg_move == 1: # Mouvement vers la droite
                        pews.move_left_rs(5)

                    elif bg_move == 2: # Mouvement vers la gauche
                        pews.move_left_rs(15)
                    
                    else:
                        pews.move_left_rs(10)

                elif pews.parts[0][1].left > bg2_rect.left + 18:
                    pews.parts[0][1].left = bg2_rect.left + 18

                if (time.time() - basic_shot_start) > 1.5:
                    pews.reset_rs()
                    print("Le tir est de nouveau prêt !")

            elif 'l' in pews.get_moves(): # mouvement du tir (gauche)
                if pews.parts[2][1].left >= bg0_rect.left - 5:
                    if bg_move == 2: # Mouvement vers la gauche
                        pews.move_left_ls(-5)

                    elif bg_move == 1: # Mouvement vers la droite
                        pews.move_left_ls(-15)
                    
                    else:
                        pews.move_left_ls(-10)

                elif pews.parts[2][1].left > bg_rect.left - 18:
                    pews.parts[2][1].left = bg_rect.left - 18

                if (time.time() - basic_shot_start) > 1.5:
                    pews.reset_ls()
                    print("Le tir est de nouveau prêt !")

        if 'd' in pews.get_moves(): # mouvement du tir (bas)
            if bg_move == 1: # Mouvement vers la droite
                pews.move_left_drop(-5)

            elif bg_move == 2: # Mouvement vers la gauche
                pews.move_left_drop(5)
            
            pews.move_top_drop(8)

            if pews.parts[1][1].top >= size[1]:
                pews.reset_drop()
                print("Le tir est de nouveau prêt !")

        # Tanks moves - 1st tank
        if tank_position < (2 * size[0] - tank_rect.width) and tank_move == 0:
            tank_position += 3

            if bg_move == 1: # Mouvement vers la droite
                tank_rect.left -= 2

            elif bg_move == 2: # Mouvement vers la gauche
                tank_rect.left += 8
            
            else:
                tank_rect.left += 3

        elif tank_position > 0:
            tank2_rect.left = bg2_rect.left + bg2_rect.width - tank2_rect.width if tank_move == 0 else tank2_rect.left

            tank_move = 1
            tank_position -= 3
            
            if bg_move == 1: # Mouvement vers la droite
                tank2_rect.left -= 8

            elif bg_move == 2: # Mouvement vers la gauche
                tank2_rect.left += 2
            
            else:
                tank2_rect.left -= 3

        else:
            tank_position = 0
            tank_move = 0
            tank_rect.left = bg_rect.left
            tank2_rect.left = bg2_rect.left + bg2_rect.width - tank2_rect.width

        # - 2nd tank
        if tank2_position < (2 * size[0] - tank3_rect.width) and tank2_move == 0:
            tank2_position += 3

            if bg_move == 1: # Mouvement vers la droite
                tank3_rect.left -= 2

            elif bg_move == 2: # Mouvement vers la gauche
                tank3_rect.left += 8
            
            else:
                tank3_rect.left += 3

        elif tank2_position > 0 and int(round(time.time() - start_timer, 0)) > 15:
            tank4_rect.left = bg2_rect.left + bg2_rect.width - tank4_rect.width if tank2_move == 0 else tank4_rect.left

            tank2_move = 1
            tank2_position -= 3
            
            if bg_move == 1: # Mouvement vers la droite
                tank4_rect.left -= 8

            elif bg_move == 2: # Mouvement vers la gauche
                tank4_rect.left += 2
            
            else:
                tank4_rect.left -= 3

        else:
            tank2_position = 0
            tank2_move = 0
            tank3_rect.left = bg_rect.left
            tank4_rect.left = bg2_rect.left + bg2_rect.width - tank4_rect.width

        # Jets moves
        if jet_position < (2 * size[0]) and jet_move == 0 and int(round(time.time() - start_timer, 0)) > 15: # arrivée après 15 secondes de jeu
            jet_position += 8

            if jet_rect.top > chop.get_top():
                jet_rect.top -= random.choice([0, 1, 3])

            elif jet_rect.top < chop.get_top():
                jet_rect.top += random.choice([0, 1, 3])

            if bg_move == 1: # Mouvement vers la droite
                jet_rect.left += 3

            elif bg_move == 2: # Mouvement vers la gauche
                jet_rect.left += 13
            
            else:
                jet_rect.left += 8

        elif jet_position > 0 - size[0] - jet_rect.width:
            jet2_rect.left = bg2_rect.left + bg2_rect.width if jet_move == 0 else jet2_rect.left

            jet_move = 1
            jet_position -= 8

            if jet2_rect.top > chop.get_top():
                jet2_rect.top -= random.choice([0, 1, 3])

            elif jet2_rect.top < chop.get_top():
                jet2_rect.top += random.choice([0, 1, 3])
            
            if bg_move == 1: # Mouvement vers la droite
                jet2_rect.left -= 13

            elif bg_move == 2: # Mouvement vers la gauche
                jet2_rect.left -= 3
            
            else:
                jet2_rect.left -= 8

        else:
            jet_position = 0 - size[0] - jet_rect.width
            jet_move = 0
            jet_rect.left = bg0_rect.left - jet_rect.width
            jet2_rect.left = bg2_rect.left + bg2_rect.width 
            jet_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0)))
            jet2_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0)))

        # Aliens moves
        if int(round(time.time() - start_timer, 0) + 1) % 12 == 0 and int(round(time.time() - start_timer, 0) + 1) > 45 and alien_move == 0: # Arrivée après 45 secondes de jeu / toute les 15 secondes
            alien_move = 1
            alien_rect.left = random.randint(int(round(0.75 * chop.get_left(), 0)), int(round(1.2 * chop.get_left(), 0)))
        
        if alien_move != 0:
            if alien_rect.top < alien_altitude and alien_move == 1:
                alien_rect.top += 1
                alien_rect.left += random.choice([-12, -8, -5, -3, -1, 0, 1, 3, 5, 8, 12])

            elif alien_rect.top >= bg_rect.top:
                alien_move = 2
                alien_rect.top -= 2
                alien_rect.left += random.choice([-12, -8, -5, -3, -1, 0, 1, 3, 5, 8, 12])

            else:
                alien_move = 0
                alien_rect.top = bg_rect.top - alien_rect.height

        # Collision events
        if chop.get_collid().colliderect(tank_rect) or chop.get_collid().colliderect(tank2_rect) or chop.get_collid().colliderect(tank3_rect) or chop.get_collid().colliderect(tank4_rect) or chop.get_collid().colliderect(jet_rect) or chop.get_collid().colliderect(jet2_rect) or chop.get_collid().colliderect(alien_rect):
            if lives == 1:
                print("Hélicoptère détruit... \n")
                print(f"Ennemis éliminés : \n{base_destroyed} bases - {tank_destroyed} tanks - {jet_destroyed} jets - {alien_destroyed} aliens")
                print(f"{rescued} otages secourus")
                running = False

            else:
                print("Hélicoptère détruit...")
                lives -= 1

                bg0_rect.left = 0
                bg_rect.left = size[0]
                bg2_rect.left = bg_rect.left + size[0]

                helibase_rect.top = size[1] - (helibase_rect.height)
                helibase_rect.left = int(round(0.4 * bg0_rect.width, 0)) - helibase_rect.width

                heliport_rect.top = size[1] - heliport_rect.height - 8
                heliport_rect.left = int(round(0.4 * bg0_rect.width, 0))

                chop.active_grounded()
                chop.set_center(heliport_rect.center)
                chop.move_top(10)
                pews.reset()

                tank_rect.left = bg_rect.left
                tank2_rect.left = bg2_rect.left + bg2_rect.width - tank_rect.width
                tank3_rect.left = bg_rect.left
                tank4_rect.left = bg2_rect.left + bg2_rect.width - tank3_rect.width

                for k in range(len(bases)):
                    bases[k][1].left = bases_lefts[k]

                    for l in range(0, len(hostages[k]), 2):
                        if hostages[k][l][2] == False:
                            hostages[k][l][2] = None
                            hostages_number -= 1                            
                            
                            hostages[k][l][1].top = 0 - 250
                            hostages[k][l + 1][1].top = 0 - 250

                            print("Un otage a succombé")

        if chop.get_collid().colliderect(heliport_rect) and chop.last == 's': # Atterrissage
            based = 1

            chop.set_center(heliport_rect.center)
            chop.move_top(10)

        if pews.get_rs_collid().colliderect(tank_rect) or pews.get_drop_collid().colliderect(tank_rect) or pews.get_ls_collid().colliderect(tank_rect):
            tank_position = 2 * size[0] - tank_rect.width
            tank_move = 1
            tank_rect.left = bg_rect.left
            tank2_rect.left =  bg2_rect.left + bg2_rect.width - tank2_rect.width

            print("Tank détruit !")
            tank_destroyed += 1

        if pews.get_rs_collid().colliderect(tank2_rect) or pews.get_drop_collid().colliderect(tank2_rect) or pews.get_ls_collid().colliderect(tank2_rect):
            tank_position = 0
            tank_move = 0
            tank_rect.left = bg_rect.left
            tank2_rect.left = bg2_rect.left + bg2_rect.width - tank2_rect.width

            print("Tank détruit !")
            tank_destroyed += 1

        if pews.get_rs_collid().colliderect(tank3_rect) or pews.get_drop_collid().colliderect(tank3_rect) or pews.get_ls_collid().colliderect(tank3_rect):
            tank2_position = 2 * size[0] - tank3_rect.width
            tank2_move = 1
            tank3_rect.left = bg_rect.left
            tank4_rect.left =  bg2_rect.left + bg2_rect.width - tank4_rect.width

            print("Tank détruit !")
            tank_destroyed += 1

        if pews.get_rs_collid().colliderect(tank4_rect) or pews.get_drop_collid().colliderect(tank4_rect) or pews.get_ls_collid().colliderect(tank4_rect):
            tank2_position = 0
            tank2_move = 0
            tank3_rect.left = bg_rect.left
            tank4_rect.left =  bg2_rect.left + bg2_rect.width - tank4_rect.width

            print("Tank détruit !")
            tank_destroyed += 1

        if pews.get_rs_collid().colliderect(jet_rect) or pews.get_drop_collid().colliderect(jet_rect) or pews.get_ls_collid().colliderect(jet_rect):
            jet_position = bg2_rect.left + bg2_rect.width 
            jet_move = 1
            jet_rect.left = bg0_rect.left - jet_rect.width
            jet2_rect.left = bg2_rect.left + bg2_rect.width 

            print("Jet détruit !")
            jet_destroyed += 1

        if pews.get_rs_collid().colliderect(jet2_rect) or pews.get_drop_collid().colliderect(jet2_rect) or pews.get_ls_collid().colliderect(jet2_rect):
            jet_position = 0 - jet_rect.width
            jet_move = 0
            jet_rect.left = bg0_rect.left - jet_rect.width
            jet2_rect.left = bg2_rect.left + bg2_rect.width 

            print("Jet détruit !")
            jet_destroyed += 1

        if pews.get_rs_collid().colliderect(alien_rect) or pews.get_drop_collid().colliderect(alien_rect) or pews.get_ls_collid().colliderect(alien_rect):
            alien_move = 0
            alien_rect.top = bg_rect.top - alien_rect.height

            print("Alien éliminé !")
            alien_destroyed += 1

        for base in bases:
            if pews.get_rs_collid().colliderect(base[1]) or pews.get_drop_collid().colliderect(base[1]) or pews.get_ls_collid().colliderect(base[1]):
                base[1].top = 0 - 250
                base[2] = False

                print("Bâtiment détruit !")
                base_destroyed += 1

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("lavender")
        screen.blit(bg, bg_rect)
        screen.blit(bg0, bg0_rect)
        screen.blit(bg2, bg2_rect)

        # Texts
        title = cms_font.render(f'CHOPLIFTER - {lives} lives', True, (0, 0, 0, 0))
        screen.blit(title, title_rect)

        # Assets
        for elt in ground.get_parts():
            screen.blit(elt[0], elt[1])

        helibase_rect.top = size[1] - (helibase_rect.height) - 60
        helibase_rect.left = bg0_rect.left + int(round(0.4 * bg0_rect.width, 0)) - helibase_rect.width
        screen.blit(helibase_image, helibase_rect)

        heliport_rect.top = size[1] - heliport_rect.height - 32
        heliport_rect.left = bg0_rect.left + int(round(0.4 * bg0_rect.width, 0)) - int(round(0.3 * helibase_rect.width))
        screen.blit(heliport_image, heliport_rect)

        if tank_move == 0:
            screen.blit(tank_image, tank_rect)

        elif tank_move == 1:
            screen.blit(tank2_image, tank2_rect)

        if tank2_move == 0:
            screen.blit(tank3_image, tank3_rect)

        elif tank2_move == 1:
            screen.blit(tank4_image, tank4_rect)

        if jet_move == 0:

            screen.blit(jet_image, jet_rect)
        
        elif jet_move == 1:
            screen.blit(jet2_image, jet2_rect)

        if alien_move != 0:
            screen.blit(alien_image, alien_rect)

        for i in range(len(bases)):
            if bases[i][2] == True:
                for j in range(0, len(hostages[i]), 2):
                    hostages[i][j][1].left = bases[i][1].left
                    hostages[i][j + 1][1].left = hostages[i][j][1].left

                screen.blit(bases[i][0], bases[i][1])

            else:
                for j in range(0, len(hostages[i]), 2):
                    if hostages[i][j][2] == True:
                        if (chop.get_left() - 5 < hostages[i][j][1].left < chop.get_left() + 5) and chop.is_grounded() == 1: # Récupération
                            hostages[i][j][2] = False

                            print("Otage ramassé")
                            inside += 1
            
                        elif chop.get_collid().colliderect(hostages[i][j][1]) and chop.is_grounded() == 0:
                            hostages[i][j][2] = None
                            hostages_number -= 1                            
                            
                            hostages[i][j][1].top = 0 - 250
                            hostages[i][j + 1][1].top = 0 - 250

                            print("Un otage a succombé")

                        else:
                            temp = 0

                            if chop.is_grounded() == 1 and chop.get_left() < hostages[i][j][1].left:
                                temp = -2

                            elif chop.is_grounded() == 1 and chop.get_left() > hostages[i][j][1].left:
                                temp = 2

                            else:
                                temp = random.choice([-3, -1, 0, 1, 3])

                            hostages[i][j][1].left += temp
                            hostages[i][j + 1][1].left += temp
                            screen.blit(hostages[i][j][0], hostages[i][j][1]) if temp >= 0 else screen.blit(hostages[i][j + 1][0], hostages[i][j + 1][1])

                    elif hostages[i][j][2] == False:
                        if based == 1:
                            hostages[i][j][2] = None
                            hostages_number -= 1

                            hostages[i][j][1].top = 0 - 250
                            hostages[i][j + 1][1].top = 0 - 250

                            print("Otage secouru")
                            rescued += 1
                            inside -= 1

                        else:
                            hostages[i][j][1].center = (chop.get_top(), chop.get_left())
                            hostages[i][j + 1][1].center = (chop.get_top(), chop.get_left())

        if 'r' in pews.get_moves():
            screen.blit(pews.parts[0][0], pews.parts[0][1])

        if 'd' in pews.get_moves():
            screen.blit(pews.parts[1][0], pews.parts[1][1])

        if 'l' in pews.get_moves():
            screen.blit(pews.parts[2][0], pews.parts[2][1])

        for elt in chop.get_parts():
            if elt[2] == True:
                screen.blit(elt[0], elt[1])

        # Fin du jeu 
        if hostages_number < 1:
            print("Aucun otage restant... \n")
            print(f"Ennemis éliminés : \n{base_destroyed} bases - {tank_destroyed} tanks - {jet_destroyed} jets - {alien_destroyed} aliens")
            print(f"{rescued} otages secourus sur {total_hostage}")
            running = False

        # flip() the display to put your work on screen
        py.display.flip()

        clock.tick(75) # limits FPS to 75

    py.quit()

if __name__ == "__main__":
    choplifter()