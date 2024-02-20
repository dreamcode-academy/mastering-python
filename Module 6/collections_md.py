'''
from collections import Counter, defaultdict, OrderedDict

c = Counter(['apple', 'banana', 'apple'])

d = defaultdict(int)
print(d['key'])

o = OrderedDict([('key1', 'value1'), ('key2', 'value2')])'''

from collections import Counter, defaultdict, OrderedDict

def nested_dict_factory():
    return defaultdict(nested_dict_factory)

nested_dict = defaultdict(nested_dict_factory)

nested_dict['key1']['inner_key'] = 'value'

print(nested_dict['key1']['inner_key'])

Counter1 = Counter(['apple', 'banana'])
Counter2 = Counter(['banana', 'orange'])
combined = Counter1 + Counter2

print(combined)

process_steps = OrderedDict([('step1', 'process_data'), ('step2', 'apply_algorithm')])

for step, action in process_steps.items():
    print(f"{step}: {action}")