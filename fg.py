import MySQLdb
db = MySQLdb.connect(user="my-username",passwd="my-password",host="localhost",db="my-databasename")
cursor = db.cursor()
cursor.execute("SELECT * from my-table-name")
data=cursor.fetchall()
for row in data :
    print (row)
db.close()