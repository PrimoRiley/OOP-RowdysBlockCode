import pygame
import os
img = pygame.image.load(os.path.join('Assets', 'MiniRowdy.png'))


class Rowdy(object):
    def __init__(self, coords):
        self._coords = coords
        self._facing = "e"
        self._hitbox = pygame.Rect(coords, (50, 50))
        self._image = pygame.transform.rotate(img, 0)

    def move(self):
        if self._facing == "n":
            self._coords[1] -= 50
        elif self._facing == "e":
            self._coords[0] += 50
        elif self._facing == "s":
            self._coords[1] += 50
        elif self._facing == "w":
            self._coords[0] -= 50

    def turn_right(self):
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
                if wall.collidepoint(self._coords[0], self._coords[1]-50):
                    return False
            if self._facing == "e":
                if wall.collidepoint(self._coords[0]+50, self._coords[1]):
                    return False
            if self._facing == "s":
                if wall.collidepoint(self._coords[0], self._coords[1]+50):
                    return False
            if self._facing == "w":
                if wall.collidepoint(self._coords[0]-50, self._coords[1]):
                    return False
        return True
    
    def foodCollide(self, foods):
         for food in foods:
            if self._facing == "n":
                if food.hitbox.collidepoint(self._coords[0], self._coords[1]-50):
                    food.blank()
            if self._facing == "e":
                if food.hitbox.collidepoint(self._coords[0]+50, self._coords[1]):
                    food.blank()
            if self._facing == "s":
                if food.hitbox.collidepoint(self._coords[0], self._coords[1]+50):
                    food.blank()
            if self._facing == "w":
                if food.hitbox.collidepoint(self._coords[0]-50, self._coords[1]):
                    food.blank()

