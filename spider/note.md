urllib.error
    urlError产生的原因:
        没网
        服务器连接失败
        知不道制定服务器
        是oserror的子类
      httpError,是urlerror的一个子类
    俩者区别:
        httperror是对应的http请求的返回码错误，如果返回码是400以上的，则引发httpError
        urlerror对应的一般是网络出现问题，包括url问题
        关系区别:
 - userAgent
    假装成ua来访问者身份
  -ProxyHandler处理(代理服务器)
    使用代理Ip是爬虫的常用手段,（反爬虫）
    获取代理服务器的地址:
                      www.xicidaili.com
                      www.goubanjia.com
     代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站,所以代理一定要喝多很多
     基本使用步骤：
        1、设置代理地址
        2、创建proxyhandler
        3、创建opener
        4、安装opener
       案例v10
    -proxyHandler处理(代理服务器)
 -cookie *&session
    -cookie是发放给用户（http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用俩记录
 -cookie和session区别
    存放位置不同
    cookie不安全
    session会保存在服务器上一段时间，会过期
    半个的cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
    
 -session的存放位置
    -存在服务器
    -一般情况下，session是放在内存中或者数据库中
    -没有cookie登录，案例v9
    -没有cookie 登录,案例9,没有使用cookie则反馈为没有登录状态
 -使用cookie登录
       直接把cookie复制下来，然后手动放入请求头，案例v12
       http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        -cookiejar
            管理存储cookie,向传出的http请求添加cookie
            -fileCookiejar
            mozillacokiejar
            lwpcookiejar
            自动使用cookie登录，大致流程是
            打开登录页面后自动通过用户名密码登录
            自动提取反馈回来的cookie
            利用提取的cookie登录隐私页面
  -ssl
        -ssl证书就是指遵守ssl安全套路竭诚的服务器数字证书
        -美国网景公司开发
        -ca
        -遇到不信任的ssl证书，需要单独处理，案例v17
        
   -js加密
    -有的反爬虫策略采用js对需要传输的数据进行加密处理(通常是去md5值)
    -经过加密，传输的就是秘闻，但是
    -加密函数或者过程一定是在浏览器完场，也就是一定会把代码暴露给使用者
    -通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    -过程参考v0
    -ajax
      -异步请求
      -一定会有url，请求方法可能有数据
      -一般使用json格式
      -案例,爬取豆瓣数据,案例v2
   -requests
    -requests-献给人类
    -http for human,更简单更友好
    -底层使用的是urllib3
    -开源地址:https://github.com/requests/requests
    -中文文档:https://docs.python-requests.org/zh_CN/latest/index.html
    安装:conda install requests
    -get请求
        -requests.get(url)
        -requests.request("get",url)
        -可以带有headers和parmas参数
        -案例v3
    -get返回内容
        -v4案例
     -post案例
     -proxy代理
        proxies={
        "http":"addresss of proxy"
        "https":"address of proxy"
        }
        rsp=requests.request("get","http:xx",proxies=proxies)
       
        代理有可能报错，如果使用人数多，考虑安全问题，可能会被强关闭
    -用户验证
        -代理验证
                #可能需要时yonghttp basic auth 可以这样
                #格式为 用户名：密码@代理地址:端口地址
                proxy={
                "http":"china:123456@xxx"
                }
                rsp=requestts,get("http://www.baidu.com",proxies=proxy)
        
      -web客户端验证
        -如果遇到web客户端验证，需要添加auth=（用户名.密码）
             auth={"test1","123456"}#授权信息
             rsp=requests.get("http://www.baidu.com",auth=auth)
      -cookie
        -requests可以自动处理cookie信息
                rsp=requests.get("xxx")
                #如果对方服务器传送过来cookie信息，泽科一通过反馈的cookie属性得到
                 #返回一个cookiejar实例
                 cookiejar=rsp.cookies
                 #可以讲cookie转换为字典
                 cookiedict=requests.utils.dict_from_cookiejar(cookiejar)
         -session
            -跟服务器端sesion不是一个·东西
            -模拟一个会话,从客户端浏览器服务开始，到客户端浏览器断开
            -让我们跨请求时保持某些参数，比如在同一个session实例发出的所有请求之间的cookie
               #创建session对象，可以保持cookie值
               ss=requests.session()
               headers={"uesr-agent":"xxx"}
               data={
               "name":"xxx"
               }
               #此时，由于创建的session管理请求，负责发出请求
               ss.post（"http://www.baidu.com",data=data,headers=headers）
               rsp=ss.get("xxx"
               )
             -https请求验证ssl验证
                -参数verify负责表示是否需要验证ssl证书，默认是true
                -如果不需要ssl验证,则设置成false
                -rsp=requests.get（"https://www.bai.com",veriff=false）
 
 
 #页面解析和数据提取
 -结构数据
    -json文件
    -json path
    -转换成pyhton类型进行操作
    -转转成python类型进行操作(json)
    -xml文件
        -转换成python类型
        -xpath
        -正则
 -非结构化数据:先有数据,再谈结果
    -文本
    -电话号码
    -邮箱地址
    -html文件
        -正则
        -xpath
        -css选择器
        -
