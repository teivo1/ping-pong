from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < 380:
            self.rect.y += self.speed_y

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x -= self.speed_x


img_player = "racket_test.png"
img_ball = "ball.png"

player1 = Player(img_player, -15, 100, 0, 5, 70, 120)
player2 = Player(img_player, 645, 100, 0, 5, 70, 120)
ball = Ball(img_ball, 300, 300, 4, 4, 60, 60)

hits = 0
game = True
finish = False

clock = time.Clock()
FPS = 60

font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 40)
won1 = font1.render("Player 1 won!", True, (102, 255, 0))
won2 = font1.render("Player 2 won!", True, (102, 255, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        text_hits = font2.render("Hits: " + str(hits), 1, (255, 255, 255))
        window.blit(text_hits, (300, 20))
        player1.update_r()
        player1.reset()
        player2.update_l()
        player2.reset()
        ball.update()
        ball.reset()
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        ball.speed_x *= -1
        hits += 1
        text_hits = font2.render("Hits: " + str(hits), 1, (255, 255, 255))
        window.blit(text_hits, (300, 20))

    if ball.rect.y > 440:
        ball.speed_y *= -1
    if ball.rect.y < 0:
        ball.speed_y *= -1

    if ball.rect.x < 35:
        window.blit(won2, (190, 215))
        finish = True
    if ball.rect.x > 630:
        window.blit(won1, (190, 215))
        finish = True


    display.update()
    clock.tick(FPS)
