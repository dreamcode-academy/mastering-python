import pandas as pd
import sqlite3

conn = sqlite3.connect('my_database.db')

query = "SELECT * FROM my_table"

df= pd.read_sql_query(query, conn)

print("Data read from my_table: ")
print(df)

df.to_sql('my_table', conn, if_exists='replace', index=False)


conn.close()