from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.42.19/HELLOWEB2/crawl.jsp")  
print(html)

bsObject = BeautifulSoup(html, "html.parser") 

tds = bsObject.select("td")
for i in tds:
    print (i.text)
