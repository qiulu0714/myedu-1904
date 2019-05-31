import os
if __name__ == '__main__':
    pwd = os.getcwd()
    print(pwd)
    cd = os.path.abspath('..')
    print(cd)
    cd2 = os.path.abspath('../..')
    print(cd2)