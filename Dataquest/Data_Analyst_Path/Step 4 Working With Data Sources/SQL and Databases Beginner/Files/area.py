import sqlite3
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
c.execute('SELECT sum(area_land),sum(area_water),sum(area_land)/sum(area_water) as rt FROM facts;')

print(c.fetchall())