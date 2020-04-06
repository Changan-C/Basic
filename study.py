print(abs(-20))
#内置函数
#查看帮组文档
help(abs)
#数据转化
print(float('123'))

#自定义函数

##def my_abs(x):
##    if x>=0;
 #       return x
##    else:
   #     return -x
from test_abs import my_abs
print(my_abs(-85))

#help 查看函数说明文档
help(my_abs)
#_doc_查看
#my_abs._doc_

#my_abs('asb')

#返回多值
def getNames():
    return 'yh','mike'
name1, name2 = getNames()
print(name1,name2)
t = getNames()
print(t)
print(type(t))

'''
默认参数
'''
def power(x):
    return x*x

def power(x , n=2):
    s=1
    while n>0:
            s= s*x
            n=n-1
    return s
    print(power(2,3))
    print(power(2))
    print(power(2,3))

'''
可变参数
'''
# n个数求和
def my_sum(numbers):
    sum = 0
    for n in numbers:
        sum= sum+n
    return sum
print(my_sum([4,5,6]))

def my_sum1(*numbers):
    sum = 0
    for n in numbers:
        sum= sum+n
    return sum
print(my_sum1(5,6,1))

#通过list 调用可变参数

nums = [1,2,3]
print(my_sum1(*nums))

#关键字参数
def student(name, age,**kw): #带两个**变成了可变参数
    print('name:',name,'age:','pthers:', kw)
student('yj',18,sex='male',region='chihna')

#通过字典传入
dicts= {'city': 'Beijing', 'sex':'female'}
student('mike',78,**dicts)

def student(name, age , **kw):
    if 'city' in kw:
        pass
    print('name:', name, 'age:',age,'others:',kw)
#空方法
def study():
    pass

def studen(name, age,*,city):
    print('name：', name, 'age:',age,'city:',city)

student('yh',78, city='Beijign' )

def f1(a, b, c=0, *args, **kw):
    pass
def f2(a,b,c=0,*,d,**kw):
    pass

#局部变量与全局变量
name = 'Zhangsan'

def fun():
    global name #局部定义为全局
    print('函数内输出全局变量', name)
    name = 'list'
    print('name=', name)
fun()
print('函数外输出', name)
