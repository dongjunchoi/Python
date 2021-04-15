from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://192.168.42.19/HELLOWEB2/mycrawl")  
bs = BeautifulSoup(html, "html.parser") 

print(bs)

tds = bs.select("td")

for i in tds:
    print (i.text)
