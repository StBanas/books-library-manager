import os
import sqlite3

basedir = os.path.abspath(os.path.dirname(__file__))

conn = sqlite3.connect('../booklibrary/dbase.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS books( id integer primary key, author text, title text, user_id integer, FOREIGN KEY(user_id) REFERENCES users(user_id))""") #
c.execute("""CREATE TABLE IF NOT EXISTS users( id integer primary key, username text, email text, password text) """)
c.execute("""CREATE TABLE IF NOT EXISTS tops( id integer primary key, author1 text, title1 text) """)

# c.execute (""" CREATE TABLE IF NOT EXISTS roles( id integer primary key, name text) """)

conn.commit()
conn.close()







