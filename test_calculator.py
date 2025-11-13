import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(5, 2), 10)
        self.assertEqual(mul(45, 3), 135)

    def test_divide(self): # 3 assertions
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
        self.assertAlmostEqual(div(2, 3), 1.5)
        self.assertAlmostEqual(div(4, 12), 3)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
             log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(6,8), 10.0)
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-10,0), 10.0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(36), 6.0)
        self.assertAlmostEqual(square_root(13), 3.605551275)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()