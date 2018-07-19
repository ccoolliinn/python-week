# 罗马数字转整数
def RomantoInt(s):
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res, p = 0, 'I'
    # 逆序逐一遍历
    # 使用逆序的好处在于，每次只需对一位罗马数字进行加或减的操作
    # 使用顺序的话，可能为两位
    for c in s[::-1]:#s[::-1]含义是s逆序，也就是从最后一个元素到第一个元素
        if d[c]<d[p]:
            res=res-d[c]
        else:
            res=res+d[c]
        p=c
    print(res)
    return res

# 整数转罗马数字
def IntToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    # 迭代依次处理每位数字
    res, i = "", 0
    while num:
        # //是取整除的商，%是取余数  举例：10除以3=3余1，则10//3=3,10%3=1
        res += (int(num) // values[i]) * numerals[i]
        num = int(num)%values[i]
        i += 1
    print(res)
    return res
s=input()
IntToRoman(s)