from urllib import request
import ssl
#导入python ssl处理模块（安全操作）
#利用非认证上下环境替换认证的向下文环境
ssl._create_default_https_context=ssl._create_default_https_context
url="https://www.12306.cn/mormhweb/"
rsp=request.urlopen(url)
html=rsp.read().decode()
print(html)