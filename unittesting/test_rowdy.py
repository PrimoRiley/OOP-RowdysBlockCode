import unittest
import pygame
from rowdy import Rowdy
from food import Food

class TestRowdy(unittest.TestCase):
    def setUp(self):
        pygame.init()

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
        walls = [pygame.Rect(0, -58.75, 50, 50)]
        rowdy._facing = "n"
        self.assertFalse(rowdy.noWallCollide(walls))

    def test_wallCollide_wall_on_east(self):
        rowdy = Rowdy([0, 0])
        walls = [pygame.Rect(58.75, 0, 50, 50)]
        rowdy._facing = "e"
        self.assertFalse(rowdy.noWallCollide(walls))

    def test_wallCollide_wall_on_south(self):
        rowdy = Rowdy([0, 0])
        walls = [pygame.Rect(0, 58.75, 50, 50)]
        rowdy._facing = "s"
        self.assertFalse(rowdy.noWallCollide(walls))

    def test_wallCollide_wall_on_west(self):
        rowdy = Rowdy([0, 0])
        walls = [pygame.Rect(-58.75, 0, 50, 50)]
        rowdy._facing = "w"
        self.assertFalse(rowdy.noWallCollide(walls))

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

    