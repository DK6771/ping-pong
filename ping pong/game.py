#region start
from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption()
background = transform.scale(image.load(picture),(700, 500))
#endregion

while game:
    window.blit(background, (0, 0))

        sprite1.update()
        sprite1.reset()
        sprite2.update()
        sprite2.reset()

    else:
        if finish == 1:
            text3.draw()
        elif finish == 2:
            text4.draw()

    for e in event.get():
                if e.type == QUIT:
                    game = False

    FPS = 60
    clock.tick(FPS)
    display.update()
