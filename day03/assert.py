if __name__ == '__main__':
   a = (13)
   b = ['哎哟诶',13]
   try:
        assert a in b
        print('正确的')
   # assert a not in b
   except :
       print('报错啦')
