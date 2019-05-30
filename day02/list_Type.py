alist = ['爱奇艺',54,758,'优酷','腾讯','爱奇艺',54,758,'优酷','腾讯','熊猫tv','斗鱼tv',15515]
def list_Tpye():
    print(alist[3])
    print(alist[2:6])
    print(alist[-3])
    print(alist[::-1])
def listpop_Type():
    print(alist.pop(2))
    print(alist)
def listappend_Tpye():
    alist.append('熊猫TV')
    alist.append('斗鱼TV')
    print(alist)
def listextend_Tpye():
    blist = ['杰克','玛丽','和尚','尼姑']
    alist.extend(blist)
    print(alist)
    alist.append(blist)
    print(alist)
def listorder_by():
    blist = [88,256,49,16,583]
    blist.sort()
    print(blist)
    blist.sort(reverse=True)
    print(blist)
def list_distinct():
    blist = list(set(alist))
    print(blist)
def add_Tpye(m,n):
    print(m+n)
    return m+n
def listupdate_Type():
    alist[2] = '虎牙TV'
    print(list)
def listlen():
    print(len(alist))
    print(alist)
def listcount():
    a = alist.count('爱奇艺')
    print(a)
if __name__ == '__main__':
    list_distinct()