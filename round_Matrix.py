'''
输入一个正整数 N，输出以 N 为边长的螺旋矩阵。（比如下图就是 N 为 4 的结果）
 1   2   3   4
12  13  14   5
11  16  15   6
10   9   8   7
'''
class Matrix:
    def __init__(self,N):
        #构造二维数组
        self.matrix=[[None for i in range(N)] for j in range(N)]
        #初始行列数
        self.row=0
        self.col=0
        #数组边界值
        self.max_row=N
        #用来标记换方向的标志位
        self.mark=0
    #数组运动方向
    def direction(self,mark):
        around = [
            [self.row, self.col+1], # 向右
            [self.row+1, self.col], # 向下
            [self.row, self.col-1], # 向左
            [self.row-1, self.col]  # 向上
        ]
        return around[mark%4]
    # 针对目前位置，获取下一位置的行列数
    # 下一位置为边界则更换方向
    # 下一位置已经有元素则更换方向
    def next(self):
        # 下一位置
        i = self.direction(mark=self.mark)
        # 判断是否更换方向，不更换则更新 self.row / self.col
        if -1 not in i and self.max_row not in i:
            if self.matrix[i[0]][i[1]] is None:
                self.row,self.col = i
                return None
        # 更换方向
        self.mark += 1
        return self.next()
    def solution(self):
        # 逐一取出 1 到 n^2 值
        for i in range(1,self.max_row**2+1):
            # 按行列赋值
            self.matrix[self.row][self.col] = i
            # 退出条件
            if i == self.max_row**2:
                break
            # 更新行列值
            self.next()
        # 打印结果
        for r in self.matrix:
            for c in r:
                print('{0:^4}'.format(c), end='')#^、<、>分别是居中、左对齐、右对齐，后面带宽度
            print('\n')
if __name__ == '__main__':
    n = int(input('n='))
    s = Matrix(n)
    s.solution()