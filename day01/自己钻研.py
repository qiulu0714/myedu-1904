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
a = ['爱奇艺',54,758,'优酷','腾讯','爱奇艺',54,758,'优酷','腾讯','熊猫tv','斗鱼tv',15515]
def list_type():
    print(a)
    b = a [2:4]
    print(b)
    c = len(a)
    print(c)
    d = a.count('优酷')
    print(d)
    a.append('斗鱼TV')
    print(a)
    e = ['512','585','695']
    a.extend(e)
    print(a)
    a.append(e)
    print(a)
# 新建一个字典变量,里面有两个键值对,访问一个值,
# 删除一个键值对,添加一个键值对,更改任意一个值,
# 再新建一个字典,将两个合并 ;

def dict_type():
    adict = {"username": "admin", "password": "123456"}
    print(adict)
    print(adict['username'])
    adict.pop ('username')
    adict['商品'] = '华为'
    adict['商品']=('荣耀')
    bdict = { 'list': ['爱奇艺','腾讯'] ,'tuple':(1,65,125)}
   # cdict = dict(adict,**bdict)
    adict.update(bdict)
    print(adict.update(bdict))
if __name__ == '__main__':
    # list_type()
# python 的运行环境是Python解释器
# Python 的编写代码的工具有pycharm,专业名字叫做pycharm编辑器,或者集成开发工具
# 变量名 = 变量
# def 方法名():  ; 带参数: def 方法名 (a,b ,c ,...)
# if __name__ == '__main__': ;  可以直接执行  ; main下面不能添加其他方法
# return 主要是给方法名()中的括号赋值,如果不加 ()中的值为Nome
    dict_type()

