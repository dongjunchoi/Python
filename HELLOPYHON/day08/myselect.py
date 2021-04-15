import pymysql
 
conn = pymysql.connect(host='localhost', port=3336, user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

sql = "select * from sample"
curs.execute(sql)

rows = curs.fetchall()

print(rows)     

conn.close()
