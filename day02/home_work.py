# 新建一个字典变量,里面有两个键值对,访问一个值,
# 删除一个键值对,添加一个键值对,更改任意一个值,
# 再新建一个字典,将两个合并
adict = {"username":"admin","password":"123456"}
def dict_Type():
    bdict=adict.pop("username")
    print(adict)
    adict['会员']= 'vip'
    adict['password']=('14526')
    print(adict)
    cdict = {'视频':'爱奇艺'}
    ddict = dict(adict,**cdict)
    print(ddict)
if __name__ == '__main__':
    dict_Type()