
'''
题目描述：    
    在一个宾馆里住着六个不同国籍的人，他们分别来自美国、德国、英国、法国、俄罗斯和意大利。
    他们的名字叫 A、B、C、D、E、F。名字的顺序与上面的国籍不一定相互对应。

    A 和美国人是医生

    E 和俄罗斯人是教师

    C 和德国人是技师

    B 和 F 曾经当过兵，而德国人从未参过军

    法国人比 A 年龄大，意大利人比 C 年龄大

    B 同美国人下周要去西安旅行，而 C 同法国人下周要去杭州度假

通过上述描述，判断 A、B、C、D、E、F 各是哪国人？
'''
import  itertools
countries=['USA','Germany','England','France','Russia','Italy'];
persons=['A','B','C','D','E','F'];
#itertools.permutations是进行排列组合，找到满足的位置，排除法
for res in itertools.permutations(persons, 6):
    # A,E,C不是美国人，俄国人，德国人
    if res[0] in 'AEC' or res[4] in 'AEC' or res[1] in 'AEC':
        continue
    # B,F不是德国人
    if res[1] == 'B' or res[1] == 'F':
        continue
    # A不是法国人，C不是意大利人
    if res[3] == 'A' or res[5] == 'C':
        continue
    # B不是美国人，C不是法国人
    if res[0] == 'B'or res[3] == 'C':
        continue
    #zip是将数据打包成元祖的形式输出
    print(sorted(zip(res, countries), key=lambda t: t[0]))
