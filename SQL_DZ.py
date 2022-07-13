import sqlite3
list_1 = [26, 'abc', 4, 'hello', 12, 46, 'agregator']
conn = sqlite3.connect('abc.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS table_1(id INTEGER PRIMARY KEY, col_1 TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS table_2(id INTEGER PRIMARY KEY, col_1 INTEGER)')

def slovo(a):
    cursor.execute('INSERT INTO table_1(col_1) VALUES (?)', (a, ))
    conn.commit()
    cursor.execute('INSERT INTO table_2(col_1) VALUES (?)', (len(a), ))
    conn.commit()

def chyslo(a):
    if a%2 == 0:
        cursor.execute('INSERT INTO table_2(col_1) VALUES (?)', (a,))
        conn.commit()
    else:
        cursor.execute('''INSERT INTO table_1(col_1) VALUES ('нечетное')''')
        conn.commit()

def table():
    if b>=5:
        cursor.execute('''DELETE FROM table_1 WHERE id  = 1''')
        conn.commit()
    else:
        cursor.execute('''UPDATE table_1 SET col_1 = 'hello' WHERE id  = 1''')
        conn.commit()

for i in list_1:
    if type(i) is str:
        slovo(i)
    else:
        chyslo(i)

cursor.execute('SELECT * FROM table_1')
k = cursor.fetchall()
cursor.execute('SELECT * FROM table_2')
m = cursor.fetchall()
b = len(m)

table()
print(k)
print(m)

