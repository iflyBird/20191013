#正则表示是的使用案例
import re
s=r'([a-z]+) ([a-z]+)'
pattern=re.compile(s,re.I)#s.i表示忽略大小写
m=pattern.match("hello world wide web")
#group表示返回匹配的整个子串
s=m.group(0)
print(s)
a=m.span(0)#返回匹配成功的整个字符串
print(a)
#group(1)表示返回得第一个分组匹配的字符串
s=m.group(1)
print(s)
a=m.span(1)
#返回匹配成功的第一个子串的跨度
print(a)
s=m.groups()#等价于m.group(1),m.group(2)
print(s)
#参数表明搜查的其实范围
m=pattern.search("one12tw34three56",10,40)
print(m.group)


