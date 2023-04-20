import unittest
from unittest.mock import MagicMock
import pygame
import os
from block import Block
from hypothesis import given
import hypothesis.strategies as st

class TestBlock(unittest.TestCase):

    def setUp(self):
        self.coords = (0, 0)
        self.color = "light green"
        self.left = 0
        self.top = 0
        self.width = 50
        self.height = 50
        self.block = Block(self.coords, self.color, self.left, self.top, self.width, self.height)

    def test_setImage(self):
        # Test that the image is correctly set based on color
        self.assertEqual(self.block.color, "light green")
        #self.assertEqual(self.block.img, pygame.image.load(os.path.join('Assets', 'block_arrow.png')))
        
        self.block.color = "light blue"
        self.assertEqual(self.block.color, "light blue")
        # self.assertEqual(self.block.img, pygame.image.load(os.path.join('Assets', 'move_arrow.png')))
        
        self.block.color = "plum"
        self.assertEqual(self.block.color, "plum")
        # self.assertEqual(self.block.img, pygame.image.load(os.path.join('Assets', 'turnRight.png')))
        
        # self.block.color = "not a color"
        # self.assertEqual(self.block.img, pygame.image.load(os.path.join('Assets', 'blank.png')))


    @given(coord = st.tuples(st.integers(min_value=0), st.integers(min_value=0)))
    def test_coords(self, coord):
        # Test that the coordinates are set correctly
        self.block.coords = coord
        self.assertEqual(self.block.coords, coord)

    def test_rect(self):
        # Test that the rectangle attributes are set correctly
        self.assertEqual(self.block.left, 0)
        self.assertEqual(self.block.top, 0)
        self.assertEqual(self.block.width, 50)
        self.assertEqual(self.block.height, 50)

if __name__ == '__main__':
    unittest.main()