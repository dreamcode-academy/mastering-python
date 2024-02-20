import sqlite3

connection = sqlite3.connect('contacts.db')

cursor = connection.cursor()

create_table_command ="""
CREATE TABLE IF NOT EXISTS contacts(
id INTEGER PRIMERY KEY,
name TEXT NOT NULL,
phone TEXT NOT NULL,
email TEXT UNIQUE
)
""" 

cursor.execute(create_table_command)
connection.commit()

# Create

cursor.execute("""INSERT INTO contacts (name, phone, email)
values('John', '1234567890', 'john@mail.com')""")

connection.commit()

# Read

cursor.execute('SELECT * FROM contacts')
for row in cursor.fetchall():
    print(row)

    
# Update

#cursor.execute("""UPDATE contacts 
#SET email = 'newmail@mail.com'
#WHERE name = 'Alice' """)
#connection.commit()

# DELETE

cursor.execute("""DELETE FROM contacts WHERE name ='Alice' """)
connection.commit()

connection.close()