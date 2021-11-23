import pygame
from pygame.locals import *
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 500))
enemy_height = 100
player_height = 100
width_ball = 22
height_ball = 22
font = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()
collision_other_rect = False
collision_player = False
collision_enemy = False
speed = 5

f12 = 0

speed_ball = 5 * random.choice((1, -1))
aleatorio = random.randint(0, 1)

gameover = False
pause = False

Player1 = pygame.Rect(50, screen.get_height()/2 - player_height/2, 5, player_height)
enemy = pygame.Rect(screen.get_width() - 50, screen.get_height()/2 - enemy_height/2, 5, enemy_height)
Ball = pygame.Rect(screen.get_width() / 2 - width_ball / 2, screen.get_height() / 2 - height_ball/2, width_ball, height_ball)


class Game():
    def __init__(self, *groups):
        super().__init__(*groups)

        self.player_ia_active = False
        self.ball_reset = False
        if aleatorio == 1:
            self.y_speed = -speed_ball
            self.x_speed = -speed_ball
        elif aleatorio == 0:
            self.y_speed = +speed_ball
            self.x_speed = +speed_ball
        self.player_point = 0
        self.enemy_point = 0

    def moving_player(self):
        if not self.player_ia_active:
            key = pygame.key.get_pressed()
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                Player1.y -= speed
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                Player1.y += speed

            if Player1.y == 0:
                Player1.y = 5
            elif Player1.y >= screen.get_height() - 100:
                Player1.y = screen.get_height() - 100


    def ball(self):
        Ball.x += self.x_speed
        Ball.y -= self.y_speed

        if Ball.y >= screen.get_height() - 15 or Ball.y <= 0:
            self.y_speed *= -1

        if Ball.x <= 0:
            self.player_point += 1
            self.ball_reset = True

        elif Ball.x >= screen.get_width():
            self.enemy_point += 1
            self.ball_reset = True
        
    def player_ia(self):
        if self.player_ia_active:
            if Ball.x <= screen.get_width() / 2:
                if Player1.y < Ball.y:
                    Player1.y += speed
                elif Player1.y > Ball.y:
                    Player1.y -= speed
                else:
                    Player1.y += 0
                
                if Player1.y <= 0:
                    Player1.y = 10
                elif Player1.y >= screen.get_height()-100:
                    Player1.y = screen.get_height()-100
            else:
                if Player1.y > int(screen.get_height() / 2 - player_height/2)-5:
                    Player1.y -= speed
                elif Player1.y < int(screen.get_height()/2 - player_height/2) - 5:
                    Player1.y += speed
    def enemy_ia(self):
        if Ball.x >= screen.get_width() / 2:
            if enemy.y < Ball.y:
                enemy.y += speed
            elif enemy.y > Ball.y:
                enemy.y -= speed
            else:
                enemy.y += 0
            
            if enemy.y <= 0:
                enemy.y = 10
            elif enemy.y >= screen.get_height()-100:
                enemy.y = screen.get_height()-100
        else:
            if enemy.y > int(screen.get_height() / 2 - enemy_height/2)-5:
                enemy.y -= speed
            elif enemy.y < int(screen.get_height()/2 - enemy_height/2) - 5:
                enemy.y += speed

    def update(self):
        if not self.player_ia_active:
            self.moving_player()
        else:
            self.player_ia()
        self.enemy_ia()
        self.ball()


def draw_text(text, fonte, color, surface, x, y):
    textobj = fonte.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)




game = Game()
while True:        
    fps = int(clock.get_fps())
    pygame.display.set_caption("Ping Pong - " + "FPS: " + str(fps))

    screen.fill((36, 41, 43))

    draw_text(str(game.player_point), font, (255, 255, 255), screen, screen.get_width()/2 - 100, screen.get_height()/2- 230)
    draw_text(str(game.enemy_point), font, (255, 255, 255), screen, screen.get_width()/2 + 100, screen.get_height()/2- 230)

    # linha no meio

    pygame.draw.rect(screen, (255, 255, 255), Ball)
    pygame.draw.rect(screen, (255, 255, 255), enemy)

    # suposto player 1
    pygame.draw.rect(screen, (255, 255, 255), Player1)

    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()/2, 0, 2, screen.get_height()))

    if Ball.colliderect(Player1) or Ball.colliderect(enemy):
        game.x_speed *= -1

    if game.ball_reset:
        Ball.x = screen.get_width() / 2 - width_ball / 2
        Ball.y = screen.get_height() / 2 - height_ball / 2

        game.x_speed *= random.choice((1, -1))
        game.y_speed *= random.choice((1, -1))
        game.ball_reset = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_F12:
                f12 += 1
                if f12 == 1:
                    game.player_ia_active = True
                elif f12 == 2:
                    game.player_ia_active = False
                    f12 = 0


    clock.tick(60)

    if not gameover:
        if not pause:
            game.update()
            pygame.display.flip()
