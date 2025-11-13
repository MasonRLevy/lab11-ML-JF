# https://github.com/MasonRLevy/lab11-ML-JF
# Partner 1: Mason Levy
# Partner 2: Jaiden Fauble

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-10, 10), 0)
        self.assertEqual(add(1000, 999), 1999)
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-10, 10), -20)
        self.assertEqual(subtract(1000, 999), 1)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(5, 2), 10)
        self.assertEqual(mul(45, 3), 135)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2, 5), 2.5)
        self.assertAlmostEqual(div(2, 3), 1.5)
        self.assertAlmostEqual(div(4, 12), 3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 1)
    def test_logarithm(self):
        self.assertEqual(logarithm(4, 4), 1)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(7, 7), 1)
    ######## Partner 1
    def test_log_invalid_base(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
             logarithm(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(6,8), 10.0)
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-10,0), 10.0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(0), 0.0)
        self.assertAlmostEqual(square_root(36), 6.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()