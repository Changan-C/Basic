#面向过程

stu1 = {'name': 'xiaohong', 'score':89}
stu1 = {'name': 'xiaobai', 'score':81}

def print_score(stu):
    print('%s:%s'%(stud['name']),stu['score'])

#面向对象
# 1.设计类
# 属性和方法

class Student(object): #类名 开头大写+括号冒号
  #  pass#占位
    def __init__(self,name,score): #属性
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s'%(self.name, self.score))
#实例化对象  每次实例化相当于重新分配一次地址
xiaohong = Student('xiaohong',98)
print(id(xiaohong))
xiaobai = Student('xiaobai',81)
print(id(xiaobai))
#xiaohong.print_score()

'''
继承，封装，多态
'''
class Student(object): #类名 开头大写+括号冒号  封装
  #  pass#占位
    def __init__(self,name,score): #属性
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s'%(self.name, self.score))
    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'
xiaolv = Student('xiaolv',45)
print(xiaolv.get_grade())

'''
访问限制
'''
xiaolv.score = 90    #此处能被随意改动
print(xiaolv.get_grade())

class Student(object): #类名 开头大写+括号冒号
  #  pass#占位
    def __init__(self,name,score): #属性
        self.__name = name #两个下划线，变成私有
        self.__score = score
    def print_score(self):
        print('%s:%s'%(self.__name, self.__score))
    def get_grade(self):
        if self.__score >=90:           #两个下划线私有化
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return
    def set_score(self,score):
        if 0<=score<=100:
            self.__score =score
        else:
            raise ValueError('error score')
#    def set_score(self,score):
#        self.__score
    def get_score(self):
        return self.__score
xiaolv = Student('xiaolv',45)

print(xiaolv.set_score(80))  #???????????????????????????????????
print(xiaolv.get_score())   #为什么输出还是45

#python 没有真正的私有化，把私有改名陈_Steudent__name
print(xiaolv._Student__name)