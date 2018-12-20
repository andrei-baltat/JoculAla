#!/usr/bin/env python

import random, os.path

#import basic pygame modules
import pygame as pg
from pygame.locals import *
from level import Level
import assetManager

class Game:
    def __init__(self, resolution : tuple, is_fullscreen : bool = True):

        pg.init()
        self.resolution : tuple = resolution
        
        # Here multiple levels can be added
        self.levels : list = [Level('./assets/levels/level1', resolution)]
        self.screen_rect : Rect = Rect(0, 0, resolution[0], resolution[1])

        # Create a screen
        self.screen = pg.display.set_mode(resolution, int(is_fullscreen))

        
    def render(self):
        # Clear the game screen (draw the background)
        # self.screen.fill([255,255,255])
        scaled_background = pg.transform.scale(assetManager.images['background'], self.resolution)
        self.screen.blit(scaled_background, (0, 0))
        self.levels[0].render(self.screen)

        # pg.display.update()
        pg.display.flip()


    def update(self, events):
        self.levels[0].update(events)

    def run(self):  
        #TO DO: would be nice to create a name and picture for the window
        #create the background
        running = True
        while running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    running = False
            self.update(events)
            self.render()



def main():
    game = Game((1000, 1000))
    game.run()

if __name__ == '__main__': 
    main()