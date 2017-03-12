import sqlite3
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
c.execute('SELECT name FROM facts ORDER BY population DESC LIMIT 10;')

print(c.fetchall())