#借助于importlib包客户以实现导入以数字开头的模块名称
#相当于导入了一个叫01的模块并把导入模块赋值给了tuling
# import p01
# stu=p01.Student("zhangxing",19)
# stu.say()
# p01.sayHello()

import importlib
tuling=importlib.import_module("01")
stu=tuling.Student()
stu.say()
