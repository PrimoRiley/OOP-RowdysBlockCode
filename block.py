import pygame
import os
from typing import Tuple 

blank = pygame.image.load(os.path.join('Assets', 'blank.png'))
light_green = pygame.image.load(os.path.join('Assets', 'move_arrow.png'))
light_blue = pygame.image.load(os.path.join('Assets', 'turnRight2.png'))
plum = pygame.image.load(os.path.join('Assets', 'turnLeft2.png'))

class Block(pygame.Rect):
    def __init__(self,coords:Tuple[int, int], color:str, left:int, top:int, width:int, height:int) -> None:
        
        self.blank = pygame.image.load(os.path.join('Assets', 'blank.png'))
        self.light_green = pygame.image.load(os.path.join('Assets', 'move_arrow.png'))
        self.light_blue = pygame.image.load(os.path.join('Assets', 'turnRight.png'))
        self.plum = pygame.image.load(os.path.join('Assets', 'turnLeft.png'))

        self._coords = coords
        self._color = color
        self._img = self.blank
        self._setImage()
        pygame.Rect.__init__(self,left,top,width,height)

    @property
    def coords(self) -> Tuple[int, int]:
        return self._coords

    @coords.setter
    def coords(self, value:Tuple[int, int]) -> None:
        self._coords = value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value:str) -> None:
        self._color = value

    @property
    def img(self) -> pygame.Surface:
        return self._img

    @img.setter
    def img(self, value:pygame.Surface) -> None:
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