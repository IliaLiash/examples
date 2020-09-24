import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://stepik.org/media/attachments/lesson/209723/5.html").read().decode("utf-8")
s = str(html)

soup_html = BeautifulSoup(s, "html.parser")
res = []

for tag in soup_html.find_all('td'):
    res.append(int(tag.string.strip())) 
    
print(sum(res))
