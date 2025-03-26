from game_sprite import *
from const import WIN_W, WIN_H

class Ball(GameSprite):
    def __init__(self,img,x=0,y=0,width= 50,height=50,speed=3):
        super().__init__(img,x,y,width,height,)
        self.speed_x = speed
        self.speed_y = speed

    def update(self):
        if self.rect.y < 0 or self.rect.y > WIN_H - self.rect.height:
            self.speed_y *= -1
        if self.rect.x < 0 or self.rect.x >WIN_W- self.rect.width:
            self.speed_x *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y