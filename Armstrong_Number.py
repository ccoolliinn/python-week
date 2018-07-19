'''
如果一个正整数等于其各个数字的立方和，则称该数为阿姆斯特朗数（亦称为自恋数、自幂数）。
如 407 = 4^3 + 0^3 + 7^3 就是一个阿姆斯特朗数。
1、写一段代码，输出 1000 以内的所有阿姆斯特朗数。
2、附加题：输入一个正整数，输出距离它最近的阿姆斯特朗数。
'''

#写一个判断是否为阿姆斯特朗数的函数
def IsArmstrong(num):
    a=sum(int(x)**3 for x in str(num))#求和的方式需要记住
    if a==num:
        return True
    else:
        return False
#输出 1000 以内的所有阿姆斯特朗数
def Armstrong_1000():
    print("1000以内的阿姆斯特朗数有：")
    for i in range(1,1001):
        if IsArmstrong(i):
            print(i)
    return 0
#附加题：输入一个正整数，输出距离它最近的阿姆斯特朗数。
def near_Armstrong():
    print("请输入一个正整数num：")
    num=int(input("n= "))
    if num<=0:
        print("num应该为正整数！")
    while True:
        if IsArmstrong(num-1):
            a=num-1
            break
        num-=1
    while True:
        if IsArmstrong(num):
            b=num
            break
        num+=1
    if abs(num-a)>=abs(num-b):
        print(b)
        return b
    else:
        print(a)
        return a
Armstrong_1000()
near_Armstrong()

