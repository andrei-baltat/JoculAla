import random, os.path

#import basic pygame modules
import pygame
from pygame.locals import *

#setting for the game

'''
########################
#................o.....#
#...............#......#
#...>.......@...#......#
#...............#......D
#..X............#......#
#......................#
########################
'''

# game constants
SCREENRECT = Rect(0, 0, 400, 400)

class Level:
    def read_level_configs(self):
        with open(self.level_file_path : str) as levelFile:
            # read the line from the config file
            lines = levelFile.read().splitlines()
            lines = [line.replace(' ', '') for line in lines]
            # where the config ends
            start_game_index = lines.index('game')
            # list with the config lines
            config_lines = lines[:start_game_index]
            # list with the game lines
            self.game_lines : list = lines[start_game_index + 1:]

            # Set default configs 
            self.configs : dict = {
                "player": "@",
                "box": "o",
                "empty_space": ".",
                "enemy": ">",
                "destination": "X",
                "wall": "#",
                "door": "D",
                "bullet": "*"
            }
            # Override default configs with user settings
            for line in config_lines:
                key, value = line.split('=')
                self.config_lines[key] = value

            # Fill level matrix based on configs and character map
            self.level : list = []
            for line in self.game_lines:
                row = []
                for elem in line:
                    row.append(self.configs[elem])
                self.level.append(row)

    def __init__(self, level_file_path : str):
        self.level_file_path : str = level_file_path
        self.read_level_configs()

    def __str__(self):
        print(self.level)



