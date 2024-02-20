class Calculator:
    calculation_count = 0

    @staticmethod
    def add(a,b):
        return a+ b
    
    @ classmethod

    def increment_count(cls):
        cls.calculation_count += 1
        return cls.calculation_count
    

result = Calculator.add(5, 3)
print(f"Sum result: {result}")

count = Calculator.increment_count()
print(f"Number of calculations performed: {count}")

result2 = Calculator.add(10, 20)
count2 = Calculator.increment_count()

print(f"Result of the second addition: {result2}")
print(f"Number of calculations performed after the second operation: {count2}")