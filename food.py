import pygame
import os
from typing import Tuple

img = pygame.image.load(os.path.join('Assets', 'Food_40.png'))
blank = pygame.image.load(os.path.join('Assets', 'blank.png'))


class Food(object):
    def __init__(self, coords:Tuple[int, int]) -> None:
        """Food object intializer

        Args:
            coords (Tuple[int, int]): x,y coordinates of food position
        """        
        self.img = pygame.image.load(os.path.join('Assets', 'food.png'))
        self.blankimg = pygame.image.load(os.path.join('Assets', 'blank.png'))

        self._coords = coords
        self.hitbox = pygame.Rect(coords, (50, 50))
        self._image = pygame.transform.rotate(img, 0)
        self.isEaten = False

    def blank(self):
        self._image = pygame.transform.rotate(blank, 0)
        self.isEaten = True
