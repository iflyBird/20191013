from urllib import request
from bs4  import BeautifulSoup
url="http://www.baidu.com"
rsp=request.urlopen(url)
content=rsp.read()
#lxml为引
soup=BeautifulSoup(content,"lxml")


#查找百度数据
tags=soup.select("title")
print(tags[0])
print("=="*12)
metas=soup.select("mata[contnet='alwaays']")
print(metas[0])