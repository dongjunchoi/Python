from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.42.19/HELLOWEB2/crawl.jsp")  
print(html)

bsObject = BeautifulSoup(html, "html.parser") 

for td_text in bsObject.head.find_all('td'):
    print (td_text.gettext())
# print(bsObject)
