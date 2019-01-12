import sqlite3

connection = sqlite3.connect("usuarios.db")

cursor = connection.cursor()

#   Create a table with primary key autoincrement and unique columns and not nulls
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni CHAR(9) UNIQUE,
        name VARCHAR(100) NOT NULL,
        age INT,
        email VARCHAR(100) UNIQUE NOT NULL
    )
''')

#   Create data to insert into the users table, now if we have a repeated dni or email, it will fail to insert
users = [
    ("99999999Y","Paco", 34, "paco@example.es"),
    ("67895434U","Spike", 24, "spike@example.es"),
    ("98787658L","Frank", 34, "frank@example.com")
]

#   Massive insert against the users table
cursor.executemany("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", users)

#   Commit the massive insert
connection.commit()

#   Filter data in the selects, filter by dni to find only one user
cursor.execute("SELECT * FROM users WHERE dni = '99999999Y'")
user = cursor.fetchone()
print(user)

#   Filter users in the selects to only find the users who have 34 years old
cursor.execute("SELECT * FROM users WHERE age = 34")
users = cursor.fetchall()
print(users)

#   Update the name of a user and the age in the same query
cursor.execute("UPDATE users SET name = 'Paco Perea', age = 33 WHERE dni = '99999999Y'")

#   Delete user, remember don't forget the WHERE clause in the DELETE FROM, if you forget the WHERE, 
#   we delete all the data
cursor.execute("DELETE FROM users WHERE dni = '67895434U'")

#   Commit the changes
connection.commit()

#   Select all the inserted data
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print(users)

#   Close the db file
connection.close()