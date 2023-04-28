import pygame
import os
from food import Food
from wall import Wall
from typing import List, Tuple

img = pygame.image.load(os.path.join('Assets', 'MiniRowdy_40.png'))


class Rowdy(object):
    def __init__(self, coords: List[int]) -> None:
        """
        Constructor
        """
        self._coords = coords
        self._facing = "e"
        self._hitbox = pygame.Rect(coords, (50, 50))
        self._image = pygame.transform.rotate(img, 0)

    @property
    def image(self) -> pygame.Surface:
        return self._image
        
    @image.setter
    def image(self, value:pygame.Surface) -> None:
        self._image = value

    def move(self) -> None:
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

    def turn_right(self) -> None:
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

    def turn_left(self) -> None:
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

    def noWallCollide(self, walls:List[Wall]) -> bool:
        """Determines if Rowdy won't collide with a wall

        Args:
            walls (List[Wall]): wall objects 

        Returns:
            bool: True if Rowdy won't collide with a wall, otherwise False
        """        
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
    
    def foodCollide(self, foods:List[Food]) -> None:
        """Fyntion to change food when rowdy colides 

        Args:
            foods (List[Food]): List of food objects
        """         
        for food in foods:
            #print(f"{food.hitbox}, Rowdy x:{self._coords[0]},y:{self._coords[1]}")
            if self._facing == "n":
                if food.hitbox.colliderect(pygame.Rect((self._coords[0],self._coords[1]-60), (45, 45))):
                    food.blank()
            if self._facing == "e":
                if food.hitbox.colliderect(pygame.Rect((self._coords[0]+60,self._coords[1]), (45, 45))):
                    food.blank()
            if self._facing == "s":
                if food.hitbox.colliderect(pygame.Rect((self._coords[0],self._coords[1]+60), (45, 45))):
                    food.blank()
            if self._facing == "w":
                if food.hitbox.colliderect(pygame.Rect((self._coords[0]-60,self._coords[1]), (45, 45))):
                    food.blank()

    def wallOnRight(self, walls:List[Wall]) -> bool:
        """Determines if there is a wall on the right side of rowdy

        Args:
            walls (List[Wall]): list of wall objects

        Returns:
            bool: True if there is a wall on the right side of rowdy, otherwise False
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

