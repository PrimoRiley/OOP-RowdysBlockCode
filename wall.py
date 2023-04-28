import pygame
import os
from typing import Tuple

wall_img = pygame.image.load(os.path.join('Assets', 'Wall.png'))
wall_img2 = pygame.image.load(os.path.join('Assets', 'Wall2.png'))
blank = pygame.image.load(os.path.join('Assets', 'blank.png'))


class Wall(object):
    def __init__(self, coords:Tuple[int, int], size:Tuple[int,int]=(50,50), img:pygame.Surface = wall_img) -> None:
        """Wall constructor

        Args:
            coords (Tuple[int, int]): wall coordinates (x,y)
            size (Tuple[int,int], optional): Size of wall. Defaults to (50,50).
            img (pygame.Surface, optional): Desired wall image as pygame surface. Defaults to wall_img.
        """        
        self._coords = coords
        self.hitbox = pygame.Rect(coords, size)
        self._image = pygame.transform.rotate(img, 0)
        self.isEaten = False

    def blank(self) -> None:
        """Make wall transparent
        """        
        self._image = pygame.transform.rotate(blank, 0)
        self.isEaten = True


