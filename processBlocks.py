import pygame
from block import Block
from typing import List


class ProcessBlocks():
    def __init__(self, blocks:List[Block]) -> None:
        """Creates process blocks observer 

        Args:
            blocks (List[Block]): list of blocks for class to maintain
        """        
        self.blocks = sorted(blocks, key = lambda x: (x[0], x[1]))

    def getInstructionString(self) -> str:
        """Gets instruction string for block

        Returns:
            str: returns block instruction string (defines what block does)
        """        
        block_string = ""
        for i in range(len(self.blocks)):
            if self.blocks[i].color == "light green":
               block_string += "m"
            elif self.blocks[i].color == "light blue":
                block_string += "r"
            elif self.blocks[i].color == "plum":
                block_string += "l"
        return block_string

    