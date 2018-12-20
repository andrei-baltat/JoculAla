import assetManager
import pygame as pg
from typing import Tuple


class LevelObject:
    def __init__ (self, rect: Tuple[float]):
        self.rect = list(rect)
        self.name = 'default'

    def render(self, surface):
        scaled_image = pg.transform.scale(assetManager.images[self.name], (self.rect[2], self.rect[3]))
        surface.blit(scaled_image, (self.rect[0], self.rect[1]))

    def update(self, events):
        pass

class Wall(LevelObject):
    def __init__(self, rect):
        super(Wall, self).__init__(rect)
        self.name = 'wall'

    def render(self,surface):
        super(Wall, self).render(surface)


class EmptySpace(LevelObject):
    def __init__(self, rect):
        super(EmptySpace, self).__init__(rect)
        self.name = 'empty_space'

    def render(self,surface):
        pass
        # super(EmptySpace, self).render(surface)


class Door(LevelObject):
    def __init__(self, rect):
        super(Door, self).__init__(rect)
        self.name = "door"
        self.is_open = False

    def render(self,surface):
        if not self.is_open:
            super(Door, self).render(surface)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_e:
                self.is_open = not self.is_open

class Enemy(LevelObject):
    def __init__(self, rect):
        super(Enemy, self).__init__(rect)
        self.name = "enemy"

    def render(self,surface):
        super(Enemy, self).render(surface)

class Player(LevelObject):
    def __init__(self, rect):
        super(Player, self).__init__(rect)
        self.name = "player"

    def render(self,surface):
        super(Player, self).render(surface)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                self.rect[0] += -10

class Destination(LevelObject):
    def __init__(self, rect):
        super(Destination, self).__init__(rect)
        self.name = "destination"

    def render(self,surface):
        super(Destination, self).render(surface)

def create_level_objects(name: str, rect: tuple) -> LevelObject:
    if name == "wall":
        return Wall(rect)
    elif name == "player":
        return Player(rect)
    elif name == "destination":
        return Destination(rect)
    elif name == "door":
        return Door(rect)
    elif name == "enemy":
        return Enemy(rect)
    elif name == "empty_space":
        return EmptySpace(rect)
    return None