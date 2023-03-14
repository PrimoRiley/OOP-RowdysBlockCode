import pygame
import os

img = pygame.image.load(os.path.join('Assets', 'food.png'))
blank = pygame.image.load(os.path.join('Assets', 'blank.png'))


class Food(object):
    def __init__(self, coords):
        self._coords = coords
        self.hitbox = pygame.Rect(coords, (50, 50))
        self._image = pygame.transform.rotate(img, 0)
        self.isEaten = False

    def blank(self):
        self._image = pygame.transform.rotate(blank, 0)
        self.isEaten = True
