from urllib import request
from bs4  import BeautifulSoup
url="http://www.baidu.com"
rsp=request.urlopen(url)
content=rsp.read()
soup=BeautifulSoup(content,'lxml')
#bs自动转码
content=soup.prettify()
print(content)
print("=="*12)

print(soup.head)
print("=="*12)
print(soup.meta)
print("=="*12)
print("=="*12)
print("=="*12)




