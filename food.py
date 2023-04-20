import pygame
import os
from typing import Tuple

class Food(object):
    def __init__(self, coords:Tuple[int, int]) -> None:
        """Food object intializer

        Args:
            coords (Tuple[int, int]): x,y coordinates of food position
        """        
        self.img = pygame.image.load(os.path.join('Assets', 'food.png'))
        self.blankimg = pygame.image.load(os.path.join('Assets', 'blank.png'))

        self._coords = coords
        self._hitbox = pygame.Rect(coords, (50, 50))
        self._image = pygame.transform.rotate(self.img, 0)
        self._isEaten = False

    @property
    def hitbox(self) -> pygame.Rect:
        return self._hitbox

    @hitbox.setter
    def hitbox(self, value:pygame.Rect) -> None:
        self._hitbox = value

    @property
    def isEaten(self) -> bool:
        """Boolean value indicating if character reached food

        Returns:
            bool: True or false
        """        
        return self._isEaten
    
    @isEaten.setter
    def isEaten(self, value: bool) -> None:
        self._isEaten = value
    
    def blank(self) -> None:
        """Make food invisible
        """        
        self._image = pygame.transform.rotate(self.blankimg, 0)
        self.isEaten = True
