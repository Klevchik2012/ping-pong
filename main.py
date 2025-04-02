from pygame import *
from ball import Ball
from const import *
from game_sprite import *
from player import Player


# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()

# название окна
display.set_caption("Догонялки")

player_left = Player(BAGET_IMG,5,(WIN_H - BAGET_H)/2, BAGET_W,BAGET_H)
# 
player_right = Player(BAGET_IMG,WIN_W - BAGET_W -5,(WIN_H - BAGET_H)/2, BAGET_W,BAGET_H)
players = sprite.Group()
players.add(player_left)
players.add(player_right)
cheese = Ball(CHEESE_IMG,(WIN_W - CHEESE_W)/2,(WIN_H - CHEESE_H)/2, CHEESE_W,CHEESE_H)

font.init()

title_font = font.SysFont('arial',70)
win_left = title_font.render('выиграл левый игрок', True, DARC_BLUE)
win_right = title_font.render('выиграл правый игрок', True,DARC_BLUE)

# игровой цикл
game = True
while game:
    window.fill(LIGHT_BLUE)

    players.draw(window)
    cheese.draw(window)
    player_left.update(K_w,K_s)
    player_right.update(K_UP,K_DOWN)
    cheese.update()

    if sprite.spritecollide(
            cheese, players, False
        ):
        cheese.speed_x *= -1

    if cheese.rect.right > player_right.rect.x:
        window.blit(win_left,(100,200))
        finish = True
        display.update()

    if cheese.rect.x < player_left.rect.x:
        window.blit(win_right,(100,200))
        finish = True
        display.update()
    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)
