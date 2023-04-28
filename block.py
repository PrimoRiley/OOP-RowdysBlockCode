import pygame
import os
from typing import Tuple 

blank = pygame.image.load(os.path.join('Assets', 'blank.png'))
light_green = pygame.image.load(os.path.join('Assets', 'move_arrow.png'))
light_blue = pygame.image.load(os.path.join('Assets', 'turnRight2.png'))
plum = pygame.image.load(os.path.join('Assets', 'turnLeft2.png'))

class Block(pygame.Rect):
    def __init__(self,coords:Tuple[int, int], color:str, left:int, top:int, width:int, height:int) -> None:
        """Block constructor, decorates pygame.Rect object

        Args:
            coords (Tuple[int, int]): x and y coordinates
            color (str): color name
            left (int): x coordinate of left edge
            top (int): y coordinate of top edge
            width (int): rectangle width
            height (int): rectangle height
        """        
        
        self.blank = pygame.image.load(os.path.join('Assets', 'blank.png'))
        self.light_green = pygame.image.load(os.path.join('Assets', 'move_arrow.png'))
        self.light_blue = pygame.image.load(os.path.join('Assets', 'turnRight2.png'))
        self.plum = pygame.image.load(os.path.join('Assets', 'turnLeft2.png'))

        self._coords = coords
        self._color = color
        self._img = self.blank
        self._setImage()
        pygame.Rect.__init__(self,left,top,width,height)

    @property
    def coords(self) -> Tuple[int, int]:
        """Coordinate getter function

        Returns:
            Tuple[int, int]: coordinates
        """        
        return self._coords

    @coords.setter
    def coords(self, value:Tuple[int, int]) -> None:
        """Coordinate setter function

        Args:
            value (Tuple[int, int]): new coordinates
        """        
        self._coords = value

    @property
    def color(self) -> str:
        """Color getter function

        Returns:
            str: color name
        """        
        return self._color

    @color.setter
    def color(self, value:str) -> None:
        """Color setter function

        Args:
            value (str): new color name 
        """        
        self._color = value

    @property
    def img(self) -> pygame.Surface:
        """Image getter function

        Returns:
            pygame.Surface: current surface object 
        """        
        return self._img

    @img.setter
    def img(self, value:pygame.Surface) -> None:
        """Image setter 

        Args:
            value (pygame.Surface): new surface object
        """        
        self._img = value


    def _setImage(self) -> None:
        """
        Set the image of Block based on color
        """
        if self._color == "light green":
            self.img = self.light_green
        elif self._color == "light blue":
            self.img = self.light_blue
        elif self._color == "plum":
            self._img = self.plum
        else:
            self._img = self.blank