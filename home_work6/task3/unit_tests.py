import unittest
from task3 import factorial

class TestCase(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_factorial_errors(self):
        with self.assertRaises(ValueError):
            factorial(-5)
        with self.assertRaises(ValueError):
            factorial(21)
        with self.assertRaises(ValueError):
            factorial(10000)

    def tearDown(self):
        print("tearDown")
