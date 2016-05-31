# mysql_p2.py
# coding: utf-8
import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',charset='utf8')
    conn.select_db('python')
    cur=conn.cursor()
    cur.execute('select * from tbl_user')
    for i in [1,2]:
    	result = cur.fetchone()
    	print result
  

    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])