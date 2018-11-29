import pygame
from pygame.locals import *

class Game:
    def __init__(self, resolution : tuple, is_fullscreen : bool = True):
        pygame.init()
        self.resolution : tuple = resolution
        self.levels : list = [Level('./assets/level/level1')]
        self.screen_rect = Rect(0, 0, resolution[0], resolution[1])
        best_depth = pygame.display.mode_ok(resolution = screen_rect.size, int(is_fullscreen), 32)
        self.screen = pygame.display.set_mode(resolution = screen_rect.size, int(is_fullscreen), best_depth)
        self.images = {
                "player": load_image("./assets/pictures/player.png"),
                "box": load_image("./assets/pictures/box.png"),
                # "empty_space": load_image("./assets/pictures/empty.png"),
                "enemy": load_image("./assets/pictures/enemy.png"),
                "destination": load_image("./assets/pictures/landing.png"),
                "wall": load_image("./assets/pictures/wall.png"),
                "door": load_image("./assets/pictures/door.png"),
                "bullet": load_image("./assets/pictures/bullet.png")
        }     

    def run(self):
        