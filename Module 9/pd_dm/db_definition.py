import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object using the connection
cursor = conn.cursor()

# SQL query to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    city TEXT
);
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Sample data to be inserted into the table
sample_data = [
    (1, 'Alice', 30, 'New York'),
    (2, 'Bob', 25, 'Los Angeles'),
    (3, 'Charlie', 35, 'Chicago')
]

# SQL query to insert data
insert_query = 'INSERT INTO my_table (id, name, age, city) VALUES (?, ?, ?, ?)'

# Inserting data into the table
cursor.executemany(insert_query, sample_data)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Table created and sample data inserted successfully into 'my_database.db'")
