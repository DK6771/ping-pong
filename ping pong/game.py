#region start
from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption()
background = transform.scale(image.load(picture),(700, 500))
#endregion

#region музон
mixer.init()
mixer.music.load('music')
mixer.music.play()
#endregion

#region FPS
clock = time.Clock()
game = True
#endregion

speed = 5
x = 5
y = 250
y1 = 250
x1 =495










class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_speed, player_x, player_y,width,heigth):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, heigth))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.x += self.speed

class Label():
    def __init__(self, text, x, y):
        self.font1 = font.SysFont("Arial", 36)
        self.text = self.font1.render(text, True, (255, 255, 255))
        self.x = x
        self.y = y
    def set_text(self, text):
        self.text = self.font1.render(text, True, (255, 255, 255))
    def draw(self):
        window.blit(self.text, (self.x, self.y))
sprite2 = ...('bal.png', 5, x, y, 65, 65)
sprite1 = Player("line.png", 5, x, y, 65, 65)
text1 = Label('игрок 1 выиграл', 350, 250)
text2 = Label('игрок 2 выиграл', 350, 250)

while game:
    window.blit(background, (0, 0))

        #sprite1.update()
       # sprite1.reset()
        #sprite2.update()
        #sprite2.reset()

    for e in event.get():
                if e.type == QUIT:
                    game = False

    FPS = 60
    clock.tick(FPS)
    display.update()

