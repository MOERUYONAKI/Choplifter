import pygame as py
import time
import chopper

last_move = 'z'
size = (1280, 720)

tank_position = 0 - 72
tank_move = 0

bg_move = 0
move_id = 0 # pew_rect
move_id2 = 0 # pew2_rect

# pygame setup
py.init()

start_timer = time.time()

screen = py.display.set_mode((1280, 720))
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

tank_image = py.image.load('Python scripts\\Choplifter\\assets\\tank.png').convert_alpha()
tank_rect = tank_image.get_rect()
tank_rect.top = size[1] - 27

tank2_image = py.image.load('Python scripts\\Choplifter\\assets\\revert_tank.png').convert_alpha()
tank2_rect = tank2_image.get_rect()
tank2_rect.top = size[1] - 27
tank2_rect.left = size[0] + 12

pew_image = py.image.load('Python scripts\\Choplifter\\assets\\green_pewpew.png').convert_alpha()
pew_rect = pew_image.get_rect()

pew_rect.left = chop_rect.left + 32
pew_rect.top = chop_rect.top + 16

pew2_image = py.image.load('Python scripts\\Choplifter\\assets\\green_pewpew2.png').convert_alpha()
pew2_rect = pew2_image.get_rect()

pew2_rect.left = chop_rect.left + 36
pew2_rect.top = chop_rect.top + 12

while running:
    # poll for events
    pressed = py.key.get_pressed()
    bg_move = 0

    if pressed[py.K_z]: # - Haut
        chop_rect.top = chop_rect.top - 5

        if move_id == 0:
            pew_rect.top = pew_rect.top - 5

        if move_id2 == 0:
            pew2_rect.top = pew2_rect.top - 5

        if chop_rect.top < 0:
            chop_rect.top = 0

            if move_id == 0:
                pew_rect.top = chop_rect.top + 16

            if move_id2 == 0:
                pew2_rect.top = chop_rect.top + 12

        last_move = 'z'

    if pressed[py.K_q]: # - Gauche  
        if chop_rect.left < 336 and bg_rect.left < 0:
            bg_move = 2

            if bg_rect.left < 0:
                bg_rect.left += 5
                bg2_rect.left += 5

        else:
            chop_rect.left = chop_rect.left - 5

            if move_id == 0:
                pew_rect.left = pew_rect.left - 5

            if move_id2 == 0:
                pew2_rect.left = pew2_rect.left - 5

            if chop_rect.left < 0:
                chop_rect.left = 0

                if move_id == 0:
                    pew_rect.left = chop_rect.left + 32

                if move_id2 == 0:
                    pew2_rect.left = chop_rect.left + 36

        last_move = 'q'

    if pressed[py.K_s]: # - Bas
        chop_rect.top = chop_rect.top + 5

        if move_id == 0:
            pew_rect.top = pew_rect.top + 5

        if move_id2 == 0:
            pew2_rect.top = pew2_rect.top + 5

        if chop_rect.top > size[1] - 32:
            chop_rect.top = size[1] - 32

            if move_id == 0:
                pew_rect.top = chop_rect.top + 16

            if move_id2 == 0:
                pew2_rect.top = chop_rect.top + 12

        last_move = 's'

    if pressed[py.K_d]: # - Droite
        if chop_rect.left > size[0] - 400 and bg2_rect.left > 0:
            bg_move = 1

            if bg2_rect.left >= 5:
                bg_rect.left -= 5
                bg2_rect.left -= 5
        
        else:
            chop_rect.left = chop_rect.left + 5

            if move_id == 0:
                pew_rect.left = pew_rect.left + 5

            if move_id2 == 0:
                pew2_rect.left = pew2_rect.left + 5

            if chop_rect.left > size[0] - 64:
                chop_rect.left = size[0] - 64

                if move_id == 0:
                    pew_rect.left = chop_rect.left + 32

                if move_id2 == 0:
                    pew2_rect.left = chop_rect.left + 36

        last_move = 'd'

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False # end of the loop

        if event.type == py.KEYUP: 
            current_w = size[0]

            ''' - Mode "Plein écran" désactivé
            if event.key == py.K_f and not py.display.is_fullscreen(): # set fullscreen mode
                screen = py.display.set_mode((0, 0), py.FULLSCREEN)
                size = (py.display.Info().current_w, py.display.Info().current_h)

                bg = py.transform.scale(bg, size)
                bg2 = py.transform.scale(bg, size)
                bg2_rect.left = size[0] - (current_w - bg2_rect.left)
                  
                tank_rect.top = size[1] - 27
                tank2_rect.top = size[1] - 27

                title_rect.center = (size[0] // 2, 12)

            if event.key == py.K_ESCAPE and py.display.is_fullscreen(): # set window mode
                screen = py.display.set_mode((1280, 720))
                size = (py.display.Info().current_w, py.display.Info().current_h)

                bg = py.transform.scale(bg, size)
                bg2 = py.transform.scale(bg, size)
                bg2_rect.left = size[0] - (current_w - bg2_rect.left)

                tank_rect.top = size[1] - 27
                tank2_rect.top = size[1] - 27

                title_rect.center = (size[0] // 2, 12)
            '''

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
                basic_shot_start = time.time()
                move_id = 1
                print("L'utilisateur tir !")

    # RENDER YOUR GAME HERE
    if move_id != 0:
        if move_id == 1: # mouvement du tir (droite)
            pew_rect.left = pew_rect.left + 8

            if (time.time() - basic_shot_start) > 2:
                move_id = 0
                pew_rect.left = chop_rect.left + 32
                pew_rect.top = chop_rect.top + 16
                print("Le tir est de nouveau prêt !")

    if move_id2 != 0:
        if move_id2 == 1: # mouvement du tir (bas)
            pew2_rect.top = pew2_rect.top + 8

            if pew2_rect.top >= size[1] or ((time.time() - down_shot_start) > 3):
                move_id2 = 0
                pew2_rect.left = chop_rect.left + 36
                pew2_rect.top = chop_rect.top + 12
                print("Le tir est de nouveau prêt !")

    if tank_position < 2572 and tank_move == 0:
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
        tank2_rect.left = bg2_rect.left + size[0] + 12

    # Collision events
    if chop_rect.colliderect(tank_rect) or chop_rect.colliderect(tank2_rect):
        print("Hélicoptère détruit !")
        running = False

    if pew_rect.colliderect(tank_rect) or pew2_rect.colliderect(tank_rect):
        tank_position = bg2_rect.left + size[0] + 12
        tank_move = 1
        tank_rect.left = bg_rect.left - 72
        tank2_rect.left = bg2_rect.left + size[0] + 12
        print("Tank détruit !")

    if pew_rect.colliderect(tank2_rect) or pew2_rect.colliderect(tank2_rect):
        tank_position = 0 - 72
        tank_move = 0
        tank_rect.left = bg_rect.left - 72
        tank2_rect.left = bg2_rect.left + size[0] + 12
        print("Tank détruit !")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("lavender")
    screen.blit(bg, bg_rect)
    screen.blit(bg2, bg2_rect)

    # Texts
    screen.blit(title, title_rect)

    # Assets
    screen.blit(tank_image, tank_rect)
    screen.blit(tank2_image, tank2_rect)
    screen.blit(pew_image, pew_rect)
    screen.blit(pew2_image, pew2_rect)
    screen.blit(chop_image, chop_rect)

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(75) # limits FPS to 75

py.quit()