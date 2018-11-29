#!/usr/bin/env python

import random, os.path

#import basic pygame modules
import pygame
from pygame.locals import *

class Game:
    def __init__(self, resolution : tuple, is_fullscreen : bool = True):
        pygame.init()
        self.resolution : tuple = resolution
        #here multiple levels can be added
        self.levels : list = [('./assets/level/level1')]
        self.screen_rect : Rect = Rect(0, 0, resolution[0], resolution[1])
        best_depth = pygame.display.mode_ok(self.screen_rect.size, int(is_fullscreen) , 32)
        #create a screen
        self.screen = pygame.display.set_mode(self.screen_rect.size, int(is_fullscreen), best_depth)
        #initialize the images
        self.images : dict = {
                "player": pygame.image.load(r"C:\JoculAla\assets\pictures\player.png"),
                "box": pygame.image.load(r"C:\JoculAla\assets\pictures\box.png"),
                # "empty_space": load_image(r"C:\JoculAla\assets\pictures\empty.png"),
                "enemy": pygame.image.load(r"C:\JoculAla\assets\pictures\enemy.png"),
                "destination": pygame.image.load(r"C:\JoculAla\assets\pictures\landing.png"),
                "wall": pygame.image.load(r"C:\JoculAla\assets\pictures\wall.png"),
                "door": pygame.image.load(r"C:\JoculAla\assets\pictures\door.png"),
                "bullet": pygame.image.load(r"C:\JoculAla\assets\pictures\bullet.png"),
        }

        #TO DO: would be nice to create a name and picture for the window
        #create the background
        background_tile =  pygame.image.load(r"C:\JoculAla\assets\pictures\background.png")
        background = pygame.Surface(self.screen_rect.size)
        for x in range (0,self.screen_rect.width, background_tile.get_width()):
            self.screen.blit(background_tile,(x,0))
        self.screen.blit(background,(0,0))
        pygame.display.flip()




if __name__ == '__main__': Game((400,400))