import sqlite3
import pandas as pd

# Function to insert sample data (Extract phase)
def insert_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('etl_demo.db')
    cursor = conn.cursor()

    # Sample employee data to insert
    employees = [
        ('John Doe', 'Software Engineer', 85000),
        ('Jane Smith', 'Data Scientist', 95000),
        ('Emily Johnson', 'Product Manager', 105000)
    ]

    for employee in employees:
        # Check if the employee already exists based on the combination of name, position, and salary
        cursor.execute('''
        SELECT COUNT(1) FROM employees WHERE name = ? AND position = ? AND salary = ?
        ''', employee)

        if cursor.fetchone()[0] == 0:  # If no match is found, insert the record
            cursor.execute('''
            INSERT INTO employees (name, position, salary)
            VALUES (?, ?, ?)
            ''', employee)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print("Sample data inserted successfully.")
    print(employees)
    
if __name__ == "__main__":
    insert_data()
    

# Transform data (e.g., increase salary by 10%)
def transform_data():
    # Connect to the database
    conn = sqlite3.connect('etl_demo.db')

    # Load the data into a pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM employees", conn)

    # Transform: Increase salary by 10%
    df['salary'] = df['salary'] * 1.10

    # Print the transformed data
    print("Transformed Data:")
    print(df)

    conn.close()
    return df

if __name__ == "__main__": 
    transformed_data = transform_data()
    
 
# Function to remove duplicates based on name, position, and salary
def remove_duplicates():
    conn = sqlite3.connect('etl_demo.db')
    cursor = conn.cursor()

    # Remove duplicates, keeping the row with the smallest 'id' for each unique combination of name, position, salary
    cursor.execute('''
    DELETE FROM employees
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM employees
        GROUP BY name, position, salary
    )
    ''')

    conn.commit()
    conn.close()

    print("Duplicates removed successfully.")
    
    

# Load the transformed data back into the database (Load phase)
def load_data(df):
    # Connect to the database
    conn = sqlite3.connect('etl_demo.db')

    # Load the transformed data into a new table or overwrite the original
    df.to_sql('employees_transformed', con=conn, if_exists='replace', index=False)

    print("Transformed data loaded into 'employees_transformed' table.")

    conn.close()

if __name__ == "__main__":
    load_data(transformed_data)
    
    

def verify_data():
    conn = sqlite3.connect('etl_demo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees_transformed")
    rows = cursor.fetchall()

    print("Data in 'employees_transformed':")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    verify_data()

