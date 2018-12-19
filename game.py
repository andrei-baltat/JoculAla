#!/usr/bin/env python

import random, os.path

#import basic pygame modules
import pygame as pg
from pygame.locals import *
from level import Level

class Game:
    def __init__(self, resolution : tuple, is_fullscreen : bool = True):

        pg.init()
        self.resolution : tuple = resolution
        #here multiple levels can be added
        self.levels : list = [Level('./assets/level/level1')]
        self.screen_rect : Rect = Rect(0, 0, resolution[0], resolution[1])

        #create a screen

        self.screen = pg.display.set_mode(resolution, int(is_fullscreen))
        #initialize the images
        self.images : dict = {
                "player": pg.image.load("./assets/pictures/player.png"),
                "box": pg.image.load("./assets/pictures/box.png"),
                # "empty_space": load_image(r"C:\JoculAla\assets\pictures\empty.png"),
                "enemy": pg.image.load("./assets/pictures/enemy.png"),
                "destination": pg.image.load("./assets/pictures/landing.png"),
                "wall": pg.image.load("./assets/pictures/wall.png"),
                "door": pg.image.load("./assets/pictures/door.png"),
                "bullet": pg.image.load("./assets/pictures/bullet.png"),
                "background": pg.image.load("./assets/pictures/background.jpg")
        }
        
        



    def render(self):
        # Clear the game screen (draw the background)
        self.screen.fill([255,255,255])
        scaled_background = pg.transform.scale(self.images['background'], self.resolution)
        self.screen.blit(scaled_background, (0, 0))
        pg.display.flip()
        self.levels[0].render(self.screen, self.resolution)


        # GENERAL TODO: Draw other elements on top of background
        # TODO 1: Parse the map (use level parser)
        # TODO 2: Make a grid with the same size as the map


    def run(self):  
        #TO DO: would be nice to create a name and picture for the window
        #create the background
        running = True
        while running:
            self.render()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False



def main():
    game = Game((1000, 1000))
    game.run()

if __name__ == '__main__': 
    main()