#正则表达式
    -一套规则，可以在字符串文本中进行搜索替换等
    -案例v1,re的基本使用流程
    -案例v2,match的基本使用
        -match：从开始位置查找，一次匹配
        -search：从任何位置查找，一次匹配
        -findall:全部匹配
        -finditer：全部匹配，返回迭代器
           -split:分割字符串,返回列表
           -sub替换
#贪婪模式与非贪婪模式
    -贪婪模式:在整个表达式匹配的前提下，尽可能多的匹配
    -非贪婪模式:xxxxx,尽可能少的
    -python里面数量词默认是贪婪模式
        例如:
            -查找文本abbbb
            -re是 ab*
            -贪婪模式:结果还是abbbb
            -非贪婪模式:结果是a
     #xml
        -xml
        -http
        案例v4
        概念:父节点。子节点，仙贝节点，兄弟节点，后代节点
      #xpath
      
     #lxml
     -python的html/xml的解析器
    -官方文档
        http://lxml.de/index.html
     -功能：
        -解析html,案例v29,py
        -文件读取，案例v30.html,v31.py
        -etreee和xpath的配合使用，案例v32.py
   #css选择器 BeautifulSoup4 
  现在是用beayutifulsoup
  http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
  几个常用的提取信息工具的比较:
        正则:很快，不好用，不许安装
        -beutifulsoup：慢，使用简单，安装简单
        -lxml：比较快，使用简单，安装一般
   -案例v32.py
 -四大对象
    -   Tag
    -NavigabelString
    -Beautifulsoup
    -commment
  -Tag
    对应html中的标签
    -对应通过soup。tag_name
    -案例a33
    
  -beautifulsoup
    -表示的是一个文档的内容,大部分可以当做是tag对象
    -一般我们可以用soup来表示
   
   
   -commment
    -特殊类型的navagablestring对象
    -对其输出,则内容不包括注释符号
  -遍历文档对象
    -contents:tag的子节点以列表的方式给出
    -children：子节点以迭代器输出
    -descendants：所有子孙节点
    -string
    -案例
    
  -css选择器
    -使用soup.select，返回一个列表
    -通过标签名称：soup.select("title")
    -通过类名:soup.select(".content)
    -通过id查找soup。select("#name_id)
    -组合查找:soup.select(div #input_content)
    -属性查找:soup.select(img[class='photo'])
    -获取tag内容:tag.get_text（案例v6）
    
    
        
    
    
  
    
    
   
    
    
   
  
  
  
   
   
   
   
   
   
     
     
           
           
    
    
               
                
    
    
        
    
            
            
            
            
            
    
    
        
    
    