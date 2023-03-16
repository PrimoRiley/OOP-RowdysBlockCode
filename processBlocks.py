import pygame
from block import Block


class ProcessBlocks():
    def __init__(self, blocks) -> None:
        self.blocks = sorted(blocks, key = lambda x: (x[0], x[1]))

    def getInstructionString(self):
        block_string = ""
        for i in range(len(self.blocks)):
            if self.blocks[i].color == "light green":
               block_string += "m"
            elif self.blocks[i].color == "light blue":
                block_string += "r"
            elif self.blocks[i].color == "plum":
                block_string += "l"
        return block_string

    