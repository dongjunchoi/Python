from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import datetime

conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
curs = conn.cursor()

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")  
bs = BeautifulSoup(html, "html.parser") 

tds = bs.select(".st2")

now = datetime.datetime.now()
in_time = now.strftime("%Y%m%d,%H%M")

for td in tds :
    s_code = td.find(["a"]).get('title')
    s_name = td.text
    s_price = td.parent.select("td")[1].text.replace(",","")
    print("s_code:",s_code, end=" ")
    print("s_name:",s_name, end=" ")
    print("s_price:",s_price)
    sql = "insert into stock (s_code,s_name,s_price,in_time) values ('"+s_code+"','"+s_name+"','"+s_price+"','"+in_time+"')"
    cnt = curs.execute(sql)

conn.commit()
conn.close()