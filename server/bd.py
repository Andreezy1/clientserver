import psycopg2
#connect
def connectbd():
    con = psycopg2.connect(database="kursach",user="postgres",password="12345678",host="localhost")
    print("Database opened successfully")
    cur = con.cursor()
    return cur,con  

#vstavka v tablicu
def inserttabl(name,dannie,cur,con):
    for i in range(len(dannie)):
        cur.execute("INSERT INTO %s VALUES %s;" %(name, tuple(dannie[i])))
    con.commit()
    print("Record inserted successfully")  

#vivod tablici
def selecttabl(name,cur,con):
    cur.execute("SELECT * from %s" %(name))
    rows = cur.fetchall()
    cur.execute("select column_name from information_schema.columns where information_schema.columns.table_name='%s';" %(name))
    row = cur.fetchall()
    rows.append(row)
    print("Operation done successfully")
    return (rows)

#udalenie stroki
def deletstroku(name,delitem,stolbec,cur,con):
    cur.execute("DELETE from %s where %s=%s;" %(name, stolbec, delitem))
    con.commit()  
    print("Total deleted rows:", cur.rowcount)

#proverka logina and pass
def checklogpas(login,password,cur,con):
    cur.execute("SELECT * from login where login = '%s' and password = '%s'"  %(login,password))
    b = cur.rowcount
    if b == 1:
        return 1
    else:
        return 0

