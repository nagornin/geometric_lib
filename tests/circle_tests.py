import unittest
import circle
import math

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(4), 50.26548245743669)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_fractions(self):
        self.assertAlmostEqual(circle.area(1.5), 7.0685834705770345)

    def test_area_invalid_type(self):
        self.assertRaises(TypeError, circle.area, "2")

    def test_area_inf(self):
        self.assertRaises(ValueError, circle.area, math.inf)

    def test_area_nan(self):
        self.assertRaises(ValueError, circle.area, math.nan)

    def test_area_negative(self):
        self.assertRaises(ValueError, circle.area, -2)

    def test_area_negative_zero(self):
        self.assertEqual(circle.area(-0.0), 0)

    def test_area_args_missing(self):
        self.assertRaises(TypeError, circle.area)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(2), 12.566370614359172)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_fractions(self):
        self.assertAlmostEqual(circle.perimeter(1.5), 9.42477796076938)

    def test_perimeter_invalid_type(self):
        self.assertRaises(TypeError, circle.perimeter, "2")

    def test_perimeter_inf(self):
        self.assertRaises(ValueError, circle.perimeter, math.inf)

    def test_perimeter_nan(self):
        self.assertRaises(ValueError, circle.perimeter, math.nan)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, circle.perimeter, -2)

    def test_perimeter_negative_zero(self):
        self.assertEqual(circle.perimeter(-0.0), 0)

    def test_perimeter_args_missing(self):
        self.assertRaises(TypeError, circle.perimeter)
