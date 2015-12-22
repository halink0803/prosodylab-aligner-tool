import MySQLdb

#update sql
db = MySQLdb.connect("localhost", "root", "t00r", "sachmem_development", unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version : %s" % data

db.close
