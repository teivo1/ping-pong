from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
background = transform.scale(image.load("back.jpg"), (win_width, win_height))

game = True

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0, 0))

    display.update()
    clock.tick(FPS)