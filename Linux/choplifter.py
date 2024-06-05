# - - - - -  I M P O R T S  - - - - -

# - PY imports
import pygame as py
import time
import random

# - Choplifter imports
from init.init import *
from init.asset import Vehicule, Music, add_asset


# - - - - -  M A I N  - - - - -

def choplifter(size : tuple = (1280, 720)):
    game = False

    bg_move = 0
    lives = 3
    based = 1

    tank_destroyed = 0
    t1_shot_timer = 0
    t2_shot_timer = 0

    jet_destroyed = 0
    j1_shot_timer = 0
    j2_shot_timer = 0

    alien_destroyed = 0
    spawn_timer = 0
    ap_shot_timer = 0

    bases_numbers = random.randint(2, 3)
    base_destroyed = 0
    
    inside = 0
    rescued = 0

    respawn_timer = -1

    # pygame setup
    py.init()

    screen = py.display.set_mode(size)

    cms_font = py.font.Font('Linux/assets/Fonts/amd64_microsoft-windows-f..ruetype-comicsansms_31bf3856ad364e35_10.0.22621.1_none_3deaef772e20c404/comic.ttf', 24)
    
    loadtxt = cms_font.render(f'CHOPLIFTER - Loading...', True, (0, 0, 0, 0))
    loadtxt_rect = loadtxt.get_rect()
    loadtxt_rect.center = (size[0] // 2, size[1] - 25)
    
    screen.blit(loadtxt, loadtxt_rect)
    py.display.flip()
    
    clock = py.time.Clock()
    start_timer = None

    running = True

    music = Music("Linux/assets/Songs/Audiomachine - By the Hand of the Mortal.mp3", 0.25)
    music.play()

    # Menu assets
    menu = add_asset('Linux/assets/menu_bg.jpg')

    choplifter_txt = add_asset('Linux/assets/choplifter_txt.png') 
    choplifter_txt[1].center = (int(round(size[0] / 2, 0)), int(round(0.06 * size[1], 0)))

    play_txt = add_asset('Linux/assets/play_txt.png') 
    play_txt[1].center = (int(round(size[0] / 2, 0)), int(round(size[1] / 2.15, 0)))

    quit_txt = add_asset('Linux/assets/quit_txt.png') 
    quit_txt[1].center = (int(round(size[0] / 2, 0)), int(round(size[1] / 1.65, 0)))

    # Game assets
    assets = assets_init(size)

    bg = assets['bg']
    chop = assets['chop']
    pews = assets['pews']
    tank1 = assets['tank1']
    t1_pews = assets['t1_pews']
    tank2 = assets['tank2']
    t2_pews = assets['t2_pews']
    jet1 = assets['jet1']
    j1_pews = assets['j1_pews']
    jet2 = assets['jet2']
    j2_pews = assets['j2_pews']
    alien = assets['alien']
    alien_pew = assets['alien_pew']

    title = cms_font.render(f'CHOPLIFTER - {lives} lives', True, (0, 0, 0, 0))
    title_rect = title.get_rect()
    title_rect.center = (size[0] // 2, 12)

    temp = bases_init(size, bases_numbers)
    bases = temp[0]
    bases_lefts = temp[1]

    hostages = temp[2]
    hostages_number = temp[3]
    total_hostage = temp[3]

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
                        music.set_volume(0.18)
                        py.mouse.set_visible(False)
                        game = True
                
                if event.type == py.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if choplifter_txt[1].collidepoint(py.mouse.get_pos()):
                            music.pause() if music.is_playing() else music.unpause()

                        elif play_txt[1].collidepoint(py.mouse.get_pos()):
                            start_timer = time.time()
                            music.set_volume(0.18)
                            py.mouse.set_visible(False)
                            game = True

                        elif quit_txt[1].collidepoint(py.mouse.get_pos()):
                            print(' ')
                            end_message(base_destroyed, tank_destroyed, jet_destroyed, alien_destroyed, rescued)
                            running = False # end of the loop

                screen.blit(menu[0], menu[1])
                screen.blit(choplifter_txt[0], choplifter_txt[1])
                screen.blit(play_txt[0], play_txt[1])
                screen.blit(quit_txt[0], quit_txt[1])

        else:
            bg_move = 0

            if pressed[py.K_z]: # - Haut
                based = 0

                chop.active_up()
                chop.move_top(-5)

                if chop.get_top() < 0:
                    chop.move_top(0 - chop.get_top())

            if pressed[py.K_s] and chop.is_grounded() == 0: # - Bas
                chop.active_up()
                chop.move_top(5)

                if chop.get_top() >= bg.get_heliport().top:
                    chop.active_grounded()
                    chop.set_top(bg.get_heliport().top + chop.get_collid().height)

            if pressed[py.K_q] and chop.is_grounded() == 0: # - Gauche  
                chop.active_left()

                if chop.get_left() < int(round(0.3 * size[0], 0)) and bg.get_position() > 0:
                    bg_move = 2

                    if bg.get_position() >= 5:
                        bg.move_left(5)
                        for base in bases:
                            base[1].left += 5

                    else:
                        bg.move_left(-1 * bg.get_left())
                        for base in bases:
                            base[1].left -= bg.get_left()

                else:
                    chop.move_left(-5)

                    if chop.get_left() < 0:
                        chop.move_left(0 - chop.get_left())

            if pressed[py.K_d] and chop.is_grounded() == 0: # - Droite
                chop.active_right()

                if chop.get_left() > (size[0] - int(round(0.3 * size[0], 0))) and bg.get_position() < 2 * size[0]:
                    bg_move = 1

                    if bg.get_position() <= 2 * size[0] - 5:
                        bg.move_left(-5)
                        for base in bases:
                            base[1].left -= 5

                    else:
                        bg.move_left(0 - bg.get_right())
                        for base in bases:
                            base[1].left -= bg.get_right()
                
                else:
                    chop.move_left(5)

                    if chop.get_left() > size[0] - chop.get_collid().width:
                        chop.move_left(size[0] - chop.get_left() - chop.get_collid().width)

            for event in py.event.get():
                if event.type == py.QUIT:
                    print(' ')
                    end_message(base_destroyed, tank_destroyed, jet_destroyed, alien_destroyed, rescued)
                    running = False # end of the loop

                if event.type == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        music.set_volume(0.25)
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
                    if pews.parts[0][1].left <= bg.get_parts()[2][1].left - 5:
                        if bg_move == 1: # Mouvement vers la droite
                            pews.move_left_rs(5)

                        elif bg_move == 2: # Mouvement vers la gauche
                            pews.move_left_rs(15)
                        
                        else:
                            pews.move_left_rs(10)

                    elif pews.parts[0][1].left > bg.get_parts()[2][1].left + 24:
                        pews.parts[0][1].left = bg.get_parts()[2][1].left + 24

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

            if chop_collid(chop, elts) and (respawn_timer == -1 or time.time() - respawn_timer > 2):
                if lives == 1:
                    print("Hélicoptère détruit... \n")
                    end_message(base_destroyed, tank_destroyed, jet_destroyed, alien_destroyed, rescued)
                    running = False

                else:
                    respawn_timer = time.time()
                    print("Hélicoptère détruit...")
                    lives -= 1

                    assets = assets_init(size)

                    bg = assets['bg']
                    chop = assets['chop']
                    pews = assets['pews']
                    tank1 = assets['tank1']
                    t1_pews = assets['t1_pews']
                    tank2 = assets['tank2']
                    t2_pews = assets['t2_pews']
                    jet1 = assets['jet1']
                    j1_pews = assets['j1_pews']
                    jet2 = assets['jet2']
                    j2_pews = assets['j2_pews']
                    alien = assets['alien']
                    alien_pew = assets['alien_pew']

                    for k in range(len(bases)):
                        bases[k][1].left = bases_lefts[k]

                        for l in range(0, len(hostages[k]), 2):
                            if hostages[k][l][2] == False:
                                hostages[k][l][2] = None
                                hostages_number -= 1
                                
                                hostages[k][l][1].top = 0 - 250
                                hostages[k][l + 1][1].top = 0 - 250

                                print("Un otage a succombé")

                            elif hostages[k][l][2] == True and bases[k][2] == False: # Repositionnement des otages libérés
                                hostages[k][l][1].left += bg.get_position()
                                hostages[k][l + 1][1].left += bg.get_position()

                    bg.position = 0

            if chop.get_collid().colliderect(bg.get_heliport()) and chop.last == 's': # Atterrissage à la base
                based = 1

                chop.set_center(bg.get_heliport().center)
                chop.active_grounded()
                chop.move_top(10)

            if cps_collid(tank1, pews, bg):
                tank1.set_position(2 * size[0] + tank1.get_parts()[0][1].width)
                tank1.set_move(1)
                
                tank1.active_left()
                tank1.set_center((3 * size[0] + tank1.get_parts()[0][1].width, int(round(0.8 * size[1], 0))))    
                t1_pews.reset()

                tank_destroyed += 1
                print("Tank détruit !")

            if cps_collid(tank2, pews, bg):
                tank2.set_position(2 * size[0] + tank2.get_parts()[0][1].width)
                tank2.set_move(1)
                
                tank2.active_left()
                tank2.set_center((3 * size[0] + tank2.get_parts()[0][1].width, int(round(0.8 * size[1], 0))))    
                t2_pews.reset()

                tank_destroyed += 1
                print("Tank détruit !")

            if cps_collid(jet1, pews, bg) and (respawn_timer == -1 or time.time() - respawn_timer > 2):
                if jet1.get_move() == 0:
                    jet1.set_position(bg.get_parts()[2][1].left + bg.get_parts()[2][1].width )
                    jet1.set_move(1)

                else:
                    jet1.set_position(0 - jet1.get_parts()[0][1].width)
                    jet1.set_move(0)

                jet_destroyed += 1
                print("Jet détruit !")

            if cps_collid(jet2, pews, bg) and (respawn_timer == -1 or time.time() - respawn_timer > 2):
                if jet2.get_move() == 0:
                    jet2.set_position(bg.get_parts()[2][1].left + bg.get_parts()[2][1].width )
                    jet2.set_move(1)

                else:
                    jet2.set_position(0 - jet2.get_parts()[0][1].width)
                    jet2.set_move(0)
                
                jet_destroyed += 1
                print("Jet détruit !")

            if pews.get_rs_collid().colliderect(alien.get_collid()) or pews.get_drop_collid().colliderect(alien.get_collid()) or pews.get_ls_collid().colliderect(alien.get_collid()):
                alien.set_move(0)
                alien.set_center(random.randint(int(round(0.35 * size[0], 0), int(round(0.65 * size[0], 0)))), bg.get_parts()[1][1].top - alien.get_collid().height)
                alien_pew.reset()

                print("Alien éliminé !")
                alien_destroyed += 1

            for base in bases:
                if pews.get_rs_collid().colliderect(base[1]) or pews.get_drop_collid().colliderect(base[1]) or pews.get_ls_collid().colliderect(base[1]):
                    base[1].top = 0 - 250
                    base[2] = False

                    print("Bâtiment détruit !")
                    base_destroyed += 1

            # Background
            screen.fill("lavender")
            for elt in bg.get_parts():
                screen.blit(elt[0], elt[1])

            # Textes
            title = cms_font.render(f'CHOPLIFTER - {lives} lives', True, (32, 32, 32, 0))
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

            # Assets - bases / hostages
            for i in range(len(bases)):
                if bases[i][2] == True:
                    for j in range(0, len(hostages[i]), 2):
                        hostages[i][j][1].left = bases[i][1].left
                        hostages[i][j + 1][1].left = hostages[i][j][1].left

                    screen.blit(bases[i][0], bases[i][1])

                else:
                    for j in range(0, len(hostages[i]), 2):
                        if hostages[i][j][2] == True:
                            if (chop.get_left() + 10 < hostages[i][j][1].left < chop.get_left() + chop.get_collid().width + 5) and chop.is_grounded() == 1 and inside < 8: # Récupération - 8 otages maximum
                                hostages[i][j][2] = False

                                print("Otage ramassé")
                                inside += 1

                                if inside == 8:
                                    print("L'hélicoptère est plein !")
                
                            elif (chop.get_collid().colliderect(hostages[i][j][1]) and chop.is_grounded() == 0) or tank1.get_collid().colliderect(hostages[i][j][1]) or tank2.get_collid().colliderect(hostages[i][j][1]) or alien_pew.get_collid().colliderect(hostages[i][j][1]): # Mort des otages
                                hostages[i][j][2] = None
                                hostages_number -= 1                            
                                
                                hostages[i][j][1].top = 0 - 250
                                hostages[i][j + 1][1].top = 0 - 250

                                print("Un otage a succombé")

                            else:
                                temp = 0

                                if chop.is_grounded() == 1 and chop.get_left() + 10 < hostages[i][j][1].left and hostages[i][j][1].left - chop.get_left() + chop.get_collid().width < 0.5 * size[0] and inside < 8:
                                    temp = -2

                                elif chop.is_grounded() == 1 and chop.get_left() + chop.get_collid().width > hostages[i][j][1].left and chop.get_left() + chop.get_collid().width - hostages[i][j][1].left < 0.5 * size[0] and inside < 8:
                                    temp = 2

                                else:
                                    temp = random.choice([-3, -1, 0, 1, 3])
                                    
                                if bg_move == 1: 
                                    temp -= 5 

                                elif bg_move == 2:
                                    temp += 5

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

            # Fin du jeu 
            if hostages_number < 1:
                print("Aucun otage restant... \n")
                end_message(base_destroyed, tank_destroyed, jet_destroyed, alien_destroyed, rescued)
                running = False

        # Affichage des modifications
        py.display.flip()

        clock.tick(90) # Limite des FPS - 90

    music.stop()
    py.quit()

# - Test
if __name__ == "__main__":
    choplifter()