import sqlite3
con = sqlite3.connect("example.db")
cur = con.cursor()

arr = []
## view contents of lang
cur. execute("SELECT * FROM person")
for row in cur.fetchall():
    arr.append(row)
con.commit()
con.close()

print(arr)
'''
## if table exists ignore else create table
try:
    con = sqlite3.connect("example.db")
    cur = con.cursor()
    cur.execute("create table lang(lang_id integer primary key, lang_name text, lang_desc text)")
    con.commit()
    con.close()
except sqlite3.OperationalError:
    pass
'''