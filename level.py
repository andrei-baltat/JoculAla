import random, os.path

#import basic pygame modules
import pygame
from pygame.locals import *
from typing import Tuple

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
    def __init__(self, level_file_path : str):
        self.level_file_path : str = level_file_path
        self.read_level_configs()

    def read_level_configs(self):
        with open(self.level_file_path) as levelFile:
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
                config_lines[key] = value

            # Fill level matrix based on configs and character map
            self.level : list = []
            for line in self.game_lines:
                row = []
                for elem in line:
                    row.append(self.configs[elem])
                self.level.append(row)



    def __str__(self):
        print(self.level)

    def render(self, screen: pygame.Surface, resolution: Tuple[int]) -> None:
        cell_width = resolution[0] / len(self.level[0])
        cell_height = resolution[1] / len(self.level)

        for row in range(len(self.level)):
            for column in range(len(self.level[row])):
                x, y = (column * cell_width, row * cell_height)
                cell_rect = Rect(x, y, cell_width, cell_height)
                pygame.draw.rect(screen, [0, 0, 0], cell_rect )
        return 0


