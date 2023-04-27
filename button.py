<<<<<<< HEAD
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, hovering_image = None):
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
=======
import pygame
from typing import Tuple
>>>>>>> 6a22805e2bfc7c137c71c54f4cab98ffdef2f10b


class Button(object):
	def __init__(self, image:pygame.Surface, pos:Tuple[int, int], text_input:str, font:pygame.font.Font, base_color:str, hovering_color:str) -> None:
		"""Button object initializer

		Args:
			image (pygame.Surface): image to display on button 
			pos (Tuple[int, int]): x,y position of the button
			text_input (str): Button text
			font (pygame.font.Font): text font style
			base_color (str): button color
			hovering_color (str): color to display when mouse is hovering over
		"""		
		self._image = image
		self._x_pos = pos[0]
		self._y_pos = pos[1]
		self._font = font
		self._base_color, self._hovering_color = base_color, hovering_color
		self._text_input = text_input
		self._text = self._font.render(self._text_input, True, self._base_color)
		if self._image is None:
			self._image = self._text
		self._rect = self._image.get_rect(center=(self._x_pos, self._y_pos))
		self._text_rect = self._text.get_rect(center=(self._x_pos, self._y_pos))

	def update(self, screen:pygame.Surface) -> None:
		"""Updates screen based on specified button attributes

		Args:
			screen (pygame.Surface): pygame display screen
		"""		
		if self._image is not None:
			screen.blit(self._image, self._rect)
		screen.blit(self._text, self._text_rect)

	def checkForInput(self, position:Tuple[int, int]) -> bool:
		"""Checks if button is pressed 

		Args:
			position (Tuple[int, int]): mouse position

		Returns:
			bool: True if button is pressed
		"""		
		if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
			return True
		return False

	def changeColor(self, position:Tuple[int, int]) -> None:
		"""Change button color to hovering color on mouse hover

		Args:
			position (Tuple[int, int]): x,y of mouse position
		"""		
		if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
			self._text = self._font.render(self._text_input, True, self._hovering_color)
		else:
<<<<<<< HEAD
			self.text = self.font.render(self.text_input, True, self.base_color)
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and self.hovering_image != None:
			self.image = self.hovering_image
		else:
			self.image = self.base_image
=======
			self._text = self._font.render(self._text_input, True, self._base_color)
>>>>>>> 6a22805e2bfc7c137c71c54f4cab98ffdef2f10b
