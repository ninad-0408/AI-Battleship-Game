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



demo = Battleship()
clearScreen()
demo.printgameBoard()       
