import time
from choplifter import *

def help():
    print('Commands list -')
    print('1 - /clear \n - Clear the CHPrompt')
    print('2 - /exit \n - Close the CHPrompt')
    print('3 - /help \n - Give the commands list')
    print('4 - /play \n - Start the Choplifter game')

    time.sleep(2)
    print(' ')
    cmd_start()

def play():
    print('Choplifter is starting...')
    print('Game logs will now be sent here \n')

    time.sleep(0.5)
    choplifter()

    time.sleep(1)
    print(' ')
    cmd_start()

def clear():
    print('En attente de création...')

    time.sleep(0.5)
    print(' ')
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

    if cmd[0] in commands or f'/{cmd[0]}' in commands:
        if cmd[0] in ('help', '/help'):
            help()

        elif cmd[0] in ('play', '/play'):
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