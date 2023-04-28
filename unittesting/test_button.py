import string
import pygame
import unittest 
from typing import Tuple
from button import Button
from hypothesis import given 
import hypothesis.strategies as st
from hypothesis.strategies import sampled_from
from unittest.mock import Mock


class TestButton(unittest.TestCase):
    @given(coords=st.tuples(st.integers(min_value=0, max_value=900), st.integers(min_value=0, max_value=900)), text = st.text(alphabet=string.ascii_letters, max_size=10), base=sampled_from(["Green", "Black"]), 
       hover=sampled_from(["Green", "Black"]))
    def test_button_initialization(self, coords, text, base, hover):
        pygame.init()

        image = pygame.Surface((50,50))
        pos = coords
        text_input = text
        font = pygame.font.Font("assets/font.ttf", 10)
        base_color = base
        hovering_color = hover

        button = Button(image, pos, text_input, font, base_color, hovering_color)

        self.assertEqual(button.image , image)
        self.assertEqual(button.x_pos , coords[0])
        self.assertEqual(button.y_pos , coords[1])
        self.assertEqual(button.font , font)
        self.assertEqual(button.base_color , base)
        self.assertEqual(button.hovering_color , hover)
        self.assertEqual(button.text_input , text)
        self.assertEqual(str(button.text), str(font.render(button.text_input, True, button.base_color)))
        self.assertEqual(button.rect , image.get_rect(center=coords))
        self.assertEqual(button.text_rect , font.render(text, True, base).get_rect(center=coords))

    
    @given(coords=st.tuples(st.integers(min_value=0, max_value=900), st.integers(min_value=0, max_value=900)), 
        text = st.text(alphabet=string.ascii_letters, max_size=10), 
        base=sampled_from(["Green", "Black"]), 
        hover=sampled_from(["Green", "Black"]))
    def test_update(self, coords:Tuple[int,int], text:str, base:str, hover:str):
        pygame.init()
        image = pygame.Surface((50,50))
        pos = coords
        font = pygame.font.Font("assets/font.ttf", 10)
        base_color = base
        hovering_color = hover
        button = Button(image, pos, text, font, base_color, hovering_color)

        # mock display
        screen = Mock(spec=pygame.Surface)
        screen.get_at.return_value = pygame.Color(base_color)

        # ensure screen was updated w/ blit
        button.update(screen)
        screen.blit.assert_any_call(image, button.rect)
        screen.blit.assert_any_call(button.text, button.text_rect)

    def test_checkForInput(self):
        # Initialize a Button object with arbitrary values
        button = Button(
            image=pygame.Surface((50, 50)),
            pos=(100, 100),
            text_input="Click Me!",
            font=pygame.font.Font(None, 20),
            base_color="blue",
            hovering_color="red"
        )

        self.assertTrue(button.checkForInput((100, 100))) #if clicked
        self.assertFalse(button.checkForInput((50, 50))) #if not clicked 

    @given(base = st.tuples(st.integers(min_value=150), st.integers(min_value=150)), hover = st.tuples(st.integers(min_value=100, max_value=150), st.integers(min_value=100, max_value=150)))
    def test_changeColor(self, base, hover):
        image = pygame.Surface((50,50))
        pos = (100, 100)
        text_input = "Test"
        font = pygame.font.Font("assets/font.ttf", 10)
        base_color = "blue"
        hovering_color = "red"
        
        button = Button(image, pos, text_input, font, base_color, hovering_color)

        # test base color
        button.changeColor(base)
        self.assertEqual(str(button.text), str(button.font.render(button.text_input, True, button.base_color)))

        # test hover color
        button.changeColor(hover)
        self.assertEqual(str(button.text), str(button.font.render(button.text_input, True, button.hovering_color)))
