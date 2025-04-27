#https://docs.google.com/presentation/d/18eTZ8OU9-FkEVV5YXYftJmshKv6Qh-O6lT2Otw9T8rc/edit?slide=id.gca1f5aec5f_0_221#slide=id.gca1f5aec5f_0_221
#https://docs.google.com/document/d/1RzQc7EHXTRUUcp6LxaRy9k3nyb0EVXaC6LPacCzT5Ic/edit?tab=t.0
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

# Initialize Pygame


win_width = 700
win_height = 500

img_back = "fon.png" 
img_ball = "ball.png" 
racket1_img = 'racket1.png'
racket2_img = 'racket2.png'

display.set_caption("Пин понг")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# Create ball and rackets
ball = GameSprite(img_ball, 5, win_height - 100, 80, 100, 10)
racket1 = GameSprite(racket1_img, 5, win_height - 30, 100, 20, 10)
racket2 = GameSprite(racket2_img, win_width - 105, win_height - 30, 100, 20, 10)

finish = False

speed_x = 3
speed_y = 3

font1 = font.SysFont(None, 36)
lose1 = font1.render('PLAYER LOSE!', True, (180, 0, 0))

run = True 

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1
    
    # Check for collisions with rackets
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
    
    # Draw everything
    window.blit(background, (0,0))
    racket1.reset()
    racket2.reset()
    ball.reset()

    if finish:
        window.blit(lose1, (200, 200))

    time.delay(50)
    display.update()

pygame.quit()
