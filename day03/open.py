def open_w_a():
    w = open('ql.txt', 'w+')
    for i in range(5):
        w.write('爱奇艺\n')
    a = open('ql.txt', 'a+')
    for i in range(5):
        a.write('txx\n')
if __name__ == '__main__':


    r = open('ql.txt','r')
    print(r.readlines())
