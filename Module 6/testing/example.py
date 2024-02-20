import unittest

def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def is_positive(num):
    return num > 0

def is_even(num):
    return num % 2 == 0

def multiply(a, b):
    return a * b

class TestExample(unittest.TestCase):

    def test_functionality(self):
        pass

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_division(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)
        self.assertTrue(is_positive(5))

    def test_multiply(self):
        self.assertEqual(multiply(3,4), 12)
        self.assertTrue(is_even(4))
        

if __name__ == '__main__':
    unittest.main() 
    