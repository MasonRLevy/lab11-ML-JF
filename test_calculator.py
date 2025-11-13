import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-10, 10), 0)
        self.assertEqual(add(1000, 999), 1999)
    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-10, 10), -20)
        self.assertEqual(sub(1000, 999), 1)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 1)
    def test_logarithm(self):
        self.assertEqual(log(4, 4), 1)
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(7, 7), 1)
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()