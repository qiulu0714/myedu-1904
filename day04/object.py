class SF () :
    def __init__(self ,name ,kc, fs ):
        self.nmae = name
        self.kc = kc
        self.fs = fs

    def eat(self):
        print(self.nmae+ '吃午餐')
    def sleep(self):
        print(self.nmae+ '睡觉')

    def xsxx (self ):
        print('姓名:%s ,课程:%s ,成绩 : %s'% (self.nmae ,self.kc,self.fs))

class TX(SF) :
    def eat(self):
        print(self.nmae +'吃火锅')
        self.sleep()
        self.xsxx()



class JD(SF):
    def __init__(self ,name ,kc, fs ,sp):
        self.nmae = name
        self.kc = kc
        self.fs = fs
        self.sp = sp

    def eat(self):
        print(self.nmae + '吃乡村基')
        self.sleep()

    def xsxx (self ):
        print('姓名:%s ,课程:%s ,成绩 : %s ,商品:%s'% (self.nmae ,self.kc,self.fs,self.sp))
if __name__ == '__main__':
    # student = SF ('马云','信息技术',85)
    # student.xsxx()
    # student.eat()
    # info = SF ('马化腾','腾讯',85)
    # info.eat()
    # info.sleep()
    # info.xsxx()
    inno = JD ('刘强东','京东',85,'手机')
    inno.eat()
    inno.sleep()
    inno.xsxx()

