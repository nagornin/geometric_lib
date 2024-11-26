import unittest
import square
import math

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_fractions(self):
        self.assertAlmostEqual(square.area(1.6), 2.56)

    def test_area_invalid_type(self):
        self.assertRaises(TypeError, square.area, "2")

    def test_area_inf(self):
        self.assertRaises(ValueError, square.area, math.inf)

    def test_area_nan(self):
        self.assertRaises(ValueError, square.area, math.nan)

    def test_area_negative(self):
        self.assertRaises(ValueError, square.area, -2)

    def test_area_negative_zero(self):
        self.assertEqual(square.area(-0.0), 0)

    def test_area_args_missing(self):
        self.assertRaises(TypeError, square.area)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_fractions(self):
        self.assertAlmostEqual(square.perimeter(1.5), 6)

    def test_perimeter_invalid_type(self):
        self.assertRaises(TypeError, square.perimeter, "2")

    def test_perimeter_inf(self):
        self.assertRaises(ValueError, square.perimeter, math.inf)

    def test_perimeter_nan(self):
        self.assertRaises(ValueError, square.perimeter, math.nan)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, square.perimeter, -2)

    def test_perimeter_negative_zero(self):
        self.assertEqual(square.perimeter(-0.0), 0)

    def test_perimeter_args_missing(self):
        self.assertRaises(TypeError, square.perimeter)
