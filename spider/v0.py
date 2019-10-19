#爬取百度链接地址
from urllib import request,error
if __name__=='__main__':
    url="http://www.bai.com"
    try:
        req=request.Request(url)
        rsp=request.urlopen(req)
        html=rsp.read().decode()
        print(html)
    except error.URLError as e:
        print("urlerror:{0}".format(e.reason))
        print("error:{0}".format(e))
    except Exception as e:
        print(e)

