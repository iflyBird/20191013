#使用需要先导入
import calendar
cal=calendar.calendar(2017)
print(type(cal))
cal=calendar.calendar(2019,l=0,c=5)
print(cal)
#lendatys：获取某一年是否是润年
calendar.isleap(2001)
calendar.leapdays(2001,2018)
#calendar.isleap(2001,2018)
m3=calendar.month(2018,3)
print(m3)
#time模块
##时间戳
    # 一个时间表示，根据不同的语言
    # utc时间，世界协调时间。
    # 时间元组
    #     一个包含时间内容的普通元组
import time
#打印时间戳
print(time.time())
t=time.localtime()
print(t.tm_hour)
lt=time.localtime()
ts=time.mktime(lt)
print(type(ts))
print(ts)
def p():
    time.sleep(2.5)
t0=time.clock()
p()
t1=time.clock()
print(t1 - t0)
#strftime：将时间元组转换为自定义的字符串格式
#datetime提供日期和时间的匀速和表示
import datetime
#datetime常见属性
#datetime.date：一个理想和的日期,提供year,month，day属性
from datetime import datetime
dt=datetime.date(2018,3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.now())
print(dt.fortimestamp(time.time()))









