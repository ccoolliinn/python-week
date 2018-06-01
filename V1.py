import urllib.request
if __name__=='__main__':
    url= 'https://blog.csdn.net/u010211479/article/details/66475183'
    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("URl: {0}".format(rsp.geturl()))
    print("code: {0}".format(rsp.getcode()))
