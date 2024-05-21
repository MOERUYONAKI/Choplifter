import pygame as py
import time
import os 
from choplifter import *
from choplifter_2 import *

def help(): # Commande d'aide - renvoie la liste des commandes avec une description rapide
    print('Commands list -')
    print('1 - /clear \n - Clear the CHPrompt')
    print('2 - /exit \n - Close the CHPrompt')
    print('3 - /help \n - Give the commands list')
    print('4 - /play \n - Start the Choplifter game (-f for fullscreen mode / -s for survival mode)')
    print('5 - /repo \n - Return the repository link')

    time.sleep(1)
    print(' ')
    cmd_start()

def play(fullscreen : bool = False, survival : bool = False): # Commande de démarrage - lance le jeu en plein écran ou fenêtré
    if fullscreen:
        print('This mode is not completed and may got some issues... \n') 
        time.sleep(0.5)

        py.display.set_mode((0, 0), py.FULLSCREEN)
        size = (py.display.Info().current_w, py.display.Info().current_h)

    else:
        size = (1280, 720)

    print('Choplifter is starting...')
    print('Game logs will now be sent here \n')

    time.sleep(0.5)
    print(size)
    choplifter(size) if not survival else choplifter_survival(size)

    time.sleep(1)
    print(' ')
    cmd_start()

def clear(): # Commande de suppression - vide la console CHPrompt
    os.system('cls')
    time.sleep(0.5)
    cmd_start()

def exit(): # Commande de sortie - ferme la console CHPrompt
    print('Exiting command prompt...')
    time.sleep(0.5)

def repo(): # Commande d'information - renvoie le lien vers le dépot distant
    print('Repository link : https://github.com/MOERUYONAKI/Choplifter')
    
    time.sleep(0.5)
    print(' ')
    cmd_start()

def cmd_start(): # Démarage de la console CHPrompt
    commands = [ # Liste des commandes et leur raccourci
        "/help",
        'h',
        "/play",
        'p',
        "/clear",
        'cls',
        "/exit",
        '/quit', 
        'q',  
        '/escape', 
        'esc', 
        "/repo",
        'r'
    ]

    cmd = input("CHPrompt > ") # Affichage du prompt
    cmd = cmd.split(' ')

    if cmd[0] in commands or f'/{cmd[0]}' in commands: # Vérification de l'entrée
        if cmd[0] in ('help', '/help', 'h'):
            help()

        elif cmd[0] in ('play', '/play', 'p'):
            play(fullscreen = True if '-f' in cmd else False, survival = True if '-s' in cmd else False)

        elif cmd[0] in ('clear', '/clear', 'cls'):
            clear()

        elif cmd[0] in ('exit', '/exit', 'quit', '/quit', 'q', 'escape', '/escape', 'esc'):
            exit()

        elif cmd[0] in ('repo', '/repo', 'r'):
            repo()

    else: # Message d'erreur en cas de mauvais renvoie
        print('Unknown command - try "/help"\n')
        time.sleep(0.5)
        cmd_start()

if __name__ == "__main__":
    print("\n - CHOPLIFTER PROMPT - \n")
    cmd_start()