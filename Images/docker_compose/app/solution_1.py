from connect import connect, closing


connection, cursor = connect()

sql_string = "CREATE TABLE users (name VARCHAR(128), email VARCHAR(128));"
cursor.execute(sql_string)

sql_string = "INSERT INTO users(name, email) VALUES('michel', 'doc.snuggles@web.de')"
cursor.execute(sql_string)
connection.commit()

sql_string = "SELECT * FROM users;"
cursor.execute(sql_string)
output = cursor.fetchone()
print(output)

closing(connection, cursor)
