import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class Test(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.5), math.pi * 2.5**2)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(0), 0)
        self.assertAlmostEqual(circle_perimeter(2.5), 2 * math.pi * 2.5)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(3, 4), 6)
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(2.5, 1.5), 2.5 * 1.5 / 2)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(0, 4, 5), 9)
        self.assertEqual(triangle_perimeter(2.5, 1.5, 3), 7)

    def test_square_area(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(2.5), 2.5**2)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(2.5), 4 * 2.5)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(4, 5), 20)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(2.5, 1.5), 2.5 * 1.5)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(4, 5), 18)
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        self.assertEqual(rectangle_perimeter(2.5, 1.5), 2 * (2.5 + 1.5))

if __name__ == '__main__':
    unittest.main()
