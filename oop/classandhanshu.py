class Teacher():
    name="data"
    age=19
    def say(self):
        self.name="zgahangxign"
        self.age=23
        print("my name iss {0}".format(self.name))
        print("my age is {0}".format(self.age))
    def sayAgain():
        print(__class__.name)
        print( __class__.age)
        print("hello,noce to meet you")
t=Teacher()
t.say()
Teacher.sayAgain()

#关于self的案例（构造函数）
class A():
    name="zhangxing"
    age=18
    def __init__(self):
        self.name="aaaa"
        self.age=200
    def say(self):
        print(self.name)
        print(self.age)

class B():
    name="bbb"
    age=90
a=A()
a.say()
#此时，传入的是类实例B,因为B具有name和age类型，所以不会报错

A.say(B)
#以上代码，利用了鸭子模型
#面向对象三大特性
 #封装
 #继承
 #多态
 #继承就是一个类可以获得另外一个类中的成员的属性和成员方法
 #作用:减少代码，增加代码的复用功能
class Pesrson():
    name="zhangxing"
    age=0
    def sleep(self):
        print("sleeping")
    def work(self):
        print("make money")
class Teacher(Pesrson):
    teacher_id="20197305"
    name="limignliag1"
    def make_test(self):
        print("attention")
    def work(self):
        Pesrson.work(self)
        self.make_test()
t=Teacher()
print(t.name)
print(Teacher.name)
t.sleep()
t.make_test()
#子类和父类定义同一个变量,则优先使用子类本身
#子类扩充父类功能




