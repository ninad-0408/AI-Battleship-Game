import os
import colorama
import numpy as np
from colorama import Fore, Back, Style
from numpy.testing._private.utils import decorate_methods

colorama.init()

ocean = 'O'
ship = 'S'
hit = '*'
miss ='X'

def clearScreen():
    os.system('cls')

def welcome():
    text = '                 *****************WELCOME TO BATTLESHIP*****************               '
    print(Back.YELLOW + Fore.BLACK + text + Style.RESET_ALL)
    print('\n')
    while 1:
        print(Fore.CYAN + 'Press 1 to read the rules of game and 2 to start the game: ' + Fore.RESET)
        n = int(input())
        if n==1:
            printRules()
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

class Battleship:
    def __init__(self):
        self.gameSize = 10
        self.gameBoardPA = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardPD = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardCA = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardCD = np.empty((self.gameSize,self.gameSize), np.str)

        for i in range(self.gameSize):
            for j in range(self.gameSize):
                self.gameBoardPA[i,j] = ocean
        
        for i in range(self.gameSize):
            for j in range(self.gameSize):
                self.gameBoardPD[i,j] = ocean
        
        for i in range(self.gameSize):
            for j in range(self.gameSize):
                self.gameBoardCA[i,j] = ocean
        
        for i in range(self.gameSize):
            for j in range(self.gameSize):
                self.gameBoardCD[i,j] = ocean


    def printgameBoard(self):
        print('    ',end='')
        for i in range(0,self.gameSize):
            print(Back.WHITE + Fore.BLACK + str(i),end=' ' + Style.RESET_ALL)
        print('||',end=' ')
        print('    ',end='')
        for i in range(0,self.gameSize):
            print(Back.WHITE + Fore.BLACK + str(i),end=' ' + Style.RESET_ALL)
        
        print('')

        for i in range(self.gameSize):
            print(Back.WHITE + Fore.BLACK + ' ' + chr(ord('A')+i) + ' ' + Style.RESET_ALL, end=' ')

            for j in range(self.gameSize):
                if self.gameBoardPA[i,j] == ocean:
                    print(Fore.BLUE + self.gameBoardPA[i,j],end=' ' + Fore.RESET)
                elif self.gameBoardPA[i,j] == ship:
                    print(Fore.MAGENTA + self.gameBoardPA[i,j],end=' ' + Fore.RESET)
                elif self.gameBoardPA[i,j] == hit:
                    print(Fore.RED + self.gameBoardPA[i,j],end=' ' + Fore.RESET)
                elif self.gameBoardPA[i,j] == miss:
                    print(Fore.GREEN + self.gameBoardPA[i,j],end=' ' + Fore.RESET)

            print('||',end=' ')
            print(Back.WHITE + Fore.BLACK + ' ' + chr(ord('A')+i) + ' ' + Style.RESET_ALL, end=' ')
            
            for j in range(self.gameSize):
                if self.gameBoardPD[i,j] == ocean:
                    print(Fore.BLUE + self.gameBoardPD[i,j],end=' ' + Fore.RESET)
                elif self.gameBoardPD[i,j] == ship:
                    print(Fore.MAGENTA + self.gameBoardPD[i,j],end=' ' + Fore.RESET)
                elif self.gameBoardPD[i,j] == hit:
                    print(Fore.RED + self.gameBoardPD[i,j],end=' ' + Fore.RESET)
                elif self.gameBoardPD[i,j] == miss:
                    print(Fore.GREEN + self.gameBoardPD[i,j],end=' ' + Fore.RESET)
            
            print('')


printRules()
clearScreen()
demo = Battleship()
demo.printgameBoard()
