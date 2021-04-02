import os
import colorama
from colorama import Fore, Back, Style

colorama.init()

ocean = 'O'
ship = 'S'
hit = '*'
miss ='X'

def clearScreen():
    os.system('cls')

def welcome():
    clearScreen()
    text = '                 *****************WELCOME TO BATTLESHIP*****************               '
    print(Back.YELLOW + Fore.BLACK + text + Style.RESET_ALL)
    print('\n')
    while 1:
        print(Fore.CYAN + 'Press 1 to read the rules of game and 2 to start the game: ' + Fore.RESET)
        n = int(input())
        if n==1:
            printRules()
            print(Fore.CYAN)
            os.system('pause')
            print(Fore.RESET + '\n')
            break
        elif n==2:
            break
        else:
            print(Fore.RED + 'Invalid input entered please try again...' + Fore.RESET)

def printRules():
    print(Fore.CYAN + 'RULES:' + Fore.RESET,end=' ')
    print(Fore.GREEN)
    print('>> 1. The game is played between two players. You will Play with AI.')
    print('>> 2. Each player will have its own ocean area and 5 different kind of ships of different kind: Carrier, Battleship, Cruiser, Submarine and Destroyer.')
    print('>> 3. The ocean is divided into different cells which can be located by row and column pattern. The rows are denoted as A-J and columns are denoted as 0-9.')
    print('>> 4. Width of each ship is 1 unit and length of ships are denoted in table below:\n>>\tCarrier \t5\n  \tBattleship \t4\n  \tCruiser \t3\n  \tSubmarine \t3\n  \tDestroyer \t2\n')
    print('>> 5. Each player will place the ships in its ocean either horizontally or vertically. It cannot be placed diagonally and 1 cell cannot be occupied by two ships. Ships should be placed only in allotted regions of ocean. Ships one placed are not allowed to move during game.')
    print('>> 6. After the arrangement the player will target the chosen coordinates of another player’s ocean. If it hits the ship the opponent will mark it as hit and tell which type of ship is hit else will tell as miss and now it\'s his turn to target.')
    print('>> 7. The ship will sink when all cells are hit by an opponent. The first player to sink all opponent ships is the winner.')
    print(Fore.RESET)

def printgameBoard(game):
    print('    ',end='')
    for i in range(0,game.gameSize):
        print(Back.WHITE + Fore.BLACK + str(i),end=' ' + Style.RESET_ALL)
    print('||',end=' ')
    print('    ',end='')
    for i in range(0,game.gameSize):
        print(Back.WHITE + Fore.BLACK + str(i),end=' ' + Style.RESET_ALL)
        
    print('')

    for i in range(game.gameSize):
        print(Back.WHITE + Fore.BLACK + ' ' + chr(ord('A')+i) + ' ' + Style.RESET_ALL, end=' ')

        for j in range(game.gameSize):
            if game.gameBoardPA[i,j] == ocean:
                print(Fore.BLUE + game.gameBoardPA[i,j],end=' ' + Fore.RESET)
            elif game.gameBoardPA[i,j] == ship:
                print(Fore.YELLOW + game.gameBoardPA[i,j],end=' ' + Fore.RESET)
            elif game.gameBoardPA[i,j] == hit:
                print(Fore.GREEN + game.gameBoardPA[i,j],end=' ' + Fore.RESET)
            elif game.gameBoardPA[i,j] == miss:
                print(Fore.RED + game.gameBoardPA[i,j],end=' ' + Fore.RESET)

        print('||',end=' ')
        print(Back.WHITE + Fore.BLACK + ' ' + chr(ord('A')+i) + ' ' + Style.RESET_ALL, end=' ')
            
        for j in range(game.gameSize):
            if game.gameBoardPD[i,j] == ocean:
                print(Fore.BLUE + game.gameBoardPD[i,j],end=' ' + Fore.RESET)
            elif game.gameBoardPD[i,j] == ship:
                print(Fore.YELLOW + game.gameBoardPD[i,j],end=' ' + Fore.RESET)
            elif game.gameBoardPD[i,j] == hit:
                print(Fore.RED + game.gameBoardPD[i,j],end=' ' + Fore.RESET)
            elif game.gameBoardPD[i,j] == miss:
                print(Fore.GREEN + game.gameBoardPD[i,j],end=' ' + Fore.RESET)
            
        print('')

def printBoard(gameBoard, gameSize):
    clearScreen()
    print(Fore.CYAN + 'This is your current Base\n' + Fore.RESET)
    print('    ',end='')
    for i in range(0,gameSize):
        print(Back.WHITE + Fore.BLACK + str(i),end=' ' + Style.RESET_ALL)
    
    print('')

    for i in range(gameSize):
        print(Back.WHITE + Fore.BLACK + ' ' + chr(ord('A')+i) + ' ' + Style.RESET_ALL, end=' ')

        for j in range(gameSize):
            if gameBoard[i,j] == ocean:
                print(Fore.BLUE + gameBoard[i,j],end=' ' + Fore.RESET)
            elif gameBoard[i,j] == ship:
                print(Fore.YELLOW + gameBoard[i,j],end=' ' + Fore.RESET)
            elif gameBoard[i,j] == hit:
                print(Fore.GREEN + gameBoard[i,j],end=' ' + Fore.RESET)
            elif gameBoard[i,j] == miss:
                print(Fore.RED + gameBoard[i,j],end=' ' + Fore.RESET)
        
        print('')

    print('\n')
