import sqlite3


connection = sqlite3.connect('dbase.db')
print(f'connection {connection}')

c = connection.cursor()
print("********************************************")
list_users = c.execute('SELECT * FROM users').fetchall()
print('Number of users in repository:', len(list_users))
for user in list_users:
    print(user)
print("********************************************")
list_books = c.execute('SELECT * FROM books').fetchall()
print("Number of books in books list: ", len(list_books))
for book in list_books:
    print(book)
print("********************************************")
connection.close()
#
# c.execute(' INSERT INTO users (username, email, password) VALUES ("Me", "test@test.pl", "password")')
# c.execute(' INSERT INTO tops (title1, author1) VALUES ("Jordan", "Rules")')
# c.execute(' INSERT INTO books (title, author, user_id) VALUES ("Jordan B. Peterson", "12 Rules for Life", 1)')

# list_tops = c.execute('SELECT * FROM tops').fetchall()
# print("Number of top in 1000 top list: ", len(list_tops))
# for top in list_tops:
#     print(top)