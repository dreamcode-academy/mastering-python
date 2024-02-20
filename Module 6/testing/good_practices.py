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
    
def test_add_positive_numbers(self):
    # Simple and clear test for adding positive numbers
    self.assertEqual(add(2, 3), 5)

def test_addition_with_positive_numbers(self):
    # Descriptive names for test methods
    self.assertEqual(add(10, 15), 25)

def test_multiply_with_large_numbers(self):
    # Testing with extremely large numbers
    self.assertEqual(multiply(1000000, 1000000), 1000000000000)

def test_divide_by_zero(self):
    # Handling division by zero
    with self.assertRaises(ZeroDivisionError):
        divide(10, 0)

def test_subtraction_independent(self):
    # Each test is independent and self-contained
    self.assertEqual(subtract(10, 5), 5)

def test_addition_independent(self):
    # Another independent test
    self.assertEqual(add(3, 2), 5)

def test_updated_behavior_of_multiply(self):
    # Updated test to reflect changes in the 'multiply' function
    # For example, if 'multiply' now handles negatives differently
    self.assertEqual(multiply(-3, 4), -12)
