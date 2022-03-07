import sqlite3





##view contents of database
import sqlite3
con = sqlite3.connect("example.db")
cur = con.cursor()


## add items to lang
cur.execute("insert into lang values(?,?)",("Python","Python is a programming language"))
cur.execute("insert into lang values(?,?)",("Java","Java is a programming language"))
cur.execute("insert into lang values(?,?)",("C++","C++ is a programming language"))
cur.execute("insert into lang values(?,?)",("C","C is a programming language"))
cur.execute("insert into lang values(?,?)",("C#","C# is a programming language"))
cur.execute("insert into lang values(?,?)",("JavaScript","JavaScript is a programming language"))
cur.execute("insert into lang values(?,?)",("PHP","PHP is a programming language"))
## view contents of lang
cur.execute("select * from lang")
for row in cur.fetchall():
    print(row)
con.commit()
con.close()



