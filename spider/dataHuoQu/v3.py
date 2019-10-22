#中文匹配
import re
hello=u'你好，世界'
patter=re.compile(r'[\u4e00-\u9fa5]+')
m=patter.findall(hello)