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
    
            
            
            
            
            
    
    
        
    
    