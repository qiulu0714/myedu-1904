def AVG():
    a = 47
    b = 95
    c = a*b
    print(c)
def bmi():
    height = 1.7
    weight = 67.5
    bmi = (weight / (height * 2))
    if bmi < 18:
        print('过轻')
    elif bmi < 25:
        print('正常')
    elif bmi < 28:
        print('超重')
    elif bmi < 32:
        print('肥胖')
    else:
        print('超级胖')
def int_name():
    a = 23
    print(type(a))
    a = str(a)
    print(type(a))
def str_name():
    a = '45'
    print(type(a))
    print(type(int(a)))
def float_name():
    a = 13.42
    print(a)
def join_name():
    a = 'jks'
    b = '爱奇艺'
    c = 525
    e = a + b
    print(a+b)
    print(e)
    f = a + str(c)
    print(f)
    print('%s%s'%(a,c))
def add(m,n):
    print(m)
    print(n)
    print(m + str(n))
    return m + str(n)
def aiqiyi_name(a ,b):
    print(a)
    print(b)
    d = a + b
    return d
if __name__ == '__main__':
    f = aiqiyi_name('爱奇艺','腾讯')
    print(f)
    print(type(f))
# python 的运行环境是Python解释器
# Python 的编写代码的工具有pycharm,专业名字叫做pycharm编辑器,或者集成开发工具
# 变量名 = 变量
# def 方法名():  ; 带参数: def 方法名 (a,b ,c ,...)
# if __name__ == '__main__': ;  可以直接执行  ; main下面不能添加其他方法
# return 主要是给方法名()中的括号赋值,如果不加 ()中的值为Nome


