#使用参数headers和paramas
import requests
#完整访问url是下面url加上参数构成
url="http://www.baidu.com/s?"
kw={

    "wd":"王八蛋"
}
headers={

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
rsp=requests.get(url,params=kw,headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)#返回码