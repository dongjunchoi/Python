import pymysql
 
conn = pymysql.connect(host='localhost', port=3336, user='root', password='java',db='python', charset='utf8')
 
curs = conn.cursor()
sql = "update sample set col03=30 where  col03=3"
cnt = curs.execute(sql)
print(cnt)
 
conn.commit()
conn.close()