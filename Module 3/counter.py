from collections import Counter


count = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])

print(count.most_common()[0])