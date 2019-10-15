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
#继承中的构造函数


# __init__就是构造函数
#每次实例化的时候，第一个被自动的调用
#因为主要工作是进行初始化，所以得名
class Animel():
    pass
class PaxingAni(Animel):
    def __init__(self):
        print("paxing Dongwu")
class Dog(PaxingAni):
    def __init__(self):
        print("I am init in dog")
kaka=Dog()
class Cat(PaxingAni):
    pass
#猫没有写构造函数
#此时应该自动调入构造函数，因为cat没有构造函数，所以查找父类构造函数
class Cat(PaxingAni):
    pass
c=Cat()

#单继承和多继承
    #单继承：每个类类只能继承一个类
    #多继承：每个类鱼鱼继承多个类
#单继承和多继承的优缺点
    #单继承:
        #继承有序逻辑清晰语法简单隐患少呀
        #功能不能无线扩展，只能在当前唯一的继承连中扩展
    #多继承:
        #类的功能扩展方便
        #继承关系混乱
class Fish():
    def __init__(self,name):
        self.name=name
    def swim(self):
        print("i am swiming")
class Bird():
    def __init__(self,name):
        self.name=name
    def fly(self):
        print("I am fltign")
class Person():
    def __init__(self,name):
        self.name=name
    def workd(self):
        print("working..../")
        #继承（多继承）
class SuperMan(Pesrson,Bird,Fish):
    def __init__(self, name):
        self.name = name
s=SuperMan("zhangxing")
s.fly()
s.work()
s.swim()
#构造函数的调用顺序
    #中想扩展b的构造函数,即调用b的构造函数后添加一些功能
    #由俩种方法实现
#此时先查找c的构造函数，
#如果没有，则向上按照mro顺序查父类的构造函数,直达找到为止.
class A():
    def __init__(self):
        print("A")
class B():
    def __init__(self,name):
        print("B")
        print(name)
class C(B):
    def __init__(self,name):
        B.__init__(self,name)
        print("这是c中的功能")
#多态
    #多态就是同一个对象在不同的情况下有不同的状态出现
    #多态不是语法，是一种设计思想
    #多态性:一种调用方式，不同的结果
    #同一事物的多种形态,动物分为人类，狗类，猪类
    #mixin设计模式

























