
a = '爱奇艺'
def var_demo1():
    b= '腾讯'
    print(a)
def var_demo2():
    print(b)
def var_demo3():
    global a
    a = '优酷'
    print(a)
if __name__ == '__main__':
    var_demo1()
    var_demo2()
    # var_demo3()
    var_demo1()