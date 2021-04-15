import pymysql
import time

conn = pymysql.connect(host='localhost', port=3336, user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

sql = "insert into sample(col01,col02,col03) values(%s,%s,%s)"

start = time.time()

for i in range(300000):
    cnt = curs.execute(sql,(i,i,i))
    
end = time.time()

elapse = end - start

print("start : ",start)
print("end : ",end)
print("elapse : ",elapse)

conn.commit()
conn.close()