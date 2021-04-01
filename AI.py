import UI
import numpy as np
import colorama
from colorama import Fore, Back, Style

colorama.init()

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.isDestroyed = False
        self.orientation = 'v'
        self.location = []

class Battleship:
    def __init__(self):
        self.gameSize = 10
        self.gameBoardPA = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardPD = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardCA = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardCD = np.empty((self.gameSize,self.gameSize), np.str)
        self.shipsP = []
        self.shipsC = []

        self.shipsP.append(Ship('Carrier', 5))
        self.shipsC.append(Ship('Carrier', 5))

        self.shipsP.append(Ship('Battleship', 4))
        self.shipsC.append(Ship('Battleship', 4))
        
        self.shipsP.append(Ship('Cruiser', 3))
        self.shipsC.append(Ship('Cruiser', 3))
        
        self.shipsP.append(Ship('Submarine', 3))
        self.shipsC.append(Ship('Submarine', 3))
        
        self.shipsP.append(Ship('Destroyer', 2))
        self.shipsC.append(Ship('Destroyer', 2))
        


        for i in range(self.gameSize):
            for j in range(self.gameSize):
                self.gameBoardPA[i,j] = UI.ocean
        
        for i in range(self.gameSize):
            for j in range(self.gameSize):
                self.gameBoardPD[i,j] = UI.ocean
        
        for i in range(self.gameSize):
            for j in range(self.gameSize):
                self.gameBoardCA[i,j] = UI.ocean
        
        for i in range(self.gameSize):
            for j in range(self.gameSize):
                self.gameBoardCD[i,j] = UI.ocean

    def initialSetup(self):
        UI.printBoard(self.gameBoardPD, self.gameSize)

        for i in range(5):
            print(Fore.CYAN)
            print('Place your ' + self.shipsP[i].name + ' of size ' + str(self.shipsP[i].size))
            print('Enter v if you want to place it vertically or h if you want to place it horizontally: ',end='')
            print(Fore.RESET)
            while 1:
                self.shipsP[i].orientation = input().lower()
                if self.shipsP[i].orientation == 'v':
                    break
                elif self.shipsP[i].orientation == 'h':
                    break
                else:
                    print(Fore.RED + 'Please enter the valid input... (v/h)' + Fore.RESET)   

            print(Fore.CYAN)
            print('Enter the starting cell location of ' + self.shipsP[i].name)
            while 1:
                print(Fore.CYAN,end = '')
                try:
                    row = input('Enter the row charecter: ').upper()
                    col = int(input('Enter the column index: '))
                except:
                    print(Fore.RED + 'Invalid Input. Try again...' + Fore.RESET)
                    continue

                check = 1

                if row < 'A' or row > 'J':
                    print(Fore.RED + 'Invalid row charecter...' + Fore.RESET)
                    check = 0
                
                if check and (col < 0 or col > self.gameSize - 1 ):
                    print(Fore.RED + 'Invalid column index entered...' + Fore.RESET)
                    check = 0

                if self.shipsP[i].orientation == 'h' and check:
                    if col + self.shipsP[i].size > self.gameSize:
                        print(Fore.RED + 'The ship is placed outside of given area. Please try again...')
                        check = 0
                    
                    else:
                        for j in range(col, col + self.shipsP[i].size):
                            if self.gameBoardPD[ord(row)-ord('A'), j] == UI.ship:
                                print(Fore.RED + self.shipsP[i].name + ' is overlapping another ship. Please try again...')
                                check = 0
                                break
                    
                    if check:
                        for j in range(col, col + self.shipsP[i].size):
                            self.gameBoardPD[ord(row)-ord('A'), j] = UI.ship
                            self.shipsP[i].location.append([ord(row)-ord('A'), j])
                        UI.printBoard(self.gameBoardPD, self.gameSize)

                elif self.shipsP[i].orientation == 'v' and check:
                    if ord(row) - ord('A') + self.shipsP[i].size > self.gameSize:
                        print(Fore.RED + 'The ship is placed outside of given area. Please try again...')
                        check = 0
                    
                    else:
                        for j in range(ord(row) - ord('A'), ord(row) - ord('A') + self.shipsP[i].size):
                            if self.gameBoardPD[j, col] == UI.ship:
                                print(Fore.RED + self.shipsP[i].name + ' is overlapping another ship. Please try again...')
                                check = 0
                                break
                    
                    if check:
                        for j in range(ord(row) - ord('A'), ord(row) - ord('A') + self.shipsP[i].size):
                            self.gameBoardPD[j, col] = UI.ship
                            self.shipsP[i].location.append([j, col])
                        UI.printBoard(self.gameBoardPD, self.gameSize)
                
                if check:
                    print(Fore.GREEN + 'Your ' + self.shipsP[i].name + ' is placed successfully.' + Fore.RESET)
                    break

        

    def aiSetup(self):
        pass


def startGame(game):
    UI.welcome()
    game.aiSetup()
    game.initialSetup()
    pass
