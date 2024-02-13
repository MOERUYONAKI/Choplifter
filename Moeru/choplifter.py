import pygame as py
import time
import os 
from choplifter import *

def help():
    print('Commands list -')
    print('1 - /clear \n - Clear the CHPrompt')
    print('2 - /exit \n - Close the CHPrompt')
    print('3 - /help \n - Give the commands list')
    print('4 - /play \n - Start the Choplifter game')

    time.sleep(1)
    print(' ')
    cmd_start()

def play(fullscreen : bool = False):
    if fullscreen:
        py.display.set_mode((0, 0), py.FULLSCREEN)
        size = (py.display.Info().current_w, py.display.Info().current_h)

    else:
        size = (1280, 720)

    print('Choplifter is starting...')
    print('Game logs will now be sent here \n')

    time.sleep(0.5)
    print(size)
    choplifter(size)

    time.sleep(1)
    print(' ')
    cmd_start()

def clear():
    os.system('cls')
    time.sleep(0.5)
    cmd_start()

def exit():
    print('Exiting command prompt...')
    time.sleep(0.5)

def cmd_start():
    commands = [
        "/help",
        "/play",
        "/clear",
        "/exit"
    ]

    cmd = input("CHPrompt > ")
    cmd = cmd.split(' ')
    cmd_size = len(cmd)

    if cmd[0] in commands or f'/{cmd[0]}' in commands:
        if cmd[0] in ('help', '/help'):
            help()

        elif cmd[0] in ('play', '/play'):
            if cmd_size == 1:
                play()

            else:
                if cmd[1] == '-f':
                    play(fullscreen = True)

                else:
                    play()

        elif cmd[0] in ('clear', '/clear'):
            clear()

        elif cmd[0] in ('exit', '/exit'):
            exit()

    else:
        print('Unknown command - try "/help"\n')
        time.sleep(0.5)
        cmd_start()

if __name__ == "__main__":
    print("\n - CHOPLIFTER PROMPT - \n")
    cmd_start()