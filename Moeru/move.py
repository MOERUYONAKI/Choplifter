import pygame as py

move_id = 0

# pygame setup
py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

rect = py.Rect(0, 0, 5, 5)
shot = py.Rect(rect.left + 1, rect.top + 1, 3, 3)

surface = py.display.get_surface()

size = (1280, 720)

while running:
    # poll for events
    pressed = py.key.get_pressed()

    if pressed[py.K_z]: # - Haut
        rect.top = rect.top - 3

        if move_id == 0:
            shot.top = shot.top - 3

        if rect.top < 0:
            rect.top = 0

            if move_id == 0:
                shot.top = 1

        last_move = 'z'

    if pressed[py.K_q]: # - Gauche    
        rect.left = rect.left - 3

        if move_id == 0:
            shot.left = shot.left - 3

        if rect.left < 0:
            rect.left = 0

            if move_id == 0:
                shot.left = 1

        last_move = 'q'

    if pressed[py.K_s]: # - Bas
        rect.top = rect.top + 3

        if move_id == 0:
            shot.top = shot.top + 3

        if rect.top > size[1] - 5:
            rect.top = size[1] - 5

            if move_id == 0:
                shot.top = size[1] - 6

        last_move = 's'

    if pressed[py.K_d]: # - Droite
        rect.left = rect.left + 3

        if move_id == 0:
            shot.left = shot.left + 3

        if rect.left > size[0] - 5:
            rect.left = size[0] - 5

            if move_id == 0:
                shot.top = size[0] - 6

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

        if event.type == py.KEYDOWN:
            if event.key == py.K_z: # Haut
                print("L'utilisateur se déplace sur le haut !")

            if event.key == py.K_q: # Gauche
                print("L'utilisateur se déplace sur la gauche !")

            if event.key == py.K_s: # Bas
                print("L'utilisateur se déplace sur le bas !")

            if event.key == py.K_d: # Droite
                print("L'utilisateur se déplace sur la droite !")

        if event.type == py.MOUSEBUTTONUP:
            if last_move == 'z' and move_id == 0:
                move_id = 1
                print("L'utilisateur tir !")

            elif last_move == 'q' and move_id == 0:
                move_id = 2
                print("L'utilisateur tir !")

            elif last_move == 's' and move_id == 0:
                move_id = 3
                print("L'utilisateur tir !")

            elif last_move == 'd' and move_id == 0:
                move_id = 4
                print("L'utilisateur tir !")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    if move_id !=0:
        if move_id == 1: # mouvement du tir (haut)
            shot.top = shot.top - 5

            if shot.top <= 0:
                move_id = 0
                shot.left = rect.left + 1
                shot.top = rect.top + 1
                print("Le tir est de nouveau prêt !")
        
        if move_id == 2: # mouvement du tir (gauche)
            shot.left = shot.left - 5

            if shot.left <= 0:
                move_id = 0
                shot.left = rect.left + 1
                shot.top = rect.top + 1
                print("Le tir est de nouveau prêt !")

        if move_id == 3: # mouvement du tir (bas)
            shot.top = shot.top + 5

            if (shot.top >= size[1]):
                move_id = 0
                shot.left = rect.left + 1
                shot.top = rect.top + 1
                print("Le tir est de nouveau prêt !")

        if move_id == 4: # mouvement du tir (droite)
            shot.left = shot.left + 5

            if (shot.left >= size[0]):
                move_id = 0
                shot.left = rect.left + 1
                shot.top = rect.top + 1
                print("Le tir est de nouveau prêt !")

    py.draw.rect(surface = surface, color = (255, 0, 0, 100), rect = rect)
    py.draw.rect(surface = surface, color = (255, 0, 0, 80), rect = shot)

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60) # limits FPS to 60

py.quit()