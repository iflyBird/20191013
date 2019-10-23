from urllib import request
from bs4  import BeautifulSoup
url="http://www.baidu.com"
rsp=request.urlopen(url)
content=rsp.read()
#lxml为引
soup=BeautifulSoup(content,"lxml")
#bs自动转码
#需要重新pip3 install lxml
content=soup.prettify()
#print(content)
print("=="*12)

#print(soup.head)
print("=="*12)
print(soup.meta)
print("=="*12)
print(soup.link)
print(soup.link.name)
#attrs是一个字典类型
print(soup.link.attrs)
print("=="*12)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print("=="*12)
print(soup.name)
print(soup.attrs)
print(soup.name)
#contents案例

for node in soup.head.contents:
    if node.name=="meta":
        print(node)
    if node.name=="title":
        print(node.string)






