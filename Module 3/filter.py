# filter(function, iterable)
'''
def greater_than_two(x):
    return x > 2
filter(greater_than_two, [1,2,3,4])
'''

def more_than_four(x):
    return len(x) > 4

words = ['apple', 'pear', 'banana', 'kiwi']

long_words = filter(more_than_four, words)

print(list(long_words))

