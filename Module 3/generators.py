import sys
"""
large_list = list(range(1000000))

large_generator = (x for x in range(1000000))

print('List size: ', sys.getsizeof(large_list, 'bytes'))

print('Generator size: ', sys.getsizeof(large_generator, 'bytes'))
"""
# YIELD FUNCTION

def number_generator():
    for i in range(5):
        yield i 
        yield i * i
'''
for number in number_generator():
    print(number)
'''
gen_expr = (x * 2 for x in range(5))

for number in gen_expr:
    print(number)