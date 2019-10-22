#findall案例
#正则表达式
import re
#匹配整数
pattern=re.compile(r'\d+')
s=pattern.findall("i am 12 years o;dmand 185 high")
print(s)
s=pattern.finditer("i am 18 years old and 185 high")
print(type(s))
for i in s:
    print(i.group())


