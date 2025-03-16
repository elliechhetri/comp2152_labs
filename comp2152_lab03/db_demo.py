import sqlite3

# Connect to the database
connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM demo")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
connection.close()