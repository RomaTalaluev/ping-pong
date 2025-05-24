
from time import time as TIME
from pygame import *
import pygame
class enemy(sprite.Sprite):
    def __init__(self,player_image,rect_x,rect_y,speed, size_x = 100, size_y=100):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class player1(enemy):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:

            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < wight - 290:
            self.rect.y += self.speed

class player2(enemy):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:

            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < wight - 290:
            self.rect.y += self.speed

        
            

class ball(enemy):
    def update(self):
        self.rect.y += self.speed
        global lose
        if self.rect.y > height:
            self.rect.x = randint(0,590)
            self.rect.y = 0
            lose += 1


pygame.init()
font = pygame.font.SysFont('Arial',50)
Game_over1 = font.render('PLAYER 1 WIN', True, (0,255,0))
Game_over2 = font.render('PLAYER 2 WIN', True, (255,0,0))
wight = 700
height = 500

window = display.set_mode((wight,height))
background = transform.scale(image.load('фон.jpg'), (wight,height))
display.set_caption('Пинг понг')

player1 = player1('платформа_1.png',10,100,10,40,100)
player2 = player2('платформа_2.png',600,100,10,30,125)
ball = ball('шарик.png',300,300,10,50,50)



clock = time.Clock()
FPS = 60
dx = 3
dy = 3
rin = True
sec = 2
while rin:
    window.blit(background,(0,0))
    for q in event.get():
        if q.type == QUIT:
            rin = False

    ball.rect.x += dx
    ball.rect.y += dy
    if ball.rect.y > 460 or ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 660 or ball.rect.x <0:
        dx *= -1
    if ball.rect.colliderect(player1.rect):
        dx *= -1
    if ball.rect.colliderect(player2.rect):
        dx *= -1
    if ball.rect.x > 660:
        window.blit(Game_over1, (200,200))
        rin = False  
    if ball.rect.x < 0:
        window.blit(Game_over2, (200,200))
        rin = False  


    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    ball.reset()
    display.update()
    clock.tick(FPS)

display.update()
time.delay(2000)
