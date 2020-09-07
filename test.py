import sqlite3

#Create the connection
connection = sqlite3.connect('data.db')

#Allows to select things, responsible for excecuting the queries, and storing the result
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'packo', 'asdf')

insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, 'armand', 'xyz'),
    (3, 'regi', 'asdre')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

#Save data into the disk
connection.commit()

connection.close()