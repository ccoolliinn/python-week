'''
    最近流行起一种奇怪的流感，称作蜥蜴流感，虽不致命，但需隔离治疗。关于这种流感，我们已经通过大量统计得知以下事实：

        总人口中有1%的人患有蜥蜴流感

        若某人已患蜥蜴流感，诊断结果为阳性的概率为90%

        若某人未患蜥蜴流感，诊断结果为阳性的概率为9%

    如果现在你的诊断结果为阳性，那么你实际患病的可能性有多大？
    用程序模拟一场蜥蜴流感。
    比如有10万个人，按照上述3条规则去模拟，最后去统计下检测结果阳性中有多少人是真正的患者。
'''
#利用random模块来模拟,random.random()产生（0,1）之间的随机浮点数
import random
#定义一个类，表示某个个体
class Man:
    flu=False#是否患病
    text=False#是否阳性
# 产生10万个体，随机患病和检测状况
all_people=[]
for i in range(1,100000):
    m=Man()
    #患病概率
    if random.random()<0.01:
        m.flu=True
    #真阳性概率
    if m.flu and random.random()<0.9:
        m.text=True
    #假阳性概率
    if not m.flu and random.random()<0.09:
        m.text=True
    all_people.append(m)
#统计个数
positive_people=[m for m in all_people if m.text]#阳性人群
print(len(positive_people))
positive_flu=[m for m in all_people if m.flu]#实际患者
print(len(positive_flu))
#实际患者在阳性中所占比例
print(len(positive_flu)/len(positive_people))