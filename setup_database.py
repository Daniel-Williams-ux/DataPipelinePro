import sqlite3

# connect to SQLite database
conn = sqlite3.connect('etl_demo.db')

# create a cursor object to interact with the database
cursor = conn.cursor()

# create a sample table
cursor.execute('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Corrected the typo here
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL NOT NULL
)
''')

# commit the changes and close connection
conn.commit()
conn.close()

print("Database and table created successfully.")
