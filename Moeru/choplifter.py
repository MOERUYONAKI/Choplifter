import pygame as py
import time
import random

def add_asset(image_path : str): # Add an asset by an image - return an image and the image's rect
    try:
        image = py.image.load(image_path).convert_alpha()
        rect = image.get_rect()

        return image, rect
    
    except:
        print("Erreur de génération")
        return False, False

def choplifter(size : tuple = (1280, 720)):
    last_move = 'z'
    bg_move = 0
    lives = 3
    grounded = 1
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

    move_id = 0 # pew_rect
    move_id2 = 0 # pew2_rect

    # pygame setup
    py.init()

    start_timer = time.time()

    screen = py.display.set_mode(size)
    clock = py.time.Clock()
    running = True

    surface = py.display.get_surface()

    bg = py.image.load('Python scripts\\Choplifter\\assets\\background.png').convert_alpha()
    bg = py.transform.scale(bg, size)
    bg_rect = bg.get_rect()
    bg_rect.left += size[0]

    bg0 = py.image.load('Python scripts\\Choplifter\\assets\\background2.png').convert_alpha()
    bg0 = py.transform.scale(bg0, size)
    bg0_rect = bg0.get_rect()

    bg2 = py.image.load('Python scripts\\Choplifter\\assets\\background2.png').convert_alpha()
    bg2 = py.transform.scale(bg2, size)
    bg2_rect = bg2.get_rect()
    bg2_rect.left = bg_rect.left + size[0]

    helibase_image = py.image.load('Python scripts\\Choplifter\\assets\\heli_base.png').convert_alpha()
    helibase_image = py.transform.scale(helibase_image, (186, 256))
    helibase_rect = helibase_image.get_rect()
    helibase_rect.top = size[1] - (helibase_rect.height)
    helibase_rect.left = int(round(0.4 * bg0_rect.width, 0)) - helibase_rect.width

    heliport_image = py.image.load('Python scripts\\Choplifter\\assets\\heliport.png').convert_alpha()
    heliport_image = py.transform.scale(heliport_image, (128, 45))
    heliport_rect = heliport_image.get_rect()
    heliport_rect.top = size[1] - heliport_rect.height - 8
    heliport_rect.left = int(round(0.4 * bg0_rect.width, 0))

    cms_font = py.font.Font('C:\\Windows\\WinSxS\\amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404\\comicbd.ttf', 24)
    title = cms_font.render(f'CHOPLIFTER - {lives} lives', True, (0, 0, 0, 0))
    title_rect = title.get_rect()
    title_rect.center = (size[0] // 2, 12)

    chop_image, chop_rect = add_asset('Python scripts\\Choplifter\\assets\\helicopter.png')
    chop_rect.left = heliport_rect.left + int(round(0.5 * heliport_rect.width)) - int(round(0.5 * chop_rect.width))
    chop_rect.top = heliport_rect.top

    chop2_image, chop2_rect = add_asset('Python scripts\\Choplifter\\assets\\revert_helicopter.png')
    chop2_rect.top = chop_rect.top
    chop2_rect.center = heliport_rect.center

    chop3_image, chop3_rect = add_asset('Python scripts\\Choplifter\\assets\\helico_ball.png')
    chop3_rect.top = chop_rect.top
    chop3_rect.left = chop_rect.left + 16

    chop4_image, chop4_rect = add_asset('Python scripts\\Choplifter\\assets\\grounded_helicopter.png')
    chop4_rect.left = chop_rect.left + 16
    chop4_rect.top = chop_rect.top + 9

    tank_image, tank_rect = add_asset('Python scripts\\Choplifter\\assets\\tank.png')
    tank_rect.top = size[1] - 27
    tank_rect.left = bg_rect.left

    tank2_image, tank2_rect = add_asset('Python scripts\\Choplifter\\assets\\revert_tank.png')
    tank2_rect.top = size[1] - 27
    tank2_rect.left = bg2_rect.left + bg2_rect.width - tank_rect.width

    tank3_image, tank3_rect = add_asset('Python scripts\\Choplifter\\assets\\tank.png')
    tank3_rect.top = size[1] - 27
    tank3_rect.left = bg_rect.left

    tank4_image, tank4_rect = add_asset('Python scripts\\Choplifter\\assets\\revert_tank.png')
    tank4_rect.top = size[1] - 27
    tank4_rect.left = bg2_rect.left + bg2_rect.width - tank3_rect.width
    
    tank2_position = (2 * size[0] - tank_rect.width)

    jet_image, jet_rect = add_asset('Python scripts\\Choplifter\\assets\\jet.png')
    jet_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0)))
    jet_rect.left = jet_rect.width

    jet_position = bg0_rect.left - jet_rect.width

    jet2_image, jet2_rect = add_asset('Python scripts\\Choplifter\\assets\\revert_jet.png')
    jet2_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0)))
    jet2_rect.left = bg2_rect.left + bg2_rect.width 

    alien_image = py.image.load('Python scripts\\Choplifter\\assets\\saucer.png').convert_alpha()
    alien_image = py.transform.scale(alien_image, (42, 38))
    alien_rect = alien_image.get_rect()
    alien_rect.top = bg_rect.top - alien_rect.height

    for i in range(bases_numbers):
        # Création des bases
        bases.append([py.image.load('Python scripts\\Choplifter\\assets\\basement.png').convert_alpha()])
        bases[i][0] = py.transform.scale(bases[i][0], (81, 60))
        bases[i].append(bases[i][0].get_rect())
        bases[i].append(True)
        bases[i][1].top = size[1] - 57
        rdm_left = random.randint(size[0] + 100 + int(round((2 * size[0] / bases_numbers) * (i), 0)), int(round((2 * size[0] / bases_numbers) * (i + 1), 0)) + size[0] - 100)
        bases[i][1].left = rdm_left
        bases_lefts.append(rdm_left)

        # Création des otages
        hostages.append([])
        for j in range(0, random.randint(4, 10), 2):
            hostages_number += 1
            total_hostage += 1

            hostages[i].append([py.image.load('Python scripts\\Choplifter\\assets\\hostage.png').convert_alpha()])
            hostages[i].append([py.image.load('Python scripts\\Choplifter\\assets\\revert_hostage.png').convert_alpha()])

            hostages[i][j][0] = py.transform.scale(hostages[i][j][0], (9, 18))
            hostages[i][j].append(hostages[i][j][0].get_rect())
            hostages[i][j].append(True)

            hostages[i][j + 1][0] = py.transform.scale(hostages[i][j + 1][0], (9, 18))
            hostages[i][j + 1].append(hostages[i][j + 1][0].get_rect())

            hostages[i][j][1].top = (size[1] - hostages[i][j][1].height) + 1
            hostages[i][j + 1][1].top = hostages[i][j][1].top
            hostages[i][j][1].left = bases[i][1].left
            hostages[i][j + 1][1].left = hostages[i][j][1].left

    pew_image, pew_rect = add_asset('Python scripts\\Choplifter\\assets\\green_pewpew.png')
    pew_rect.left = chop_rect.left + 32
    pew_rect.top = chop_rect.top + 16

    pew2_image, pew2_rect = add_asset('Python scripts\\Choplifter\\assets\\green_pewpew2.png')
    pew2_rect.left = chop_rect.left + 26
    pew2_rect.top = chop_rect.top + 12

    pew3_image, pew3_rect = add_asset('Python scripts\\Choplifter\\assets\\green_revert_pewpew.png')
    pew3_rect.left = chop_rect.left + 32
    pew3_rect.top = chop_rect.top + 16

    while running:
        # poll for events
        pressed = py.key.get_pressed()
        bg_move = 0

        if pressed[py.K_z]: # - Haut
            grounded = 0
            based = 0

            chop_rect.top -= 5
            chop2_rect.top -= 5
            chop3_rect.top -= 5
            chop4_rect.top -= 5

            if move_id != 1:
                pew_rect.top -= 5

            if move_id != 2:
                pew3_rect.top -= 5

            if move_id2 == 0:
                pew2_rect.top -= 5

            if chop_rect.top < 0:
                chop_rect.top = 0
                chop2_rect.top = 0
                chop3_rect.top = 0
                chop4_rect.top = 9

                if move_id == 0:
                    pew_rect.top = chop_rect.top + 16
                    pew3_rect.top = chop_rect.top + 16

                if move_id2 == 0:
                    pew2_rect.top = chop_rect.top + 12

            last_move = 'z'

        if pressed[py.K_s] and grounded == 0: # - Bas
            chop_rect.top += 5
            chop2_rect.top += 5
            chop3_rect.top += 5
            chop4_rect.top += 5

            if move_id != 1:
                pew_rect.top += 5

            if move_id != 2:
                pew3_rect.top += 5

            if move_id2 == 0:
                pew2_rect.top = pew2_rect.top + 5

            if chop_rect.top > size[1] - 32:
                grounded = 1

                chop_rect.top = size[1] - 32
                chop2_rect.top = size[1] - 32
                chop3_rect.top = size[1] - 32
                chop4_rect.top = size[1] - 21

                if move_id == 0:
                    pew_rect.top = chop_rect.top + 16
                    pew3_rect.top = chop_rect.top + 16

                if move_id2 == 0:
                    pew2_rect.top = chop_rect.top + 12

            last_move = 's'

        if pressed[py.K_q] and grounded == 0: # - Gauche  
            if chop_rect.left < int(round(0.3 * size[0], 0)) and bg0_rect.left < 0:
                bg_move = 2

                if bg0_rect.left <= 5:
                    bg_rect.left += 5
                    bg0_rect.left += 5
                    bg2_rect.left += 5
                    for base in bases:
                        base[1].left += 5

                else:
                    bg_rect.left -= bg0_rect.left
                    bg2_rect.left -= bg0_rect.left
                    for base in bases:
                        base[1].left -= bg2_rect.left
                    bg0_rect.left = 0

            else:
                chop_rect.left -= 5
                chop2_rect.left -= 5
                chop3_rect.left -= 5
                chop4_rect.left -= 5

                if move_id != 1:
                    pew_rect.left -= 5

                if move_id != 2:
                    pew3_rect.left -= 5

                if move_id2 == 0:
                    pew2_rect.left = pew2_rect.left - 5

                if chop_rect.left < 0:
                    chop_rect.left = 0
                    chop2_rect.left = 0
                    chop3_rect.left = 16
                    chop4_rect.left = 16

                    if move_id == 0:
                        pew_rect.left = chop_rect.left + 32
                        pew3_rect.left = chop_rect.left + 32

                    if move_id2 == 0:
                        pew2_rect.left = chop_rect.left + 36

            last_move = 'q'

        if pressed[py.K_d] and grounded == 0: # - Droite
            if chop_rect.left > (size[0] - int(round(0.3 * size[0], 0))) and bg2_rect.left > 0:
                bg_move = 1

                if bg2_rect.left >= 5:
                    bg_rect.left -= 5
                    bg0_rect.left -= 5
                    bg2_rect.left -= 5
                    for base in bases:
                        base[1].left -= 5

                else:
                    bg_rect.left -= bg2_rect.left
                    bg0_rect.left -= bg2_rect.left
                    for base in bases:
                        base[1].left -= bg2_rect.left
                    bg2_rect.left = 0  
            
            else:
                chop_rect.left += 5
                chop2_rect.left += 5
                chop3_rect.left += 5
                chop4_rect.left += 5

                if move_id != 1:
                    pew_rect.left += 5

                if move_id != 2:
                    pew3_rect.left += 5

                if move_id2 == 0:
                    pew2_rect.left = pew2_rect.left + 5

                if chop_rect.left > size[0] - 64:
                    chop_rect.left = size[0] - 64
                    chop2_rect.left = size[0] - 64
                    chop3_rect.left = size[0] - 49
                    chop4_rect.left = size[0] - 49

                    if move_id == 0:
                        pew_rect.left = chop_rect.left + 32
                        pew3_rect.left = chop_rect.left + 32

                    if move_id2 == 0:
                        pew2_rect.left = chop_rect.left + 36

            last_move = 'd'

        for event in py.event.get():
            if event.type == py.QUIT:
                print(f"\nEnnemis éliminés : \n{base_destroyed} bases - {tank_destroyed} tanks - {jet_destroyed} jets - {alien_destroyed} aliens")
                print(f"{rescued} otages secourus")
                running = False # end of the loop

            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE: # Tir bas
                    if move_id2 == 0 and grounded == 0:
                        down_shot_start = time.time()
                        move_id2 = 1
                        print("L'utilisateur tir !")

                if event.key == py.K_z: # Haut
                    print("L'utilisateur se déplace sur le haut !")

                if event.key == py.K_q: # Gauche
                    print("L'utilisateur se déplace sur la gauche !")

                if event.key == py.K_s: # Bas
                    print("L'utilisateur se déplace sur le bas !")

                if event.key == py.K_d: # Droite
                    print("L'utilisateur se déplace sur la droite !")

            if event.type == py.MOUSEBUTTONDOWN:
                if move_id == 0 and event.button == 1: # 1 - Click gauche
                    if last_move == 'd':
                        move_id = 1
                        basic_shot_start = time.time()
                        print("L'utilisateur tir !")

                    elif last_move == 'q':
                        move_id = 2
                        basic_shot_start = time.time()
                        print("L'utilisateur tir !")

                    else:
                        print("Impossible de tirer !")

        # RENDER YOUR GAME HERE
        if move_id != 0:
            if move_id == 1: # mouvement du tir (droite)
                if bg_move == 1: # Mouvement vers la droite
                    pew_rect.left += 5

                elif bg_move == 2: # Mouvement vers la gauche
                    pew_rect.left += 15
                
                else:
                    pew_rect.left += 10

                if (time.time() - basic_shot_start) > 1.75:
                    move_id = 0
                    pew_rect.left = chop_rect.left + 32
                    pew_rect.top = chop_rect.top + 16
                    print("Le tir est de nouveau prêt !")

            if move_id == 2: # mouvement du tir (gauche)
                if pew3_rect.left >= bg0_rect.left - 5:
                    if bg_move == 2: # Mouvement vers la gauche
                        pew3_rect.left -= 5

                    elif bg_move == 1: # Mouvement vers la droite
                        pew3_rect.left -= 15
                    
                    else:
                        pew3_rect.left -= 10

                elif pew3_rect.left > bg_rect.left - 18:
                    pew3_rect.left = bg_rect.left - 18

                if (time.time() - basic_shot_start) > 1.75:
                    move_id = 0
                    pew3_rect.left = chop_rect.left + 32
                    pew3_rect.top = chop_rect.top + 16
                    print("Le tir est de nouveau prêt !")

        if move_id2 != 0:
            if move_id2 == 1: # mouvement du tir (bas)
                if bg_move == 1: # Mouvement vers la droite
                    pew2_rect.left -= 5

                elif bg_move == 2: # Mouvement vers la gauche
                    pew2_rect.left += 5
                
                pew2_rect.top = pew2_rect.top + 8

                if pew2_rect.top >= size[1]:
                    move_id2 = 0
                    pew2_rect.left = chop_rect.left + 26
                    pew2_rect.top = chop_rect.top + 12
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

            if jet_rect.top > chop_rect.top:
                jet_rect.top -= random.choice([0, 1, 3])

            elif jet_rect.top < chop_rect.top:
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

            if jet2_rect.top > chop_rect.top:
                jet2_rect.top -= random.choice([0, 1, 3])

            elif jet2_rect.top < chop_rect.top:
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
            alien_rect.left = random.randint(int(round(0.75 * chop_rect.left, 0)), int(round(1.2 * chop_rect.left, 0)))
        
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
        if chop_rect.colliderect(tank_rect) or chop_rect.colliderect(tank2_rect) or chop_rect.colliderect(tank3_rect) or chop_rect.colliderect(tank4_rect) or chop_rect.colliderect(jet_rect) or chop_rect.colliderect(jet2_rect) or chop_rect.colliderect(alien_rect):
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

                chop_rect.left = heliport_rect.left + int(round(0.5 * heliport_rect.width)) - int(round(0.5 * chop_rect.width))
                chop_rect.top = heliport_rect.top

                chop2_rect.top = chop_rect.top
                chop2_rect.center = heliport_rect.center

                chop3_rect.top = chop_rect.top
                chop3_rect.left = chop_rect.left + 16

                chop4_rect.left = chop_rect.left + 16
                chop4_rect.top = chop_rect.top + 9

                tank_rect.left = bg_rect.left
                tank2_rect.left = bg2_rect.left + bg2_rect.width - tank_rect.width
                tank3_rect.left = bg_rect.left
                tank4_rect.left = bg2_rect.left + bg2_rect.width - tank3_rect.width

                for k in range(len(bases)):
                    bases[k][1].left = bases_lefts[k]

        if chop_rect.colliderect(heliport_rect) and last_move == 's': # Atterrissage
            grounded = 1
            based = 1

            chop_rect.left = heliport_rect.left + int(round(0.5 * heliport_rect.width)) - int(round(0.5 * chop_rect.width))
            chop_rect.top = heliport_rect.top

            chop2_rect.top = chop_rect.top
            chop2_rect.center = heliport_rect.center

            chop3_rect.top = chop_rect.top
            chop3_rect.left = chop_rect.left + 16
            
            chop4_rect.left = chop_rect.left + 16
            chop4_rect.top = chop_rect.top + 9

        if pew_rect.colliderect(tank_rect) or pew2_rect.colliderect(tank_rect) or pew3_rect.colliderect(tank_rect):
            tank_position = 2 * size[0] - tank_rect.width
            tank_move = 1
            tank_rect.left = bg_rect.left
            tank2_rect.left =  bg2_rect.left + bg2_rect.width - tank2_rect.width

            print("Tank détruit !")
            tank_destroyed += 1

        if pew_rect.colliderect(tank2_rect) or pew2_rect.colliderect(tank2_rect) or pew3_rect.colliderect(tank2_rect):
            tank_position = 0
            tank_move = 0
            tank_rect.left = bg_rect.left
            tank2_rect.left = bg2_rect.left + bg2_rect.width - tank2_rect.width

            print("Tank détruit !")
            tank_destroyed += 1

        if pew_rect.colliderect(tank3_rect) or pew2_rect.colliderect(tank3_rect) or pew3_rect.colliderect(tank3_rect):
            tank2_position = 2 * size[0] - tank3_rect.width
            tank2_move = 1
            tank3_rect.left = bg_rect.left
            tank4_rect.left =  bg2_rect.left + bg2_rect.width - tank4_rect.width

            print("Tank détruit !")
            tank_destroyed += 1

        if pew_rect.colliderect(tank4_rect) or pew2_rect.colliderect(tank4_rect) or pew3_rect.colliderect(tank4_rect):
            tank2_position = 0
            tank2_move = 0
            tank3_rect.left = bg_rect.left
            tank4_rect.left =  bg2_rect.left + bg2_rect.width - tank4_rect.width

            print("Tank détruit !")
            tank_destroyed += 1

        if pew_rect.colliderect(jet_rect) or pew2_rect.colliderect(jet_rect) or pew3_rect.colliderect(jet_rect):
            jet_position = bg2_rect.left + bg2_rect.width 
            jet_move = 1
            jet_rect.left = bg0_rect.left - jet_rect.width
            jet2_rect.left = bg2_rect.left + bg2_rect.width 

            print("Jet détruit !")
            jet_destroyed += 1

        if pew_rect.colliderect(jet2_rect) or pew2_rect.colliderect(jet2_rect) or pew3_rect.colliderect(jet2_rect):
            jet_position = 0 - jet_rect.width
            jet_move = 0
            jet_rect.left = bg0_rect.left - jet_rect.width
            jet2_rect.left = bg2_rect.left + bg2_rect.width 

            print("Jet détruit !")
            jet_destroyed += 1

        if pew_rect.colliderect(alien_rect) or pew2_rect.colliderect(alien_rect) or pew3_rect.colliderect(alien_rect):
            alien_move = 0
            alien_rect.top = bg_rect.top - alien_rect.height

            print("Alien éliminé !")
            alien_destroyed += 1

        for base in bases:
            if pew_rect.colliderect(base[1]) or pew2_rect.colliderect(base[1]) or pew3_rect.colliderect(base[1]):
                base[1].top = 0 - 250
                base[2] = False

                print("Bâtiment détruit !")
                base_destroyed += 1

            elif chop_rect.colliderect(base[1]):
                if lives == 1:
                    print("Hélicoptère détruit...")
                    print(f"Ennemis éliminés : \n{base_destroyed} bases - {tank_destroyed} tanks - {jet_destroyed} jets - {alien_destroyed} aliens")
                    print(f"{rescued} otages secourus")
                    running = False

                else:
                    print("Hélicoptère détruit... \n")
                    lives -= 1

                    bg0_rect.left = 0
                    bg_rect.left = size[0]
                    bg2_rect.left = bg_rect.left + size[0]

                    helibase_rect.top = size[1] - (helibase_rect.height)
                    helibase_rect.left = int(round(0.4 * bg0_rect.width, 0)) - helibase_rect.width

                    heliport_rect.top = size[1] - heliport_rect.height - 8
                    heliport_rect.left = int(round(0.4 * bg0_rect.width, 0))

                    chop_rect.left = heliport_rect.left + int(round(0.5 * heliport_rect.width)) - int(round(0.5 * chop_rect.width))
                    chop_rect.top = heliport_rect.top

                    chop2_rect.top = chop_rect.top
                    chop2_rect.center = heliport_rect.center

                    chop3_rect.top = chop_rect.top
                    chop3_rect.left = chop_rect.left + 16

                    chop4_rect.left = chop_rect.left + 16
                    chop4_rect.top = chop_rect.top + 9

                    tank_rect.left = bg_rect.left
                    tank2_rect.left = bg2_rect.left + bg2_rect.width - tank_rect.width
                    tank3_rect.left = bg_rect.left
                    tank4_rect.left = bg2_rect.left + bg2_rect.width - tank3_rect.width

                    for k in range(len(bases)):
                        bases[k][1].left = bases_lefts[k]


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("lavender")
        screen.blit(bg, bg_rect)
        screen.blit(bg0, bg0_rect)
        screen.blit(bg2, bg2_rect)

        # Texts
        title = cms_font.render(f'CHOPLIFTER - {lives} lives', True, (0, 0, 0, 0))
        screen.blit(title, title_rect)

        # Assets
        helibase_rect.top = size[1] - (helibase_rect.height)
        helibase_rect.left = bg0_rect.left + int(round(0.4 * bg0_rect.width, 0)) - helibase_rect.width
        screen.blit(helibase_image, helibase_rect)

        heliport_rect.top = size[1] - heliport_rect.height - 8
        heliport_rect.left = bg0_rect.left + int(round(0.4 * bg0_rect.width, 0))
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
                        if (chop4_rect.left - 5 < hostages[i][j][1].left < chop4_rect.left + 5) and grounded == 1: # Récupération
                            hostages[i][j][2] = False

                            print("Otage ramassé")
                            inside += 1
            
                        elif chop4_rect.colliderect(hostages[i][j][1]) and grounded == 0:
                            hostages[i][j][2] = None
                            hostages_number -= 1                            
                            
                            hostages[i][j][1].top = 0 - 250
                            hostages[i][j + 1][1].top = 0 - 250

                            print("Un otage a succombé")

                        else:
                            temp = 0

                            if grounded == 1 and chop_rect.left < hostages[i][j][1].left:
                                temp = -2

                            elif grounded == 1 and chop_rect.left > hostages[i][j][1].left:
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
                            hostages[i][j][1].center = chop4_rect.center
                            hostages[i][j + 1][1].center = chop4_rect.center

        if move_id == 1:
            screen.blit(pew_image, pew_rect)

        if move_id == 2:
            screen.blit(pew3_image, pew3_rect)

        if move_id2:
            screen.blit(pew2_image, pew2_rect)

        if grounded != 0:
            screen.blit(chop4_image, chop4_rect)

        else:
            if last_move == 'd':
                screen.blit(chop_image, chop_rect)

            elif last_move == 'q':
                screen.blit(chop2_image, chop2_rect)

            else:
                screen.blit(chop3_image, chop3_rect)

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