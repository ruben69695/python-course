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
    ("98787658L","Frank", 67, "frank@example.com")
]

#   Massive insert against the users table
cursor.executemany("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", users)

#   Commit the massive insert
connection.commit()

#   Select all the inserted data
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

#   Show all the data in the console
for user in users:
    print(user)

#   Close the database file
connection.close()

