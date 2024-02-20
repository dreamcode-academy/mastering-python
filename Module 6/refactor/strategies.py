# Code optimization

test_list = [1,2,3]

def complex_function(items):
    result = []
    for item in items:
        for x in range(10):
            result.append(item * x)

    return result

print(complex_function(test_list))

def simplified_function(items):
    return [item * x for item in set(items) for x in range(10)]

print(simplified_function(test_list))