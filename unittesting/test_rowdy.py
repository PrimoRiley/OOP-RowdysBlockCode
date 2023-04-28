import unittest
import pygame
from rowdy import Rowdy
from food import Food
from wall import Wall
import os

class TestRowdy(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.blank = pygame.image.load(os.path.join('Assets', 'blank.png'))
        top_border = Wall([0,0], size = (900,50), img=self.blank)
        left_border = Wall([0,0], size = (150,500), img=self.blank)
        right_border = Wall([713,0], size = (750,500), img=self.blank)
        bottom_border_top = Wall([0,350], size = (900,50), img=self.blank)
        bottom_border_bottom = Wall([0,340], size = (900,50), img=self.blank)
        side_bar_left = Wall([150,400], size = (100,100), img=self.blank)
        side_bar_right = Wall([650,400], size = (100,100), img=self.blank)
        self.walls = [top_border, left_border, right_border, bottom_border_top, bottom_border_bottom, side_bar_left, side_bar_right]

    def tearDown(self):
        pygame.quit()

    def test_move_north(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "n"
        rowdy.move()
        self.assertEqual(rowdy._coords, [0, -58.75])

    def test_move_east(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "e"
        rowdy.move()
        self.assertEqual(rowdy._coords, [58.75, 0])

    def test_move_south(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "s"
        rowdy.move()
        self.assertEqual(rowdy._coords, [0, 58.75])

    def test_move_west(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "w"
        rowdy.move()
        self.assertEqual(rowdy._coords, [-58.75, 0])

    def test_turn_right_n(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "n"
        rowdy.turn_right()
        self.assertEqual(rowdy._facing, "e")

    def test_turn_right_e(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "e"
        rowdy.turn_right()
        self.assertEqual(rowdy._facing, "s")

    def test_turn_right_s(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "s"
        rowdy.turn_right()
        self.assertEqual(rowdy._facing, "w")

    def test_turn_right_w(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "w"
        rowdy.turn_right()
        self.assertEqual(rowdy._facing, "n")

    def test_turn_left_n(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "n"
        rowdy.turn_left()
        self.assertEqual(rowdy._facing, "w")

    def test_turn_left_e(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "e"
        rowdy.turn_left()
        self.assertEqual(rowdy._facing, "n")

    def test_turn_left_s(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "s"
        rowdy.turn_left()
        self.assertEqual(rowdy._facing, "e")

    def test_turn_left_w(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "w"
        rowdy.turn_left()
        self.assertEqual(rowdy._facing, "s")

    def test_wallCollide_no_walls(self):
        rowdy = Rowdy([0, 0])
        walls = []
        self.assertTrue(rowdy.noWallCollide(walls))

    def test_wallCollide_wall_on_north(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "n"
        self.assertTrue(rowdy.noWallCollide(self.walls))

    def test_wallCollide_wall_on_east(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "e"
        self.assertFalse(rowdy.noWallCollide(self.walls))

    def test_wallCollide_wall_on_south(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "s"
        self.assertFalse(rowdy.noWallCollide(self.walls))

    def test_wallCollide_wall_on_west(self):
        rowdy = Rowdy([0, 0])
        rowdy._facing = "w"
        self.assertTrue(rowdy.noWallCollide(self.walls))

    def test_foodCollide_no_foods(self):
        rowdy = Rowdy([0, 0])
        foods = []
        self.assertIsNone(rowdy.foodCollide(foods))

    def test_foodCollide_food_on_north(self):
        rowdy = Rowdy([0, 0])
        foods = [Food([0, -58.75])]
        rowdy._facing = "n"
        rowdy.foodCollide(foods)
        self.assertEqual(foods[0]._hitbox, pygame.Rect(0, -58.75, 50, 50))

    def test_foodCollide_food_on_east(self):
        rowdy = Rowdy([0, 0])
        foods = [Food([0, -58.75])]
        rowdy._facing = "e"
        rowdy.foodCollide(foods)
        self.assertEqual(foods[0]._hitbox, pygame.Rect(0, -58.75, 50, 50))

    def test_foodCollide_food_on_south(self):
        rowdy = Rowdy([0, 0])
        foods = [Food([0, -58.75])]
        rowdy._facing = "s"
        rowdy.foodCollide(foods)
        self.assertEqual(foods[0]._hitbox, pygame.Rect(0, -58.75, 50, 50))

    def test_foodCollide_food_on_west(self):
        rowdy = Rowdy([0, 0])
        foods = [Food([0, -58.75])]
        rowdy._facing = "w"
        rowdy.foodCollide(foods)
        self.assertEqual(foods[0]._hitbox, pygame.Rect(0, -58.75, 50, 50))

    def test_wallOnRight_north(self):
        rowdy = Rowdy([0,0])  # Create an instance of YourClass for testing
        rowdy._facing = "n"  # Set rowdy's facing direction to north for testing
        walls = []

        walls.append(Wall([0,50], img=self.blank))

        # Check if wallOnRight returns True for the wall to the right of rowdy
        self.assertTrue(rowdy.wallOnRight(self.walls))
    
    def test_wallOnRight_east(self):
        rowdy = Rowdy([0,0])  # Create an instance of YourClass for testing
        rowdy._facing = "e"  # Set rowdy's facing direction to north for testing
        walls = []

        walls.append(Wall([50,0], img=self.blank))

        # Check if wallOnRight returns True for the wall to the right of rowdy
        self.assertTrue(rowdy.wallOnRight(self.walls))

    # def test_wallOnRight_south(self):
    #     rowdy = Rowdy([0,0])  # Create an instance of YourClass for testing
    #     rowdy._facing = "s"  # Set rowdy's facing direction to north for testing
    #     walls = []

    #     walls.append(Wall([-65,0], img=self.blank))

    #     # Check if wallOnRight returns True for the wall to the right of rowdy
    #     self.assertTrue(rowdy.wallOnRight(self.walls))

    # def test_wallOnRight_west(self):
    #     rowdy = Rowdy([0,0])  # Create an instance of YourClass for testing
    #     rowdy._facing = "w"  # Set rowdy's facing direction to north for testing
    #     walls = []

    #     walls.append(Wall([0,-65], img=self.blank))

    #     # Check if wallOnRight returns True for the wall to the right of rowdy
    #     self.assertTrue(rowdy.wallOnRight(self.walls))