import pygame
import os

wall_img = pygame.image.load(os.path.join('Assets', 'Wall.png'))
wall_img2 = pygame.image.load(os.path.join('Assets', 'Wall2.png'))
blank = pygame.image.load(os.path.join('Assets', 'blank.png'))


class Wall(object):
    def __init__(self, coords, size=(50,50), img = wall_img):
        self._coords = coords
        self.hitbox = pygame.Rect(coords, size)
        self._image = pygame.transform.rotate(img, 0)
        self.isEaten = False

    def blank(self):
        self._image = pygame.transform.rotate(blank, 0)
        self.isEaten = True


