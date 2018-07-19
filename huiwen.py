'''
给你一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n(5<=n<=54)。
按从小到大的顺序输出满足条件的整数。
'''
def reverse(num):
    return int(str(num)[::-1])
def accumulate(n):
    return sum([int(x) for x in str(n)])
n=input("n:")
for i in range(10000,999999):
    if i==reverse(i) and accumulate(i)==int(n):
        print(i)