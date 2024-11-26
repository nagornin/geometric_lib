import unittest
import rectangle
import math

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(10, 5), 50)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_fractions(self):
        self.assertAlmostEqual(rectangle.area(3.5, 2.5), 8.75)

    def test_area_invalid_type(self):
        self.assertRaises(TypeError, rectangle.area, "2", "3")

    def test_area_inf(self):
        self.assertRaises(ValueError, rectangle.area, math.inf, 3)

    def test_area_nan(self):
        self.assertRaises(ValueError, rectangle.area, math.nan, 3)

    def test_area_negative(self):
        self.assertRaises(ValueError, rectangle.area, -2, 3)

    def test_area_negative_zero(self):
        self.assertEqual(rectangle.area(-0, -0.0), 0)

    def test_area_args_missing(self):
        self.assertRaises(TypeError, rectangle.area)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(10, 5), 30)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(10, 0), 20)

    def test_perimeter_fractions(self):
        self.assertAlmostEqual(rectangle.perimeter(3.5, 2.5), 12)

    def test_perimeter_invalid_type(self):
        self.assertRaises(TypeError, rectangle.perimeter, "2", "3")

    def test_perimeter_inf(self):
        self.assertRaises(ValueError, rectangle.perimeter, math.inf, 3)

    def test_perimeter_nan(self):
        self.assertRaises(ValueError, rectangle.perimeter, math.nan, 3)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, rectangle.perimeter, -2, 3)

    def test_perimeter_negative_zero(self):
        self.assertEqual(rectangle.perimeter(-0, -0.0), 0)

    def test_perimeter_args_missing(self):
        self.assertRaises(TypeError, rectangle.perimeter)
