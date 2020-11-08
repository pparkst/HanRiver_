from MySQLdb import _mysql

db = _mysql.connect("rds-mysql-8v.cej8zsslhqnj.ap-northeast-2.rds.amazonaws.com:44433", "sa", "wjdals1qaz!", "pparkst_db")
cur = db.cursor()
cur.execute("SELECT sysdate()")
res = cur.fetchall()
print(res)
