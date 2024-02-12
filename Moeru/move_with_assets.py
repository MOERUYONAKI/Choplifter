import pygame as py
import time
import chopper

last_move = 'z'
size = (1280, 720)

move_id = 0 # pew_rect
move_id2 = 0 # pew2_rect

# pygame setup
py.init()

screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

chop_image = py.image.load('Python scripts\\Choplifter\\assets\\helicopter.png').convert_alpha()
chop_rect = chop_image.get_rect()

pew_image = py.image.load('Python scripts\\Choplifter\\assets\\green_pewpew.png').convert_alpha()
pew_rect = pew_image.get_rect()

pew_rect.left = chop_rect.left + 32
pew_rect.top = chop_rect.top + 16

pew2_image = py.image.load('Python scripts\\Choplifter\\assets\\green_pewpew2.png').convert_alpha()
pew2_rect = pew2_image.get_rect()

pew2_rect.left = chop_rect.left + 36
pew2_rect.top = chop_rect.top + 12

surface = py.display.get_surface()

while running:
    # poll for events
    pressed = py.key.get_pressed()

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
            if event.key == py.K_f and not py.display.is_fullscreen(): # set fullscreen mode
                screen = py.display.set_mode((0, 0), py.FULLSCREEN)
                size = (py.display.Info().current_w, py.display.Info().current_h)

            if event.key == py.K_ESCAPE and py.display.is_fullscreen(): # set window mode
                screen = py.display.set_mode((1280, 720))
                size = (py.display.Info().current_w, py.display.Info().current_h)

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

        if event.type == py.MOUSEBUTTONUP:
            if move_id == 0:
                basic_shot_start = time.time()
                move_id = 1
                print("L'utilisateur tir !")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    if move_id != 0:
        if move_id == 1: # mouvement du tir (droite)
            pew_rect.left = pew_rect.left + 8

            if (pew_rect.left >= size[0]) or ((time.time() - basic_shot_start) > 2.5):
                move_id = 0
                pew_rect.left = chop_rect.left + 32
                pew_rect.top = chop_rect.top + 16
                print("Le tir est de nouveau prêt !")

    if move_id2 != 0:
        if move_id2 == 1: # mouvement du tir (bas)
            pew2_rect.top = pew2_rect.top + 8

            if pew2_rect.top >= size[1] or ((time.time() - down_shot_start) > 2.5):
                move_id2 = 0
                pew2_rect.left = chop_rect.left + 36
                pew2_rect.top = chop_rect.top + 12
                print("Le tir est de nouveau prêt !")

    screen.blit(pew_image, pew_rect)
    screen.blit(pew2_image, pew2_rect)
    screen.blit(chop_image, chop_rect)

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(75) # limits FPS to 75

py.quit()