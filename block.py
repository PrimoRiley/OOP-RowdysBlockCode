import pygame
import os

class Block(pygame.Rect):
    def __init__(self,coords,color, left, top, width, height):
        self.coords = coords
        self.color = color
        pygame.Rect.__init__(self,left,top,width,height)
