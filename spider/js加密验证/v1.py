#1、这个是计算salt中的公式r=""+((new Date).getTime()+parseInt(10*Math.randow(),10)))
#2、sigh:n.md5一共需要四个参数，第一个和第四个都是固定值的字符串，第三个是所谓的salt，d
#第二个参数就是要查找的单词
#未完待续
def getSalt():
    import time,random
    salt=int(time.time()*1000)+random.randint(0,10)
    return salt
def getMd5(v):
    import  hashlib
    md5=hashlib.md5()
    md5.update(v,encoding="utf-8")

