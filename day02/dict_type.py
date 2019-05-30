# 字典类型(键值对/json/xml)用{ }包起来,前面是 key ,后面是 value ,多组键值对用 ,隔开;
# 字典类型是无序的,没有索引,只能通过 key ,来访问 value ,并且 key 不能重复 ;
adict = {"username":"admin","password":"123456"}
def dict_type():
    print(adict["username"])
def dict_update():
    adict["username"] = 'aiqiyi'
    print(adict)
def dict_delete():
    adict.pop('username')
    print(adict)
def dict_add():
    bdict = {'list': ('爱奇艺','腾讯'),'tuple': (1,2,6,46)}
    adict.update(bdict)
    print(adict)
    cdict = {'password':'19526','height':'170cm','weight':'67'}
    ddict = dict(adict,**cdict)
    print(ddict)
if __name__ == '__main__':
    dict_add()