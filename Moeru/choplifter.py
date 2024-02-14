import pygame as py
import time
import random

def choplifter(size : tuple = (1280, 720)):
    last_move = 'z'
    bg_move = 0

    tank_position = 0 - 72
    tank_move = 0
    tank_destroyed = 0

    jet_position = 0 - 32
    jet_move = 0
    jet_destroyed = 0

    bases_numbers = random.randint(2, 3)
    bases = []
    base_destroyed = 0

    move_id = 0 # pew_rect
    move_id2 = 0 # pew2_rect

    # pygame setup
    py.init()

    start_timer = time.time()

    screen = py.display.set_mode(size)
    clock = py.time.Clock()
    running = True

    surface = py.display.get_surface()

    bg = py.image.load('C:\\Users\\1bbor\\Pictures\\Choplifters\\49c21344-36b4-4a8b-b73b-31e28d0d5fba.webp').convert_alpha()
    bg = py.transform.scale(bg, size)
    bg_rect = bg.get_rect()

    bg2 = py.image.load('C:\\Users\\1bbor\\Pictures\\Choplifters\\49c21344-36b4-4a8b-b73b-31e28d0d5fba.webp').convert_alpha()
    bg2 = py.transform.scale(bg, size)
    bg2_rect = bg2.get_rect()
    bg2_rect.left = size[0]

    cms_font = py.font.Font('C:\\Windows\\WinSxS\\amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404\\comicbd.ttf', 24)
    title = cms_font.render(f'CHOPLIFTER', True, (0, 0, 0, 0))
    title_rect = title.get_rect()
    title_rect.center = (size[0] // 2, 12)

    chop_image = py.image.load('Python scripts\\Choplifter\\assets\\helicopter.png').convert_alpha()
    chop_rect = chop_image.get_rect()

    chop2_image = py.image.load('Python scripts\\Choplifter\\assets\\revert_helicopter.png').convert_alpha()
    chop2_rect = chop2_image.get_rect()

    tank_image = py.image.load('Python scripts\\Choplifter\\assets\\tank.png').convert_alpha()
    tank_rect = tank_image.get_rect()
    tank_rect.top = size[1] - 27

    tank2_image = py.image.load('Python scripts\\Choplifter\\assets\\revert_tank.png').convert_alpha()
    tank2_rect = tank2_image.get_rect()
    tank2_rect.top = size[1] - 27
    tank2_rect.left = size[0] + 12

    jet_image = py.image.load('Python scripts\\Choplifter\\assets\\jet.png').convert_alpha()
    jet_rect = jet_image.get_rect()
    jet_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0)))
    jet_rect.left = 0 - 72

    jet2_image = py.image.load('Python scripts\\Choplifter\\assets\\revert_jet.png').convert_alpha()
    jet2_rect = jet2_image.get_rect()
    jet2_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0)))
    jet2_rect.left = size[0] + 32

    for i in range(bases_numbers):
        bases.append([py.image.load('Python scripts\\Choplifter\\assets\\basement.png').convert_alpha()])
        bases[i][0] = py.transform.scale(bases[i][0], (81, 60))
        bases[i].append(bases[i][0].get_rect())
        bases[i][1].top = size[1] - 57
        bases[i][1].left = random.randint(100 + int(round((2 * size[0] / bases_numbers) * (i), 0)), int(round((2 * size[0] / bases_numbers) * (i + 1), 0)) - 100)

    pew_image = py.image.load('Python scripts\\Choplifter\\assets\\green_pewpew.png').convert_alpha()
    pew_rect = pew_image.get_rect()

    pew_rect.left = chop_rect.left + 32
    pew_rect.top = chop_rect.top + 16

    pew2_image = py.image.load('Python scripts\\Choplifter\\assets\\green_pewpew2.png').convert_alpha()
    pew2_rect = pew2_image.get_rect()

    pew2_rect.left = chop_rect.left + 36
    pew2_rect.top = chop_rect.top + 12

    pew3_image = py.image.load('Python scripts\\Choplifter\\assets\\green_revert_pewpew.png').convert_alpha()
    pew3_rect = pew3_image.get_rect()

    pew3_rect.left = chop_rect.left + 32
    pew3_rect.top = chop_rect.top + 16

    while running:
        # poll for events
        pressed = py.key.get_pressed()
        bg_move = 0

        if pressed[py.K_z]: # - Haut
            chop_rect.top -= 5
            chop2_rect.top -= 5

            if move_id != 1:
                pew_rect.top -= 5

            if move_id != 2:
                pew3_rect.top -= 5

            if move_id2 == 0:
                pew2_rect.top -= 5

            if chop_rect.top < 0:
                chop_rect.top = 0
                chop2_rect.top = 0

                if move_id == 0:
                    pew_rect.top = chop_rect.top + 16
                    pew3_rect.top = chop_rect.top + 16

                if move_id2 == 0:
                    pew2_rect.top = chop_rect.top + 12

            last_move = 'z'

        if pressed[py.K_q]: # - Gauche  
            if chop_rect.left < int(round(0.3 * size[0], 0)) and bg_rect.left < 0:
                bg_move = 2

                if bg_rect.left <= 5:
                    bg_rect.left += 5
                    bg2_rect.left += 5
                    for base in bases:
                        base[1].left += 5

                else:
                    bg2_rect.left -= bg_rect.left
                    for base in bases:
                        base[1].left -= bg2_rect.left
                    bg_rect.left = 0

            else:
                chop_rect.left -= 5
                chop2_rect.left -= 5

                if move_id != 1:
                    pew_rect.left -= 5

                if move_id != 2:
                    pew3_rect.left -= 5

                if move_id2 == 0:
                    pew2_rect.left = pew2_rect.left - 5

                if chop_rect.left < 0:
                    chop_rect.left = 0
                    chop2_rect.left = 0

                    if move_id == 0:
                        pew_rect.left = chop_rect.left + 32
                        pew3_rect.left = chop_rect.left + 32

                    if move_id2 == 0:
                        pew2_rect.left = chop_rect.left + 36

            last_move = 'q'

        if pressed[py.K_s]: # - Bas
            chop_rect.top += 5
            chop2_rect.top += 5

            if move_id != 1:
                pew_rect.top += 5

            if move_id != 2:
                pew3_rect.top += 5

            if move_id2 == 0:
                pew2_rect.top = pew2_rect.top + 5

            if chop_rect.top > size[1] - 32:
                chop_rect.top = size[1] - 32
                chop2_rect.top = size[1] - 32

                if move_id == 0:
                    pew_rect.top = chop_rect.top + 16
                    pew3_rect.top = chop_rect.top + 16

                if move_id2 == 0:
                    pew2_rect.top = chop_rect.top + 12

            last_move = 's'

        if pressed[py.K_d]: # - Droite
            if chop_rect.left > (size[0] - int(round(0.3 * size[0], 0))) and bg2_rect.left > 0:
                bg_move = 1

                if bg2_rect.left >= 5:
                    bg_rect.left -= 5
                    bg2_rect.left -= 5
                    for base in bases:
                        base[1].left -= 5

                else:
                    bg_rect.left -= bg2_rect.left
                    for base in bases:
                        base[1].left -= bg2_rect.left
                    bg2_rect.left = 0  
            
            else:
                chop_rect.left += 5
                chop2_rect.left += 5

                if move_id != 1:
                    pew_rect.left += 5

                if move_id != 2:
                    pew3_rect.left += 5

                if move_id2 == 0:
                    pew2_rect.left = pew2_rect.left + 5

                if chop_rect.left > size[0] - 64:
                    chop_rect.left = size[0] - 64
                    chop2_rect.left = size[0] - 64

                    if move_id == 0:
                        pew_rect.left = chop_rect.left + 32
                        pew3_rect.left = chop_rect.left + 32

                    if move_id2 == 0:
                        pew2_rect.left = chop_rect.left + 36

            last_move = 'd'

        for event in py.event.get():
            if event.type == py.QUIT:
                print(f"Ennemis éliminés : \n{base_destroyed} bases - {tank_destroyed} tanks - {jet_destroyed} jets")
                running = False # end of the loop

            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE: # Tir bas
                    if move_id2 == 0:
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
                if pew3_rect.left >= bg_rect.left - 5:
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
                    pew2_rect.left = chop_rect.left + 36
                    pew2_rect.top = chop_rect.top + 12
                    print("Le tir est de nouveau prêt !")

        # Tanks moves
        if tank_position < (2 * size[0] + 72) and tank_move == 0:
            tank_position += 3

            if bg_move == 1: # Mouvement vers la droite
                tank_rect.left -= 2

            elif bg_move == 2: # Mouvement vers la gauche
                tank_rect.left += 8
            
            else:
                tank_rect.left += 3

        elif tank_position > 0 - 72:
            tank_move = 1
            tank_position -= 3
            
            if bg_move == 1: # Mouvement vers la droite
                tank2_rect.left -= 8

            elif bg_move == 2: # Mouvement vers la gauche
                tank2_rect.left += 2
            
            else:
                tank2_rect.left -= 3

        else:
            tank_position = 0 - 72
            tank_move = 0
            tank_rect.left = bg_rect.left - 72
            tank2_rect.left = bg2_rect.left + size[0] + 72

        # Jets moves
        if jet_position < (2 * size[0] + 32) and jet_move == 0:
            jet_position += 8

            if bg_move == 1: # Mouvement vers la droite
                jet_rect.left += 3

            elif bg_move == 2: # Mouvement vers la gauche
                jet_rect.left += 13
            
            else:
                jet_rect.left += 8

        elif jet_position > 0 - 72:
            jet_move = 1
            jet_position -= 8
            
            if bg_move == 1: # Mouvement vers la droite
                jet2_rect.left -= 13

            elif bg_move == 2: # Mouvement vers la gauche
                jet2_rect.left -= 3
            
            else:
                jet2_rect.left -= 8

        else:
            jet_position = 0 - 72
            jet_move = 0
            jet_rect.left = bg_rect.left - 72
            jet2_rect.left = bg2_rect.left + size[0] + 32
            jet_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0)))
            jet2_rect.top = random.randint(int(round(0.15 * size[1], 0)), int(round(0.85 * size[1], 0)))

        # Collision events
        if chop_rect.colliderect(tank_rect) or chop_rect.colliderect(tank2_rect) or chop_rect.colliderect(jet_rect) or chop_rect.colliderect(jet2_rect):
            print("Hélicoptère détruit... \n")
            print(f"Ennemis éliminés : \n{base_destroyed} bases - {tank_destroyed} tanks - {jet_destroyed} jets")
            running = False

        if pew_rect.colliderect(tank_rect) or pew2_rect.colliderect(tank_rect) or pew3_rect.colliderect(tank_rect):
            tank_position = bg2_rect.left + size[0] + 12
            tank_move = 1
            tank_rect.left = bg_rect.left - 72
            tank2_rect.left = bg2_rect.left + size[0] + 12

            print("Tank détruit !")
            tank_destroyed += 1

        if pew_rect.colliderect(tank2_rect) or pew2_rect.colliderect(tank2_rect) or pew3_rect.colliderect(tank_rect):
            tank_position = 0 - 72
            tank_move = 0
            tank_rect.left = bg_rect.left - 72
            tank2_rect.left = bg2_rect.left + size[0] + 12

            print("Tank détruit !")
            tank_destroyed += 1

        if pew_rect.colliderect(jet_rect) or pew2_rect.colliderect(jet_rect) or pew3_rect.colliderect(tank_rect):
            jet_position = bg2_rect.left + size[0] + 32
            jet_move = 1
            jet_rect.left = bg_rect.left - 72
            jet2_rect.left = bg2_rect.left + size[0] + 32

            print("Jet détruit !")
            jet_destroyed += 1

        if pew_rect.colliderect(jet2_rect) or pew2_rect.colliderect(jet2_rect) or pew3_rect.colliderect(tank_rect):
            jet_position = 0 - 72
            jet_move = 0
            jet_rect.left = bg_rect.left - 72
            jet2_rect.left = bg2_rect.left + size[0] + 72

            print("Jet détruit !")
            jet_destroyed += 1

        for base in bases:
            if pew_rect.colliderect(base[1]) or pew2_rect.colliderect(base[1]) or pew3_rect.colliderect(base[1]):
                base[1].top = 0 - 250

                print("Bâtiment détruit !")
                base_destroyed += 1

            elif chop_rect.colliderect(base[1]):
                print("Hélicoptère détruit... \n")
                print(f"Ennemis éliminés : \n{base_destroyed} bases - {tank_destroyed} tanks - {jet_destroyed} jets")
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("lavender")
        screen.blit(bg, bg_rect)
        screen.blit(bg2, bg2_rect)

        # Texts
        screen.blit(title, title_rect)

        # Assets
        screen.blit(tank_image, tank_rect)
        screen.blit(tank2_image, tank2_rect)
        screen.blit(jet_image, jet_rect)
        screen.blit(jet2_image, jet2_rect)

        for base in bases:
            screen.blit(base[0], base[1])

        if move_id == 1:
            screen.blit(pew_image, pew_rect)

        if move_id == 2:
            screen.blit(pew3_image, pew3_rect)

        if move_id2:
            screen.blit(pew2_image, pew2_rect)

        if last_move != 'q':
            screen.blit(chop_image, chop_rect)

        elif last_move == 'q':
            screen.blit(chop2_image, chop2_rect)

        # flip() the display to put your work on screen
        py.display.flip()

        clock.tick(75) # limits FPS to 75

    py.quit()

if __name__ == "__main__":
    choplifter()