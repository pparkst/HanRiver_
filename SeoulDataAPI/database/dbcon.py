import MySQLdb

db = MySQLdb.connect("????")
cur = db.cursor()
cur.execute("SELECT sysdate()")
res = cur.fetchall()
print(res)
