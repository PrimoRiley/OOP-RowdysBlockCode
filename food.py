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
        self._hitbox = pygame.Rect(coords, (50, 50))
        self._image = pygame.transform.rotate(img, 0)
        self._isEaten = False

    @property
    def hitbox(self) -> pygame.Rect:
        """Hitbox getter

        Returns:
            pygame.Rect: rect object the size of the hitbox
        """        
        return self._hitbox
    
    @hitbox.setter
    def hitbox(self, value:pygame.Rect) -> None:
        """Hitbox setter

        Args:
            value (pygame.Rect): rect object to set hitbox
        """        
        self._hitbox = value

    @property
    def isEaten(self) -> bool:
        """isEaten getter

        Returns:
            bool: returns True if food is eaten, False otherwise
        """        
        return self._isEaten
        
    @isEaten.setter
    def isEaten(self, value:bool) -> None:
        """isEaten setter

        Args:
            value (bool): boolean value to set 
        """        
        self._isEaten = value

    def blank(self) -> None:
        """Make food disapear 
        """        
        self._image = pygame.transform.rotate(blank, 0)
        self.isEaten = True
