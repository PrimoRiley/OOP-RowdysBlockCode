import pygame
import os
from food import Food

img = pygame.image.load(os.path.join('Assets', 'MiniRowdy_40.png'))


class Rowdy(object):
    def __init__(self, coords):
        """
        Constructor
        """
        self._coords = coords
        self._facing = "e"
        self._hitbox = pygame.Rect(coords, (50, 50))
        self._image = pygame.transform.rotate(img, 0)

    def move(self):
        """
        Moves rowdy 1 space in the direction he is facing
        """
        if self._facing == "n":
            self._coords[1] -= 58.75
        elif self._facing == "e":
            self._coords[0] += 58.75
        elif self._facing == "s":
            self._coords[1] += 58.75
        elif self._facing == "w":
            self._coords[0] -= 58.75

    def turn_right(self):
        """
        Rotates rowdy clokwise 90 degrees in place
        """
        if self._facing == "n":
            self._facing = "e"
            self._image = pygame.transform.rotate(self._image, -90)
        elif self._facing == "e":
            self._facing = "s"
            self._image = pygame.transform.rotate(self._image, -90)
        elif self._facing == "s":
            self._facing = "w"
            self._image = pygame.transform.rotate(self._image, -90)
        elif self._facing == "w":
            self._facing = "n"
            self._image = pygame.transform.rotate(self._image, -90)

    def turn_left(self):
        """
        Rotates rowdy counterclokwise 90 degrees in place
        """
        if self._facing == "n":
            self._facing = "w"
            self._image = pygame.transform.rotate(self._image, 90)
        elif self._facing == "e":
            self._facing = "n"
            self._image = pygame.transform.rotate(self._image, 90)
        elif self._facing == "s":
            self._facing = "e"
            self._image = pygame.transform.rotate(self._image, 90)
        elif self._facing == "w":
            self._facing = "s"
            self._image = pygame.transform.rotate(self._image, 90)

    def wallCollide(self, walls):
        for wall in walls:
            if self._facing == "n":
                if wall.hitbox.colliderect(pygame.Rect((self._coords[0],self._coords[1]-60), (40, 40))):
                    return False
            if self._facing == "e":
                if wall.hitbox.colliderect(pygame.Rect((self._coords[0]+60,self._coords[1]), (40, 40))):
                    return False
            if self._facing == "s":
                if wall.hitbox.colliderect(pygame.Rect((self._coords[0],self._coords[1]+60), (40, 40))):
                    return False
            if self._facing == "w":
                if wall.hitbox.colliderect(pygame.Rect((self._coords[0]-60,self._coords[1]), (40, 40))):
                    return False
        return True
    
    def foodCollide(self, foods):
         for food in foods:
            #print(f"{food.hitbox}, Rowdy x:{self._coords[0]},y:{self._coords[1]}")
            if self._facing == "n":
                if food.hitbox.colliderect(pygame.Rect((self._coords[0],self._coords[1]-60), (45, 45))):
                    food.blank()
                    foods.remove(food)
            if self._facing == "e":
                if food.hitbox.colliderect(pygame.Rect((self._coords[0]+60,self._coords[1]), (45, 45))):
                    food.blank()
                    foods.remove(food)
            if self._facing == "s":
                if food.hitbox.colliderect(pygame.Rect((self._coords[0],self._coords[1]+60), (45, 45))):
                    food.blank()
                    foods.remove(food)
            if self._facing == "w":
                if food.hitbox.colliderect(pygame.Rect((self._coords[0]-60,self._coords[1]), (45, 45))):
                    food.blank()
                    foods.remove(food)

    def wallOnRight(self, walls):
        """
        Return True if wall on right of rowdy
        """
        for wall in walls:
            if self._facing == "n":
                if wall.hitbox.colliderect(pygame.Rect((self._coords[0]+60,self._coords[1]), (40, 40))):
                    return True
            if self._facing == "e":
                if wall.hitbox.colliderect(pygame.Rect((self._coords[0],self._coords[1]+60), (40, 40))):
                    return True
            if self._facing == "s":
                if wall.hitbox.colliderect(pygame.Rect((self._coords[0]-60,self._coords[1]), (40, 40))):
                    return True
            if self._facing == "w":
                if wall.hitbox.colliderect(pygame.Rect((self._coords[0],self._coords[1]-60), (40, 40))):
                    return True
        return False

