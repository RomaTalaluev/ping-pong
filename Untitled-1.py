
from time import time as TIME
from pygame import *

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
        if keys[K_s] and self.rect.y < wight - 110:
            self.rect.y += self.speed

class player2(enemy):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:

            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < wight - 110:
            self.rect.y += self.speed

        
            

class ufo(enemy):
    def update(self):
        self.rect.y += self.speed
        global lose
        if self.rect.y > height:
            self.rect.x = randint(0,590)
            self.rect.y = 0
            lose += 1




wight = 700
height = 500

window = display.set_mode((wight,height))
background = transform.scale(image.load('фон.jpg'), (wight,height))
display.set_caption('Пинг понг')



clock = time.Clock()
FPS = 60

rin = True

while rin:
    window.blit(background,(0,0))
    for q in event.get():
        if q.type == QUIT:
            rin = False

    display.update()
    clock.tick(FPS)