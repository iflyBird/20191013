from urllib import request,parse
from http import cookiejar
#创建cookie的实例
cookie=cookiejar.CookieJar()
cookie_handler=request.HTTPHandler()
#生成Http管理器
https_handler=request.HTTPHandler()
#创建请求管理器
# 负责初次登录
# 需要输入用户名密码，用来获取登录的cookie凭证
#此url需要从登录form的action得属性中提取
opener=request.build_opener(https_handler,https_handler,cookie_handler)
def login():
    url="http://www.renren.com/Plogin.do"
    data={
        "email":"13119144223",
        "password":"123456"
    }
    #把数据进行编码
    data=parse.urlencode(data)
    req=request.Request(url,data=data.encode())
    #使用opener发起请求
    rsp=opener.open(req)
def getHomePage():
    url="http://www.renren.com/965187997/profile"
    rsp=opener.open(url)
    html=rsp.read().decode()
    with open("rsp.html","w") as f:
        f.write(html)
if __name__=="_main__":
    login()
    getHomePage()







