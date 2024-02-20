def divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = "You cannot divide by zero"

    return result

print(divide(1, 10))