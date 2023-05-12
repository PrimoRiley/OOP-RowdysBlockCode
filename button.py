import pygame 
from typing import Tuple, Optional 

class Button():
	def __init__(self, image:pygame.Surface, pos:Tuple[int, int], text_input:str, font:pygame.font.Font, base_color:str, hovering_color:str, hovering_image:Optional[pygame.Surface] = None) -> None:
		"""Button constructor

		Args:
			image (pygame.Surface): desired image loaded into pygame.Surface
			pos (Tuple[int, int]): x, y position
			text_input (str): desired text
			font (pygame.font.Font): desired font as a pygame.font.Font object
			base_color (str): color name
			hovering_color (str): color name 
			hovering_image (Optional[pygame.Surface], optional): hover image as pygame.Surface object. Defaults to None.
		"""		
		self.image = image
		self.base_image = image
		self.hovering_image = hovering_image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen:pygame.Surface) -> None:
		"""Updates the button state

		Args:
			screen (pygame.Surface): game screen as a surface
		"""		
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position:Tuple[int, int]) -> bool:
		"""Checks for something sharing the same location as the button

		Args:
			position (Tuple[int, int]): x y position (typically of the mouse)

		Returns:
			bool: True or False if position is on the button
		"""		
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position:Tuple[int, int]) -> None:
		"""Changes button color on hover

		Args:
			position (Tuple[int, int]): mouse position
		"""		
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and self.hovering_image != None:
			self.image = self.hovering_image
		else:
			self.image = self.base_image