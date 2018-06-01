#request.data使用
#get或post 访问网络
import urllib.request
import urllib.parse
if __name__=='__main__':
    url= 'http://www.baidu.com/s?'
    wd= input("Input your key word: ")

    #使用data要用字典结构
    qs={"wd":wd}
    #转换url编码
    qs= urllib.parse.urlencode(qs)
    fullurl= url + qs
    print(fullurl)
    rsp = urllib.request.urlopen(fullurl)
    html=rsp.read()

    html=html.decode()
    print(html)

