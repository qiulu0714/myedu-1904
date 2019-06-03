from day01 import home_type
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
# a = ['爱奇艺',54,758,'优酷','腾讯','爱奇艺',54,758,'优酷','腾讯','熊猫tv','斗鱼tv',15515]
# def list_type():
#     print(a)
#     b = a [2:4]
#     print(b)
#     c = len(a)
#     print(c)
#     d = a.count('优酷')
#     print(d)
#     a.append('斗鱼TV')
#     print(a)
#     e = ['512','585','695']
#     a.extend(e)
#     print(a)
#     a.append(e)
#     print(a)
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
def date_tyep():
    a = 12
    b = '会员'
    c = 12.32
    print(a,b,c)
# int转str类型 : a = str(a) , str 转 int 类型 : b = int(b)
# 不同数据类型之间的连接 :a = str(a)+b
    print(a)
def list_type():
    a = ['爱奇艺','腾讯','优酷',35,425]
    print(a[1])
    print(a[1:])
    print(a[::-1])
    a.append('hui')
    print(a)
    a.pop(1)
    print(a)
    a[1] = '23'
    print(a)
    b = ['亚索','小炮']
    a.extend(b)
    print(a)
def tuple_type():
    a = ('无极','武器','狮子狗' ,52)
    print(a)
def dict__type():
    a = {"username": "admin", "password": "123456"}
    print(a ['password'])
    a.pop('username')
    print(a)
    a['huiyuan'] = '腾讯'
    print(a)
    a['huiyuan'] = 'bilibili'
    print(a)
    b = {'lol':'英雄联盟','cs':'穿越火线'}
    a.update(b)
    print(a)
    c = {'你好':['无极'],'大家好': ('无极')}
    i = dict(a,**c)
    print(i)
def if_demo():
    a = 23
    if 6>=a<=11 :
        print('小学')
    elif 12>=a<=14 :
        print('初中')
    elif 15>=a<=17 :
       print('高中')
    elif 18 >=a <= 21 :
       print('大学')
    else :
       print('进入社会')


def return_demo(a,b):
    print(a)
    print(b)
    print(a*b)
    return a/b
if __name__ == '__main__':
    if_demo()
    # list_type()
    # tuple_type()
# date_tyep()
#     return_demo(25,43)
# # a = home_type.TEST_1()
# # print(type(a))
# # # python的运行环境叫什么?
# # python 解释器
# # # 写python代码的工具叫什么?专业名词是什么?
# # pycharm 集成开发工具/python编辑器
# # # 如何声明一个变量?
# #  变量名 = '变量'
# # # 如何声明一个普通方法?带参数的方法呢?
# # def 方法名():
# # # main方法怎么写?有什么特别?有什么限制?
# # # if __name__ == '__main__':
# # # 今天学了几个变量类型?分别都是什么?什么意思?
# # int str float nome list dict tuple
# # # 讲一下return是干嘛的?加不加有什么区别?
# # 方法执行到return 然后返回return后面的值
# # # 手写一种字符串拼接的方式?
# # a = 12 b = '爱奇艺' str(a) + b
# # # 如何调用其他模块的方法?
# # from 包名 import 文件夹
# # a= 文件夹.方法名