'''
星期五和数字13都代表着坏运气，两个不幸的个体最后结合成超级不幸的一天。
所以，不管哪个月的13日，如果恰逢星期五就叫“黑色星期五”。
找出一年中哪些日子是“黑色星期五”??
【已知条件】2017年1月1日是星期日
【要求】输入2017之后任意年份，输出该年包含黑色星期五的具体日期
'''
from datetime import date
def black_Friday(year):
    year = input("查询年份： ")
    year = int(year)
    if year < 2017:
        print("请输入2017以后的年份")
        return 0
    days = [date(year, i, 13) for i in range(1, 13)]
    fridays=[str(i) for i in days if f'{i:%a}'=='Fri']
    print('黑色星期五：\n{}'.format("\n".join(fridays)))

black_Friday(2016)
