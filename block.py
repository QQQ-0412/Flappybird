import numpy as np
from PySide2.QtGui import QPixmap


class Block():
    def __init__(self,id,speed=3,width=480,height=512):
        self.id = id
        self.width = width
        self.height = height
        self.x = 570
        self.my_width = 60
        self.begin = 0
        self.space = 100
        self.speed = speed
        self.free = True
        self.img = [QPixmap(),QPixmap()]
        self.img[0].load("imgs/pipe.png")
        self.img[1].load("imgs/pipe_down.png")

    def move(self,bird):
        self.x -= self.speed
        if self.x < -self.my_width:
            self.free = True
        # 碰撞检测
        if (bird.x+bird.size[0] > self.x) and (bird.x < self.x+self.my_width):
            if bird.y - bird.size[1] < self.begin:
                return True
            elif bird.y + bird.size[1] > self.begin + self.space:
                return True
        return False

    def draw(self,my_painter):
        my_painter.drawPixmap(self.x, 0,self.my_width,self.begin,self.img[0])

        my_painter.drawPixmap(self.x,
                              self.begin + self.space,
                              self.my_width,
                              self.height-self.begin - self.space-112,self.img[1])

    def create(self):
        self.x = 570
        self.begin = 20+30*np.random.randint(0,11)
        self.space = 80 # 35 + 30 * np.random.randint(1, 3)
        self.free = False


