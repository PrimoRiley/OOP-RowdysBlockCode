import unittest
import pygame
from hypothesis import given
import hypothesis.strategies as st
from food import Food

class TestFood(unittest.TestCase):

    def test_hitbox(self):
        food = Food((100, 100))
        assert isinstance(food.hitbox, pygame.Rect)

    def test_isEaten(self):
        food = Food((100, 100))
        assert food.isEaten == False

    def test_blank(self):
        food = Food((100, 100))
        food.blank()
        assert food.isEaten == True

    @given(coords=st.tuples(st.integers(min_value=0, max_value=900), st.integers(min_value=0, max_value=500)))
    def test_init(self, coords):
        food = Food(coords)
        assert isinstance(food.img, pygame.Surface)
        assert isinstance(food.blankimg, pygame.Surface)
        assert isinstance(food.hitbox, pygame.Rect)
        assert isinstance(food._image, pygame.Surface)
        assert food._isEaten == False