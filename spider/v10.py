#使用代理地址访问百度网站
from urllib import request,error
if __name__=='__main__':
    url="http://www.baidu.com"
    #使用代理步骤
    #1设置代理地址
    proxy={'http':"111.29.3.222:8080"}
    proxy_hander=request.ProxyHandler(proxy)
    #3.创建opener
    opener=request.build_opener(proxy_hander)
    # 4安装opener
    request.install_opener(opener)
    #2.创建proxyhandler
    #现在如果访问URL,则使用代理服务器
    try:
        rsp=request.urlopen(url)
        html=rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
       # print("error")



