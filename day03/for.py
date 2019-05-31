def for_demo1():
    for i in range (5):
        print('世界,你好')
        print(i)
def for_demo2(a):
    for i in range(50):
        a+=1
        print(a)
        print(i)
def for_demo3(b,c):
    for i in range(4):
        b*=2
        c*=2
        print(b)
        print(c)
def for_demo4():
    alist = ['a','nb','sb','zz']
    for i in alist:
        print(i)
    for i in range(len(alist)):
        print(alist[i])

def for_demo5():
    for i in range(3):
        print('你好')
        for j in range(2):
            print('世界')

if __name__ == '__main__':
    for_demo5()
