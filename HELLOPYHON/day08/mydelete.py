import pymysql
 
conn = pymysql.connect(host='localhost', port=3336, user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

sql = "delete from sample where col03=%s"
cnt =curs.execute(sql, 4)
print(cnt)

conn.commit()
conn.close()