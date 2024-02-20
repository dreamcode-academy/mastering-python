import sqlite3


connection = sqlite3.connect('contacts.db')
"""
print("Add a new contact")
name = input("Enter the name: ")
phone = input("Enter the phone number: ")
email = input("Enter the email address: ")

if len(name) > 0 and len(phone) > 0 and '@' in email:
"""#
    #connection.execute("""INSERT INTO contacts (name, phone, email)
    #VALUES (?, ?, ?)""", (name, phone, email))
    #connection.commit()#
#else:
 #   print("Invalid Data")

print("Contacts")

cursor = connection.execute("SELECT * FROM contacts")
for row in cursor:
    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}")

connection.close()
