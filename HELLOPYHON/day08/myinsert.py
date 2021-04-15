import pymysql

conn = pymysql.connect(host='localhost', port=3336, user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

sql = "insert into sample(col01,col02,col03) values('4','4','4')"
cnt = curs.execute(sql)
print(cnt)

conn.commit()
conn.close()