'''
records = [('Alice', ('New York', 10001)),  ('Bob', ('Los Angeles', 90001))]
for name, (city, zip_code) in records:

    print(name,city,zip_code)


records = [("Alice", 30, ["Reading", "Hiking"]), ("Bob", 25, ["Gaming", "Cooking"]), ("Cara", 28, ["Dancing", "Writing"])]

for name, age, hobbies in records:
    print(f"Name: {name}, Age: {age}, Hobbies: {','.join(hobbies)}")
'''

def process_record(name, age, *contact_details):
    pass

process_record('Alice', 30, 'alice@example.com','55-0110')

process_record('Bob', 25)