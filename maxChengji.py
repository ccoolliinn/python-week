'''
        设定一个长度为 N 的数字串，将其分为两部分，找出一个切分位置，使两部分的乘积值最大，并返回最大值。
'''
def product1(num):
    numstr=str(num)
    length=len(numstr)
    max_num=0
    for i in range(1,length):
        #分别得到两边的数字串
        left=numstr[:i]#左边
        right=numstr[i:]#右边
        ans=int(left)*int(right)
        #更新最大值
        if  ans>max_num:
            max_num=ans
    return max_num

num=product1(1234)
print(num)

'''
  附加题：和原题一样求乘积最大，但输入的num可以打乱顺序。
  比如输入123，则132,231,……等也需要考虑，求最终的最大值。
'''
import itertools
def product2(num):
    numstr=str(num)
    length=len(str(num))
    max_num=0;
    for n in itertools.permutations(numstr):#permutations返回排列组合
        mixnumber=''.join(n)
        '''
        语法：  'sep'.join(seq)
        参数说明
        sep：分隔符。可以为空
        seq：要连接的元素序列、字符串、元组、字典
        '''
        #调用之前的函数
        ans=product1(int(mixnumber))
        if ans>max_num:
            max_num=ans
    return max_num
num1=product2(1234)
print(num1)