def if_demo():
    a = 54 == 54
    if a :
        print('a是正确的')
    else:
        print('a是错误的')
def if_demo2():
    a = 23
    if a >= 11 :
       print('恭喜你小学毕业')
    elif a > 14 :
       print('你初中毕业啦')
    elif a > 17 :
        print('你高中毕业啦')
    else:
        print('你大学毕业啦 ,你将步入社会啦')

if __name__ == '__main__':
    if_demo2()