from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)

       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed

       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed


win_width = 700
win_height = 500

img_back = "fon.png" 
img_ball = "ball.png" 

display.set_caption("Пин понг")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
ball = Player(img_ball, 5, win_height - 100, 80, 100, 10)

finish = False

run = True 
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    time.delay(50)
    display.update()
