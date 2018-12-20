import pygame as pg

images : dict = {
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