# *
# constante final pentru partile componente ale levelului: 
    #

class Level:
    def __init__(self,levelFilePath):
        self.levelFilePath = levelFilePath
    def readLevelFile(self):
        with open(self.levelFilePath) as levelFile:
            lines = levelFile.readlines()
            startGameIndex = lines.index('game')
            configLines = lines[:startGameIndex]
            gameLines = lines[startGameIndex + 1:]
            
            configs = {line.split('=')[0]: line.split('=')[1] for line in configLines}


