'''
验证哥德巴赫猜想：
实现一段代码，输入一个大于 2 的偶数 k，输出两个质数 m、n，满足 m + n == k。
组合有很多，仅输出一对。
'''
def Iszhishu(n):
    a=[]
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)
    if len(a)==2:
        return  True
def Goldbach(n):
    if int(n)<=1 or int(n)%2!=0:
        print("请输入大于2的偶数")
    else:
        for i in range(1,round(int(n)/2)):
            if Iszhishu(i) and Iszhishu(int(n)-i):
                print(n,"=",i,"+",int(n)-i)
                break
    return 0
n=input()
Goldbach(n)
