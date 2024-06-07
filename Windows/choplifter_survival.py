# - - - - -  I M P O R T S  - - - - -

# - PY imports
import pygame as py
import time
import random

# - Choplifter imports
from init.asset import Vehicule, Music, add_asset
from init.background import Background_survival as Background
from init.chop import Chop, Pew as ChopPew
from init.tank import Tank, Pew as TankPew
from init.jet import Jet, Pew as JetPew
from init.alien import Alien, Pew as AlienPew


# - - - - -  F O N C T I O N S  - - - - -

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
        vehicule.get_parts()[0][1].left = bg.get_parts()[1][1].left + bg.get_parts()[1][1].width
        
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
def jet_moves(chop : Chop, jet : Jet, pews : JetPew, bg : Background, bg_move : int):
    shot_timer = 0

    if jet.get_position() < (2 * bg.size[0] + 2 * jet.get_parts()[0][1].width) and jet.get_move() == 0:
        jet.set_position(jet.get_position() + 8)
        move = random.choice([0, 1, 3])

        if jet.get_top() > chop.get_top():
            jet.move_top(0 - move)
            
            if not 'r' in pews.get_moves():
                pews.move_top(0 - move)

        elif jet.get_top() < chop.get_top():
            jet.move_top(move)

            if not 'r' in pews.get_moves():
                pews.move_top(move)

        else:
            if not pews.shot and (15 < chop.get_left() - jet.get_left() and 750 > chop.get_left() - jet.get_left()):
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
            
            if not 'l' in pews.get_moves():
                pews.move_top(0 - move)

        elif jet.get_top() < chop.get_top():
            jet.move_top(move)
            
            if not 'l' in pews.get_moves():
                pews.move_top(move)

        else:
            if not pews.shot and (15 < jet.get_left() - chop.get_left() and 750 > jet.get_left() - chop.get_left()):
                pews.shoot()
                shot_timer = time.time()
        
        if bg_move == 2: # Mouvement vers la droite
            jet.move_left(-3)

            if pews.parts[1][2]:
                pews.move_left(-7)

            else:
                pews.reset()

        elif bg_move == 1: # Mouvement vers la gauche
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
        
        if not 'r' in pews.get_moves() and not 'l' in pews.get_moves():
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
def end_message(tank_destroyed : int, jet_destroyed : int, alien_destroyed : int, score : int):
        print(f"\nEnnemis éliminés : \n{tank_destroyed} {'tanks' if tank_destroyed > 1 else 'tank'} - {jet_destroyed} {'jets' if jet_destroyed > 1 else 'jet'} - {alien_destroyed} {'aliens' if alien_destroyed > 1 else 'alien'}")
        print(f'Final score - {score}')


# - - - - -  M A I N  - - - - -

