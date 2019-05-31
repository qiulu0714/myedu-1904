def home_work1(a):
    for i in range(1,51):
        if i%2==1 :
            a = a +i
    return print(a)
def home_work2():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s*%s=%s'%(i,j,i*j),end=' ')
        print(' ')
def home_work3():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s+%s=%2s'%(i ,j,i+j),end=' ')
            print('')
def home_work4():
    a = 72
    for i in range(72,88):
        if i%2==0 :
            a = a+i
    return print(a)
def home_work5():
    for i in range(1,1001):
        if i % 4 == 1 and i % 5 == 4 and i % 6 == 3 and i % 7 == 5 \
                and i % 8 == 1 and i % 9 == 0:
            print(i)
def home_work6():
    a = 0
    for i in range(1,51,2):
        print(i)
        a = a + i
        return a

if __name__ == '__main__':
    # home_work1(0)
    # home_work2()
    # home_work4()
    home_work6()