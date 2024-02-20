import sqlite3

connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()

print("Update")
#update_query = '''UPDATE contacts SET phone = ? WHERE name = ?'''

#cursor.execute(update_query,('987654321', 'John'))
#connection.commit()

print("Delete")

delete_query = '''DELETE FROM contacts WHERE name = ?'''
cursor.execute(delete_query, ("John", ))
connection.commit()

connection.close()




