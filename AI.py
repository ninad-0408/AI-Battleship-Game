import UI
import numpy as np

class Battleship:
    def __init__(self):
        self.gameSize = 10
        self.gameBoardPA = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardPD = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardCA = np.empty((self.gameSize,self.gameSize), np.str)
        self.gameBoardCD = np.empty((self.gameSize,self.gameSize), np.str)

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
        pass

    def aiSetup(self):
        pass


def startGame(game):
    UI.clearScreen()
    UI.welcome()
    UI.clearScreen()
    game.aiSetup()
    game.initialSetup()
    UI.printgameBoard(game)
    pass
