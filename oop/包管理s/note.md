 #如何使用模块
 模块直接导入
  语法
      import  module_name
      module_name.function_name
      module_name.class_name
    import 模块 as 别名
        导入的同时给hi给模块起一个别名
        其余用法跟第一个相同
     form module_name import func_name,class,class_name
        按上述方法有选择
         案例p04
     from module_name import *
        导入模块的所有内容
2、模块的搜索路径和存储
    加载模块的搜索路径,系统会在那些模块寻找此模块
   系统默认的模块搜索路径
            import sys
            sys.path属性可以获取路径列表
            #案例 p06.py
   添加搜索路径
        sys.path.append(dir)
    模块的加载顺序
        1、搜索内存中已经存在的模块
        2、搜索pythom的内置模块
        3、搜索sys.path路径
   #包的导入操作
            import package_name
                直接导入一个包。可与使用__init__.py中的内容、
                使用方式是:
                    package_name.func_name
                    package_name.class_name.func_name()
                  此种方式的访问内容是
                  案例 pkg01,p07.py
            import package_name as p
            
            import package.module
                导入包中的某一个具体的方式i
                
               
   
   
      
        
