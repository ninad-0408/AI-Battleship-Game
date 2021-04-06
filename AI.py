import UI
import numpy as np
import random
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
        self.gameSize = 8
        self.won = 0
        self.gameBoardPA = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardPD = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardCA = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardCD = np.empty((self.gameSize,self.gameSize), np.str)
        self.shipsP = []
        self.shipsC = []
        self.aiMoves = []

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
                try:
                    self.shipsP[i].orientation = input().lower()
                except:
                    print(Fore.RED + 'Invalid Input. Try again...' + Fore.RESET)
                    continue
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
                    row = ord(row) - ord('A')
                except:
                    print(Fore.RED + 'Invalid Input. Try again...' + Fore.RESET)
                    continue

                check = 1

                if row < 0 or row >= self.gameSize:
                    print(Fore.RED + 'Invalid row charecter...' + Fore.RESET)
                    check = 0
                
                if check and (col < 0 or col >= self.gameSize):
                    print(Fore.RED + 'Invalid column index entered...' + Fore.RESET)
                    check = 0

                if self.shipsP[i].orientation == 'h' and check:
                    if col + self.shipsP[i].size > self.gameSize:
                        print(Fore.RED + 'The ship is placed outside of given area. Please try again...')
                        check = 0
                    
                    elif check:
                        for j in range(col, col + self.shipsP[i].size):
                            if self.gameBoardPD[row, j] == UI.ship:
                                print(Fore.RED + self.shipsP[i].name + ' is overlapping another ship. Please try again...')
                                check = 0
                                break
                    
                    if check:
                        for j in range(col, col + self.shipsP[i].size):
                            self.gameBoardPD[row, j] = UI.ship
                            self.shipsP[i].location.append([row, j])
                        UI.printBoard(self.gameBoardPD, self.gameSize)

                elif self.shipsP[i].orientation == 'v' and check:
                    if row + self.shipsP[i].size > self.gameSize:
                        print(Fore.RED + 'The ship is placed outside of given area. Please try again...')
                        check = 0
                    
                    elif check:
                        for j in range(row, row + self.shipsP[i].size):
                            if self.gameBoardPD[j, col] == UI.ship:
                                print(Fore.RED + self.shipsP[i].name + ' is overlapping another ship. Please try again...')
                                check = 0
                                break
                    
                    if check:
                        for j in range(row, row + self.shipsP[i].size):
                            self.gameBoardPD[j, col] = UI.ship
                            self.shipsP[i].location.append([j, col])
                        UI.printBoard(self.gameBoardPD, self.gameSize)
                
                if check:
                    print(Fore.GREEN + 'Your ' + self.shipsP[i].name + ' is placed successfully.' + Fore.RESET)
                    break

    def aiSetup(self):
        for i in range(5):
            var = random.randint(0,1)
            if var == 1:
                self.shipsC[i].orientation = 'v'
            else:
                self.shipsC[i].orientation = 'h'
                    
            while 1:
                row = random.randint(0,self.gameSize-1)
                col = random.randint(0,self.gameSize-1)

                check = 1

                if self.shipsC[i].orientation == 'h' and check:
                    if col + self.shipsC[i].size > self.gameSize:
                        check = 0
                    
                    elif check:
                        for j in range(col, col + self.shipsC[i].size):
                            if self.gameBoardCD[row, j] == UI.ship:
                                check = 0
                                break
                    
                    if check:
                        for j in range(col, col + self.shipsP[i].size):
                            self.gameBoardCD[row, j] = UI.ship
                            self.shipsC[i].location.append([row, j])

                elif self.shipsC[i].orientation == 'v' and check:
                    if row + self.shipsC[i].size > self.gameSize:
                        check = 0
                    
                    elif check:
                        for j in range(row, row + self.shipsC[i].size):
                            if self.gameBoardCD[j, col] == UI.ship:
                                check = 0
                                break
                    
                    if check:
                        for j in range(row, row + self.shipsC[i].size):
                            self.gameBoardCD[j, col] = UI.ship
                            self.shipsC[i].location.append([j, col])
                
                if check:
                    break
    
    def aiPlay(self):
        while 1:
            row = random.randint(0,self.gameSize-1)
            col = random.randint(0,self.gameSize-1)

            if [row, col] in self.aiMoves:
                continue

            self.aiMoves.append([row,col])

            if self.gameBoardPD[row, col] == UI.ship:
                for i in range(5):
                    if [row, col] in self.shipsP[i].location:
                        rem=i
                self.aiLogic([row, col], 0, rem)
                for i in range(5):
                    if [row, col] in self.shipsP[i].location:
                        self.shipsP[i].location.remove([row, col])
                        if len(self.shipsP[i].location) == 0:
                            self.shipsP[i].isDestroyed = True
                        break
            
            check = True

            for i in range(5):
                if self.shipsP[i].isDestroyed == False:
                    check = False
                    break

            if check:
                break
        print(len(self.aiMoves))
    
    def aiLogic(self,current,direction,rem):

        if direction == 0:
            if current[0]-1>=0 and [current[0]-1, current[1]] not in self.aiMoves:
                self.aiMoves.append([current[0]-1, current[1]])
                dire = 1
                if self.gameBoardPD[current[0]-1, current[1]] == UI.ship:
                    for i in range(5):
                        if [current[0]-1, current[1]] in self.shipsP[i].location:
                            self.aiLogic([current[0]-1, current[1]], dire, rem)
                            self.shipsP[i].location.remove([current[0]-1, current[1]])
                            if len(self.shipsP[i].location) == 0:
                                self.shipsP[i].isDestroyed = True
                            break
            
            if current[0]+1<self.gameSize and [current[0]+1, current[1]] not in self.aiMoves and len(self.shipsP[rem].location)-1 > 0:
                self.aiMoves.append([current[0]+1, current[1]])
                dire = 2
                if self.gameBoardPD[current[0]+1, current[1]] == UI.ship:
                    for i in range(5):
                        if [current[0]+1, current[1]] in self.shipsP[i].location:
                            self.aiLogic([current[0]+1, current[1]], dire, rem)
                            self.shipsP[i].location.remove([current[0]+1, current[1]])
                            if len(self.shipsP[i].location) == 0:
                                self.shipsP[i].isDestroyed = True
                            break
            
            if current[1]-1>=0 and [current[0], current[1]-1] not in self.aiMoves and len(self.shipsP[rem].location)-1 > 0:
                self.aiMoves.append([current[0], current[1]-1])
                dire = 3
                if self.gameBoardPD[current[0], current[1]-1] == UI.ship:
                    for i in range(5):
                        if [current[0], current[1]-1] in self.shipsP[i].location:
                            self.aiLogic([current[0], current[1]-1], dire, rem)
                            self.shipsP[i].location.remove([current[0], current[1]-1])
                            if len(self.shipsP[i].location) == 0:
                                self.shipsP[i].isDestroyed = True
                            break
            
            if current[1]+1<self.gameSize and [current[0], current[1]+1] not in self.aiMoves and len(self.shipsP[rem].location)-1 > 0:
                self.aiMoves.append([current[0], current[1]+1])
                dire = 4
                if self.gameBoardPD[current[0], current[1]+1] == UI.ship:
                    for i in range(5):
                        if [current[0], current[1]+1] in self.shipsP[i].location:
                            self.aiLogic([current[0], current[1]+1], dire, rem)
                            self.shipsP[i].location.remove([current[0], current[1]+1])
                            if len(self.shipsP[i].location) == 0:
                                self.shipsP[i].isDestroyed = True
                            break
        
        elif direction == 1:
            if current[0]-1>=0 and [current[0]-1, current[1]] not in self.aiMoves:
                self.aiMoves.append([current[0]-1, current[1]])
                dire = 1
                if self.gameBoardPD[current[0]-1, current[1]] == UI.ship:
                    for i in range(5):
                        if [current[0]-1, current[1]] in self.shipsP[i].location:
                            self.aiLogic([current[0]-1, current[1]], dire, rem)
                            self.shipsP[i].location.remove([current[0]-1, current[1]])
                            if len(self.shipsP[i].location) == 0:
                                self.shipsP[i].isDestroyed = True
                            break
        
        elif direction == 2:
            if current[0]+1<self.gameSize and [current[0]+1, current[1]] not in self.aiMoves:
                self.aiMoves.append([current[0]+1, current[1]])
                dire = 2
                if self.gameBoardPD[current[0]+1, current[1]] == UI.ship:
                    for i in range(5):
                        if [current[0]+1, current[1]] in self.shipsP[i].location:
                            self.aiLogic([current[0]+1, current[1]], dire, rem)
                            self.shipsP[i].location.remove([current[0]+1, current[1]])
                            if len(self.shipsP[i].location) == 0:
                                self.shipsP[i].isDestroyed = True
                            break
        
        elif direction == 3:
             if current[1]-1>=0 and [current[0], current[1]-1] not in self.aiMoves:
                self.aiMoves.append([current[0], current[1]-1])
                dire = 3
                if self.gameBoardPD[current[0], current[1]-1] == UI.ship:
                    for i in range(5):
                        if [current[0], current[1]-1] in self.shipsP[i].location:
                            self.aiLogic([current[0], current[1]-1], dire, rem)
                            self.shipsP[i].location.remove([current[0], current[1]-1])
                            if len(self.shipsP[i].location) == 0:
                                self.shipsP[i].isDestroyed = True
                            break
        
        elif direction == 4:
            if current[1]+1<self.gameSize and [current[0], current[1]+1] not in self.aiMoves:
                self.aiMoves.append([current[0], current[1]+1])
                dire = 4
                if self.gameBoardPD[current[0], current[1]+1] == UI.ship:
                    for i in range(5):
                        if [current[0], current[1]+1] in self.shipsP[i].location:
                            self.aiLogic([current[0], current[1]+1], dire, rem)
                            self.shipsP[i].location.remove([current[0], current[1]+1])
                            if len(self.shipsP[i].location) == 0:
                                self.shipsP[i].isDestroyed = True
                            break
       
      
    def playerPlay(self):
        UI.clearScreen()
        for i in range(len(self.aiMoves)):
            UI.printgameBoard(self)
            print(Fore.CYAN)
            print('Enter the target cell location ')
            while 1:
                print(Fore.CYAN, end='')
                try:
                    row = input('Enter the row charecter: ').upper()
                    col = int(input('Enter the column index: '))
                    row = ord(row) - ord('A')
                except:
                    print(Fore.RED + 'Invalid Input. Try again...' + Fore.RESET)
                    continue

                check = 1

                if row < 0 or row >= self.gameSize:
                    print(Fore.RED + 'Invalid row charecter...' + Fore.RESET)
                    check = 0
                
                if check and (col < 0 or col >= self.gameSize):
                    print(Fore.RED + 'Invalid column index entered...' + Fore.RESET)
                    check = 0

                if check and (self.gameBoardPA[row, col] == UI.hit or self.gameBoardPA[row,col] == UI.miss):
                    print(Fore.RED + 'Targeted cell is already attacked. Try again...' + Fore.RESET)
                    check = 0

                if check:
                    break

            if self.gameBoardCD[row, col] == UI.ship:
                for j in range(5):
                    if [row, col] in self.shipsC[j].location:
                        self.shipsC[j].location.remove([row, col])
                        print(Fore.GREEN + 'Ohh!!! You hit my ' + self.shipsC[j].name + '.' + Fore.RESET)
                        if len(self.shipsC[j].location) == 0:
                            self.shipsC[j].isDestroyed = True
                            print(Fore.GREEN + 'Ohh!!! You sink my ' + self.shipsC[j].name + '.' + Fore.RESET)
                        break
                        
                self.gameBoardPA[row, col] = UI.hit
            
            else:
                print(Fore.RED + 'Yeah!!!! You missed my ship.' + Fore.RESET)
                self.gameBoardPA[row, col] = UI.miss

            check = 1

            for j in range(5):
                if self.shipsC[j].isDestroyed == False:
                    check = False
                    break

            if check:
                self.won = 1
                print(Fore.GREEN + 'Congratulations!!!! You won the game...' + Fore.RESET)
                break
            
            if self.gameBoardPD[self.aiMoves[i][0], self.aiMoves[i][1]] == UI.ship:
                print(Fore.RED + 'Yesss!!! I hit your ship...' + Fore.RESET)
                self.gameBoardPD[self.aiMoves[i][0], self.aiMoves[i][1]] = UI.hit
            
            else:
                print(Fore.GREEN + 'Ohh!!! I missed your ship...' + Fore.RESET)
                self.gameBoardPD[self.aiMoves[i][0], self.aiMoves[i][1]] = UI.miss
        
        if self.won == 0:
            print(Fore.RED + 'You lost the game!!!!' + Fore.RESET)



def startGame(game):
    UI.welcome()
    game.aiSetup()
    game.initialSetup()
    game.aiPlay()
    # game.playerPlay()
