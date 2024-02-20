"""
#list_comp =[x for x in range(20) if x % 2 == 0]
#list_comp = [x * y for x in range(3) for y in range(3)]
list_comp = [x **2 for x in range(1, 31) if x % 3 == 0]
print(list_comp)


#set comprehensions

#set_comp = {x for x in [1,1,2,2,3,3]}
#set_comp = {x*2 for x in range(10)}
#print(set_comp)
words = {len(word) for word in ['apple', 'banana', 'cherry', 'date', 'apple', 'banana']}
print(words)
"""
#dictionary comprehensions
# {key_expression: value_expression for element in iterable}."

keys= ['a', 'b', 'c']

values = [1,2,3]

dictionary = {k:v for k, v in zip(keys, values)}
print(dictionary)

word_lenghts = {word:len(word) for word in ['apple', 'banana', 'cherry', 'date'] if len(word)>4}
print(word_lenghts)