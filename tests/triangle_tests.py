import unittest
import triangle
import math

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(3, 4), 6)

    def test_area_zero(self):
        self.assertEqual(triangle.area(3, 0), 0)

    def test_area_fractions(self):
        self.assertAlmostEqual(triangle.area(3.5, 4.5), 7.875)

    def test_area_invalid_type(self):
        self.assertRaises(TypeError, triangle.area, "2", "3")

    def test_area_inf(self):
        self.assertRaises(ValueError, triangle.area, math.inf, 3)

    def test_area_nan(self):
        self.assertRaises(ValueError, triangle.area, math.nan, 3)

    def test_area_negative(self):
        self.assertRaises(ValueError, triangle.area, -2, 3)

    def test_area_negative_zero(self):
        self.assertEqual(triangle.area(-0, -0.0), 0)

    def test_area_args_missing(self):
        self.assertRaises(TypeError, triangle.area)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(2, 3, 9), 14)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_fractions(self):
        self.assertAlmostEqual(triangle.perimeter(3.1, 2.4, 1.1), 6.6)

    def test_perimeter_invalid_type(self):
        self.assertRaises(TypeError, triangle.perimeter, "2", "3", "4")

    def test_perimeter_inf(self):
        self.assertRaises(ValueError, triangle.perimeter, math.inf, 3, 1)

    def test_perimeter_nan(self):
        self.assertRaises(ValueError, triangle.perimeter, math.nan, 3, 1)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, triangle.perimeter, -2, 3, 1)

    def test_perimeter_negative_zero(self):
        self.assertEqual(triangle.perimeter(-0, -0.0, 0), 0)

    def test_perimeter_args_missing(self):
        self.assertRaises(TypeError, triangle.perimeter)
