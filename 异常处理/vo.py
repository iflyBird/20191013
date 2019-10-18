# #打开文件
# #W文件成为句柄
# f=open(r"test01.txt",'w')
# f.close()
# #此案例说明，以写方式打开文件，默认驶入过没有文件，则创建
# #with语句
# with open(r"test01.txt",'r') as f:
#     pass
# #with案例
#   #按行读取文件。
# with open(r'test01.txt','r') as f:
#
#     strline=f.readline()
#     while strline:
#         print(strline)
#         strline = f.readline()
# #list能用打开的文件作为参数，把文件内每一行内荣作为一个参数
# with open(r'test01.txt','r') as f:
#     l=list(f)
#     for line in l:
#         print(line)
with open(r'C:/Users/zhangxing/PycharmProjects/20191013/异常处理/test01.txt','r') as f:
    strChar=f.read(1)
    print(len(strChar))
   # print(strChar)

#seek(offset,from)
    #移动文件的读取位置，也叫读取指针
    #从文件当前位置开始偏移
    #从文件末尾开始偏移
    #seek案例
    #打开位置后，从第五个字节开始读取
    #打开读写指针在0处，即文件的开头
    # seek移动单位是字节
    #seek移动单位是字节
#     with open(r'test01.txt','r'):
#         f.seek(6,0)
#         strChar=f.read()
#         print(strChar)
# #让程序暂停，可以使用time下的sleep函数
# import time
# with open(r'test01.txt','r') as f:
#     strChar=f.read(3)
#     while strChar:
#         print(strChar)
#         time.sleep(1)
#         strChar=f.read(3)
#
#







