from pygame import *
from const import WIN_H
from game_sprite import  GameSprite

class Player(GameSprite):
    def __init__(self,img,x,y,width,height,speed = 3):
        super().__init__(img,x,y,width,height,)
        self.speed = speed

        
    def update(self):
        keys = key.get_pressed()
        if self.rect.y > 0 and keys[K_w]:
            self.rect.y -= self.speed
        if self.rect.y < WIN_H - self.rect.height and keys[K_s]:
            self.rect.y += self.speed
            