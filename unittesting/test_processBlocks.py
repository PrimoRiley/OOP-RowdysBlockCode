from typing import List, Tuple
import unittest
from unittest.mock import patch, MagicMock
from hypothesis import given
from hypothesis.strategies import integers, text, tuples, lists
from processBlocks import ProcessBlocks
from block import Block

class TestProcessBlocks(unittest.TestCase):
    def test_init(self):
        # Set up some unsorted Block objects with known coordinates
        blocks = [
            Block((0, 1), "light green", 0, 1, 1, 1),
            Block((1, 0), "light blue", 1, 0, 1, 1),
            Block((0, 0), "plum", 0, 0, 1, 1)
        ]
        # Create a ProcessBlocks object with the unsorted Block objects
        pb = ProcessBlocks(blocks)
        # Check that the blocks are now sorted by coordinates
        self.assertEqual(pb.blocks[0].coords, (0, 0))
        self.assertEqual(pb.blocks[1].coords, (0, 1))
        self.assertEqual(pb.blocks[2].coords, (1, 0))

    def test_getInstructionString(self):
        # Set up some Block objects with known colors
        blocks = [
            Block((0, 0), "light green", 0, 0, 1, 1),
            Block((0, 1), "light blue", 0, 1, 1, 1),
            Block((1, 0), "plum", 1, 0, 1, 1)
        ]
        # Create a ProcessBlocks object with the Block objects
        pb = ProcessBlocks(blocks)
        # Call getInstructionString and check the result
        self.assertEqual(pb.getInstructionString(), "mrl")


if __name__ == '__main__':
    unittest.main()