def choplifter_survival(size : tuple = (1280, 720), difficulty : int = 1):
    game = False
    
    bg_move = 0
    score = 0

    tank_destroyed = 0
    t1_shot_timer = 0
    t2_shot_timer = 0

    jet_destroyed = 0
    j1_shot_timer = 0
    j2_shot_timer = 0

    alien_destroyed = 0
    spawn_timer = 0
    ap_shot_timer = 0

    # pygame setup
    py.init()

    screen = py.display.set_mode(size)

    cms_font = py.font.Font('assets\\Fonts\\amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404\\comic.ttf', 24)
    
    loadtxt = cms_font.render(f'CHOPLIFTER - Loading...', True, (0, 0, 0, 0))
    loadtxt_rect = loadtxt.get_rect()
    loadtxt_rect.center = (size[0] // 2, size[1] - 25)
    
    screen.blit(loadtxt, loadtxt_rect)
    py.display.flip()
    
    clock = py.time.Clock()
    start_timer = None

    running = True

    music = Music("assets\\Songs\\Audiomachine - By the Hand of the Mortal.mp3", 0.2)
    music.play()

    # Menu assets
    image = py.image.load('assets\\menu_bg.jpg').convert_alpha()
    image = py.transform.scale(image, size)
    rect = image.get_rect()
    
    menu = (image, rect)

    choplifter_txt = add_asset('assets\\choplifter_txt.png') 
    choplifter_txt[1].center = (int(round(size[0] / 2, 0)), int(round(0.06 * size[1], 0)))

    play_txt = add_asset('assets\\play_txt.png') 
    play_txt[1].center = (int(round(size[0] / 2, 0)), int(round(size[1] / 2.15, 0)))

    quit_txt = add_asset('assets\\quit_txt.png') 
    quit_txt[1].center = (int(round(size[0] / 2, 0)), int(round(size[1] / 1.65, 0)))

    # Game assets
    bg = Background()

    chop = Chop(size)
    chop.active_up()
    chop.move_left(int(round(0.49 * size[0], 0)))
    chop.move_top(int(round(0.3 * size[1], 0)))
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

    title = cms_font.render(f'CHOPLIFTER - {score}', True, (0, 0, 0, 0))
    title_rect = title.get_rect()
    title_rect.center = (size[0] // 2, 12)

    tank1.set_center((bg.get_parts()[0][1].left + int(round(0.5 * tank1.get_parts()[0][1].width, 0)), int(round(0.8 * size[1], 0))))
    tank1.set_position(0)
    tank2.set_center((2 * size[0] - int(round(0.5 * tank2.get_parts()[0][1].width, 0)), int(round(0.8 * size[1], 0))))
    tank2.set_position(2 * size[0] - tank2.get_parts()[0][1].width)
    
    t1_pews.reset()
    t2_pews.reset()

    jet1.set_center((0 - int(round(0.5 * jet1.get_parts()[0][1].width, 0)), random.randint(int(round(0.3 * size[1], 0)), int(round(0.9 * size[1], 0)) - 48)))
    jet2.set_center((2 * size[0] + int(round(0.5 * jet2.get_parts()[0][1].width, 0)), random.randint(int(round(0.3 * size[1], 0)), int(round(0.9 * size[1], 0)) - 48)))
    jet2.set_position(2 * size[0] + jet2.get_parts()[0][1].width)

    j1_pews.reset()
    j2_pews.reset()

    alien.set_center((random.randint(int(round(0.35 * size[0], 0)), int(round(0.65 * size[0], 0))), bg.get_parts()[1][1].top - alien.get_collid().height))
    alien_pew.reset()

    while running:
        # poll for events
        pressed = py.key.get_pressed()

        if not game:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False # end of the loop

                if event.type == py.KEYDOWN:
                    if event.key == py.K_SPACE or event.key == py.K_ESCAPE:
                        start_timer = time.time()
                        music.set_volume(0.1)
                        py.mouse.set_visible(False)
                        game = True
                
                if event.type == py.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if choplifter_txt[1].collidepoint(py.mouse.get_pos()):
                            music.pause() if music.is_playing() else music.unpause()

                        elif play_txt[1].collidepoint(py.mouse.get_pos()):
                            start_timer = time.time()
                            music.set_volume(0.1)
                            py.mouse.set_visible(False)
                            game = True

                        elif quit_txt[1].collidepoint(py.mouse.get_pos()):
                            end_message(tank_destroyed, jet_destroyed, alien_destroyed, score)
                            running = False # end of the loop

                screen.blit(menu[0], menu[1])
                screen.blit(choplifter_txt[0], choplifter_txt[1])
                screen.blit(play_txt[0], play_txt[1])
                screen.blit(quit_txt[0], quit_txt[1])

        else:
            bg_move = 0

            # Gestion de la difficultée
            if int(round(time.time() - start_timer, 0)) > 300 and difficulty < 3: # Niveau 3 après 5 minutes
                difficulty = 3

            elif int(round(time.time() - start_timer, 0)) > 180 and difficulty < 2: # Niveau 2 après 3 minutes
                difficulty = 2

            if pressed[py.K_z]: # - Haut
                chop.active_up()
                chop.move_top(-5)

                if chop.get_top() < 0:
                    chop.move_top(0 - chop.get_top())

            if pressed[py.K_s] and chop.is_grounded() == 0: # - Bas
                chop.active_up()
                chop.move_top(5)

                if chop.get_top() >= int(round(0.764 * size[1], 0)):
                    chop.active_grounded()
                    chop.set_top(int(round(0.764 * size[1], 0)) + chop.get_collid().height)

            if pressed[py.K_q] and chop.is_grounded() == 0: # - Gauche  
                chop.active_left()

                if chop.get_left() < int(round(0.3 * size[0], 0)) and bg.get_position() > 0:
                    bg_move = 2

                    if bg.get_position() >= 5:
                        bg.move_left(5)

                    else:
                        bg.move_left(-1 * bg.get_left())

                else:
                    chop.move_left(-5)

                    if chop.get_left() < 0:
                        chop.move_left(0 - chop.get_left())

            if pressed[py.K_d] and chop.is_grounded() == 0: # - Droite
                chop.active_right()

                if chop.get_left() > (size[0] - int(round(0.3 * size[0], 0))) and bg.get_position() < size[0]:
                    bg_move = 1

                    if bg.get_position() <= size[0] - 5:
                        bg.move_left(-5)

                    else:
                        bg.move_left(0 - bg.get_right())
                
                else:
                    chop.move_left(5)

                    if chop.get_left() > size[0] - chop.get_collid().width:
                        chop.move_left(size[0] - chop.get_left() - chop.get_collid().width)

            for event in py.event.get():
                if event.type == py.QUIT:
                    end_message(tank_destroyed, jet_destroyed, alien_destroyed, score)
                    running = False # end of the loop

                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        music.set_volume(0.2)
                        py.mouse.set_visible(True)
                        game = False 

                    if event.key == py.K_SPACE: # Tir bas
                        if 'd' not in pews.get_moves() and chop.is_grounded() == 0:
                            pews.parts[1][2] = True
                            print("L'utilisateur tir !")

                        else:
                            print("Impossible de larguer le drop !")

                    # - Game logs
                    if event.key == py.K_z: # Haut
                        print("L'utilisateur se déplace sur le haut !")

                    if event.key == py.K_q: # Gauche
                        print("L'utilisateur se déplace sur la gauche !")

                    if event.key == py.K_s: # Bas
                        print("L'utilisateur se déplace sur le bas !")

                    if event.key == py.K_d: # Droite
                        print("L'utilisateur se déplace sur la droite !")

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

            # - Game render
            if 'r' in pews.get_moves() or 'l' in pews.get_moves():
                if 'r' in pews.get_moves(): # mouvement du tir (droite)
                    if pews.parts[0][1].left <= bg.get_parts()[1][1].left - 5:
                        if bg_move == 1: # Mouvement vers la droite
                            pews.move_left_rs(5)

                        elif bg_move == 2: # Mouvement vers la gauche
                            pews.move_left_rs(15)
                        
                        else:
                            pews.move_left_rs(10)

                    elif pews.parts[0][1].left > bg.get_parts()[1][1].left + 24:
                        pews.parts[0][1].left = bg.get_parts()[1][1].left + 24

                    if (time.time() - basic_shot_start) > 1.5:
                        pews.reset_rs()
                        print("Le tir est de nouveau prêt !")

                elif 'l' in pews.get_moves(): # mouvement du tir (gauche)
                    if pews.parts[2][1].left >= bg.get_parts()[0][1].left - 5:
                        if bg_move == 2: # Mouvement vers la gauche
                            pews.move_left_ls(-5)

                        elif bg_move == 1: # Mouvement vers la droite
                            pews.move_left_ls(-15)
                        
                        else:
                            pews.move_left_ls(-10)

                    elif pews.parts[2][1].left > bg.get_parts()[1][1].left - 24:
                        pews.parts[2][1].left = bg.get_parts()[1][1].left - 24

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
                    print("Le drop est de nouveau prêt !")

            # Tanks moves
            if int(round(time.time() - start_timer, 0)) > 1: # arrivée après 1 secondes de jeu
                t1_shot_timer = tank_moves(chop, tank1, t1_pews, bg, bg_move)

            if int(round(time.time() - start_timer, 0)) > 12: # arrivée après 12 secondes de jeu
                t2_shot_timer = tank_moves(chop, tank2, t2_pews, bg, bg_move)

            if int(round(time.time() - t1_shot_timer, 0)) > 2 and t1_shot_timer != 0:
                t1_pews.reset()
                t1_shot_timer = 0

            if int(round(time.time() - t2_shot_timer, 0)) > 2 and t2_shot_timer != 0:
                t2_pews.reset()
                t2_shot_timer = 0

            # Jets moves
            if int(round(time.time() - start_timer, 0)) > 8: # arrivée après 8 secondes de jeu
                j1_shot_timer = jet_moves(chop, jet1, j1_pews, bg, bg_move)

            if int(round(time.time() - start_timer, 0)) > 24: # arrivée après 24 secondes de jeu
                j2_shot_timer = jet_moves(chop, jet2, j2_pews, bg, bg_move)

            if int(round(time.time() - j1_shot_timer, 0)) > 3 and j1_shot_timer != 0:
                j1_pews.reset()
                j1_shot_timer = 0

            if int(round(time.time() - j2_shot_timer, 0)) > 3 and j2_shot_timer != 0:
                j2_pews.reset()
                j2_shot_timer = 0

            # Aliens moves
            if int(round(time.time() - start_timer, 0) + 1) % 15 == 0 and int(round(time.time() - start_timer, 0) + 1) > 30 and alien.get_move() == 0: # Arrivée après 30 secondes de jeu / toute les 15 secondes
                spawn_timer = time.time()
                alien.set_move(1)
            
            if alien.get_move() != 0:
                if time.time() - spawn_timer >= 4 and spawn_timer != 0:
                    alien_pew.shoot()
                    ap_shot_timer = time.time()

                    alien.set_move(2)
                    spawn_timer = 0

                if ap_shot_timer == 0 or time.time() - ap_shot_timer > 1:
                    alien_moves(chop, alien, alien_pew, bg, bg_move)

            if time.time() - ap_shot_timer > 2 and ap_shot_timer != 0:
                alien_pew.reset()
                ap_shot_timer = 0

            # Collisions events
            elts = [tank1, tank2, jet1, jet2, t1_pews, t2_pews, j1_pews, j2_pews, alien, alien_pew]

            if chop_collid(chop, elts):
                print("Hélicoptère détruit...")
                end_message(tank_destroyed, jet_destroyed, alien_destroyed, score)
                running = False

            if cps_collid(tank1, pews, bg):
                tank1.set_position(2 * size[0] + tank1.get_parts()[0][1].width)
                tank1.set_move(1)
                
                tank1.active_left()
                tank1.set_center((3 * size[0] + tank1.get_parts()[0][1].width, int(round(0.8 * size[1], 0))))    
                t1_pews.reset()

                tank_destroyed += 1
                print("Tank détruit !")

                score += 30 * difficulty

            if cps_collid(tank2, pews, bg):
                tank2.set_position(2 * size[0] + tank2.get_parts()[0][1].width)
                tank2.set_move(1)
                
                tank2.active_left()
                tank2.set_center((2 * size[0] + tank2.get_parts()[0][1].width, int(round(0.8 * size[1], 0))))    
                t2_pews.reset()

                tank_destroyed += 1
                print("Tank détruit !")

                score += 30 * difficulty

            if cps_collid(jet1, pews, bg):
                jet2.set_position(bg.get_parts()[1][1].left + bg.get_parts()[1][1].width )
                jet2.set_move(1)
                jet_destroyed += 1

                print("Jet détruit !")

                score += 75 * difficulty

            if cps_collid(jet2, pews, bg):
                jet2.set_position(0 - jet1.get_parts()[0][1].width)
                jet2.set_move(0)
                jet_destroyed += 1
                
                print("Jet détruit !")

                score += 75 * difficulty

            if pews.get_rs_collid().colliderect(alien.get_collid()) or pews.get_drop_collid().colliderect(alien.get_collid()) or pews.get_ls_collid().colliderect(alien.get_collid()):
                alien.set_move(0)
                alien.set_center(random.randint(int(round(0.35 * size[0], 0), int(round(0.65 * size[0], 0)))), bg.get_parts()[1][1].top - alien.get_collid().height)
                alien_pew.reset()

                print("Alien éliminé !")
                alien_destroyed += 1

                score += 120 * difficulty

            # Background
            screen.fill("lavender")
            for elt in bg.get_parts():
                screen.blit(elt[0], elt[1])

            # Textes
            diff = 'easy'

            if difficulty == 2:
                diff = 'medium'

            elif difficulty == 3:
                diff = 'hard'

            title = cms_font.render(f'CHOPLIFTER - {score} ({diff})', True, (32, 32, 32, 0))
            screen.blit(title, title_rect)

            # Assets - tanks
            for elt in t1_pews.get_parts():
                if elt[2]:
                    screen.blit(elt[0], elt[1])

            for elt in t2_pews.get_parts():
                if elt[2]:
                    screen.blit(elt[0], elt[1])

            for elt in tank1.get_parts():
                if elt[2]:
                    screen.blit(elt[0], elt[1])
            
            for elt in tank2.get_parts():
                if elt[2]:
                    screen.blit(elt[0], elt[1])

            # Assets - jets
            for elt in j1_pews.get_parts():
                if elt[2]:
                    screen.blit(elt[0], elt[1])

            for elt in j2_pews.get_parts():
                if elt[2]:
                    screen.blit(elt[0], elt[1])

            for elt in jet1.get_parts():
                if elt[2]:
                    screen.blit(elt[0], elt[1])
            
            for elt in jet2.get_parts():
                if elt[2]:
                    screen.blit(elt[0], elt[1])

            # Assets - aliens
            if alien.get_move() != 0:
                screen.blit(alien.get_parts()[0][0], alien.get_parts()[0][1])

            if alien_pew.get_shot():
                alien_pew.move_top(12)
                screen.blit(alien_pew.get_parts()[0][0], alien_pew.get_parts()[0][1])

            # Assets - chop
            if 'r' in pews.get_moves():
                screen.blit(pews.parts[0][0], pews.parts[0][1])

            else:
                pews.reset_rs()

            if 'd' in pews.get_moves():
                screen.blit(pews.parts[1][0], pews.parts[1][1])
            
            else:
                pews.reset_drop()

            if 'l' in pews.get_moves():
                screen.blit(pews.parts[2][0], pews.parts[2][1])

            else:
                pews.reset_ls()

            for elt in chop.get_parts():
                if elt[2] == True:
                    screen.blit(elt[0], elt[1])

        # Affichage des modifications
        py.display.flip()

        if difficulty == 2:
            clock.tick(90)

        elif difficulty == 3:
            clock.tick(120)

        else: # Difficulté par défaut : facile
            clock.tick(75)

    music.stop()
    py.quit()

if __name__ == "__main__":
    choplifter_survival()