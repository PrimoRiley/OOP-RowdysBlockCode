import pygame
import os

blank = pygame.image.load(os.path.join('Assets', 'blank.png'))
light_green = pygame.image.load(os.path.join('Assets', 'move_arrow.png'))
light_blue = pygame.image.load(os.path.join('Assets', 'turnRight2.png'))
plum = pygame.image.load(os.path.join('Assets', 'turnLeft2.png'))

class Block(pygame.Rect):
    
    def __init__(self,coords,color, left, top, width, height):
        self.coords = coords
        self.color = color
        self.img = blank
        self.setImage()
        pygame.Rect.__init__(self,left,top,width,height)

    def setImage(self):
        """
        Set the image of Block based on color
        """
        if self.color == "light green":
            self.img = light_green
        elif self.color == "light blue":
            self.img = light_blue
        elif self.color == "plum":
            self.img = plum
        else:
            self.img = blank