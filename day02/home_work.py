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
# 新建一个list变量,里面有五个元素,访问索引2,
# 切片访问索引1到4,删除索引3,添加两个元素,
# 第0位元素改成字符5,获取索引长度
alist = ['爱奇艺','腾讯','优酷',26,96]
def list_Type():
    print(alist[2])
    print(alist[1:4])
    alist.pop(3)
    alist.append('谷歌')
    alist.append('火狐')
    blist = ['谷歌','火狐']
    alist.extend(blist)
    alist[0]= '5'
    print(alist)
    print(len(alist))
if __name__ == '__main__':
    list_Type()