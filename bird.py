

class Bird():
    def __init__(self,x=200,y=160):
        self.x = x  # 初始横坐标位置
        self.y = y  # 初始纵坐标位置
        self.t = 0  # 掉落时间计时
        self.n = 0  # 跳跃间隔控制参数，最大值为3
        self.size = [12,8]  # 小鸟的尺寸
        self.IsJumping = False  # 记录小鸟的跳跃状态

    def jump(self):
        self.y -= 15-3*self.n  # 基本公式
        self.n += 1     # 跳跃步数增加
        if self.n == 5:
            self.IsJumping = False
            self.n = 0

    def fall(self):
        if not self.IsJumping:  # 判定是否处于跳跃状态
            y = 2+5*self.t**2   # 基本公式，前面的2为人为设定的速度偏移量，后面则是房重力
            self.y += y         # 对小鸟的纵坐标进行位移增加




