import random, os.path

#import basic pygame modules
import pygame
from pygame.locals import *

#setting for the game
player = '@'
box = 'o'
empty_space = '.' #nu cred ca o sa avem nevoie.
enemy = '>'
destination = 'X'
wall = '#'
door = 'D'
bullet = '*'
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
    def __init__(self, level_file_path):
        self.level_file_path = level_file_path

    def read_level_file(self):
        with open(self.level_file_path) as levelFile:
            # read the line from the config file
            lines = levelFile.read().splitlines()
            lines = [line.replace(' ', '') for line in lines]
            # where the config ends
            start_game_index = lines.index('game')
            # list with the config lines
            config_lines = lines[:start_game_index]
            # list with the game lines
            self.game_lines = lines[start_game_index + 1:]
            # all the configs stored in a dictionary splited by #
            self.configs = {line.split('=')[1]: line.split('=')[0] for line in config_lines}
            # level = something

    def fill_level_matrix(self):
        self.level = []
        for line in self.game_lines:
            row = []
            for elem in line:
                row.append(self.configs[elem])
            self.level.append(row)

            '''
            Configs is now a dict with the following shape:
            configs = {
                '#': 'wall',
                '@': 'player',
                ' ': 'empty',
                etc...
            }

            TODO 1: think of possible level elements (e.g. walls, empty, doors etc).
            TODO 2: make default characters for elements that are not specified in the configs 
            (e.g. walls can by default be '#')
            TODO 3: using the configs, parse the @game_lines and fill the game matrix 
            (@level) with the corresponding elements
                    Careful with dimensions. 
            TODO 4: make an example level file and test the parsing
            TODO 5: implement __str__() for the Level class to make it human readable
            e.g.
            level =[
                ['wall', 'wall', 'wall']
                ['wall', 'empty', 'wall']
                ['wall', 'empty', 'wall']
                ]
            '''
        print(self.level)


