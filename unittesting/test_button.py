# import pygame
# pygame.init()
# from typing import Tuple
# import unittest
# from unittest import mock
# from unittest.mock import patch
# from hypothesis import given
# import hypothesis.strategies as st
# from button import Button

# class TestButton(unittest.TestCase):
    
#     @given(
#         image=st.none() | st.builds(pygame.Surface),
#         pos=st.tuples(st.integers(), st.integers()),
#         text_input=st.text(),
#         font=st.just(pygame.font.Font("assets/font.ttf", 8)),
#         base_color=st.text(),
#         hovering_color=st.text()
#     )
#     @patch("pygame.Surface.get_rect")
#     @patch("pygame.font.Font.render")
#     @patch("pygame.Surface.blit")
#     def test_update(self, mock_blit, mock_render, mock_get_rect, image, pos, text_input, font, base_color, hovering_color):
#         pass
#         # button = Button(image, pos, text_input, font, base_color, hovering_color)
#         # screen = mock.MagicMock()
#         # button.update(screen)
#         # if image:
#         #     mock_blit.assert_called_once_with(image, mock_get_rect.return_value)
#         # mock_blit.assert_called_with(mock_render.return_value, mock_render.return_value.get_rect.return_value)
#         # mock_render.assert_called_once_with(text_input, True, base_color)
#         # mock_get_rect.assert_called_once_with(center=pos)

#     # @given(
#     #     position=st.tuples(st.integers(), st.integers())
#     # )
#     # def test_checkForInput(self, position):
#     #     button = Button(None, (0, 0), "", None, "", "")
#     #     button._rect = mock.MagicMock(left=0, right=10, top=0, bottom=10)
#     #     self.assertTrue(button.checkForInput(position))
#     #     button._rect = mock.MagicMock(left=5, right=15, top=5, bottom=15)
#     #     self.assertFalse(button.checkForInput(position))

#     # @given(
#     #     position=st.tuples(st.integers(), st.integers())
#     # )
#     # def test_changeColor(self, position):
#     #     button = Button(None, (0, 0), "", None, "", "")
#     #     button._rect = mock.MagicMock(left=0, right=10, top=0, bottom=10)
#     #     button.changeColor(position)
#     #     if position[0] in range(button._rect.left, button._rect.right) and position[1] in range(button._rect.top, button._rect.bottom):
#     #         button._font.render.assert_called_once_with(button._text_input, True, button._hovering_color)
#     #     else:
#     #         button._font.render.assert_called_once_with(button._text_input, True, button._base_color)

# if __name__ == '__main__':
#     unittest.main()