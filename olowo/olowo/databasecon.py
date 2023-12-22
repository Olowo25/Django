import mysql.connector

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "kambok123")
cur = myconn.cursor()

try:


    dbs = cur.execute("create table weed.igbo(name varchar(20) not null, id int(20) "
                      "not null primary key, salary float not null, State int not null)")
    print("done")
except:
    myconn.rollback()
    myconn.close()
