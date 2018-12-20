import random, os.path

#import basic pygame modules
import pygame
from math import ceil
from pygame.locals import *
from typing import Tuple
from pygame import gfxdraw
from levelObjects import create_level_objects, LevelObject
#setting for the game

'''
key1=val1
key1=val1
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
    def __init__(self, level_file_path : str, resolution: Tuple[int]):
        self.level_file_path : str = level_file_path
        self.resolution = resolution
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
                 "@":"player",
                 "o":"box",
                 ".":"empty_space",
                 ">":"enemy",
                 "X":"destination",
                 "#":"wall",
                 "D":"door",
                 "*":"bullet"
            }
            # Override default configs with user settings
            for line in config_lines:
                key, value = line.split('=')
                self.configs[value] = key

            self.cell_width = ceil(self.resolution[0] / len(self.game_lines[0]))
            self.cell_height = ceil(self.resolution[1] / len(self.game_lines))
           
            # Fill level matrix based on configs and character map
            # self.level[row][col] might be "box" or "empty_space"
            self.level : list = []

            for row in range(len(self.game_lines)):
                self.level.append([])
                for column in range(len(self.game_lines[row])):
                    rect = (column * self.cell_width, row * self.cell_height, self.cell_width, self.cell_width)

                    # Add new level objects to the level matrix
                    self.level[-1].append(create_level_objects(self.configs[self.game_lines[row][column]], rect))


    def __str__(self):
        print(self.level)

    def update(self, events):
        for row in range(len(self.level)):
            for column in range(len(self.level[row])):
                self.level[row][column].update(events)
        
    def render(self, screen: pygame.Surface) -> None:
        for row in range(len(self.level)):
            for column in range(len(self.level[row])):
                self.level[row][column].render(screen)                           


