import pygame
from pygame.locals import *
import random

clock = pygame.time.Clock()

speed = 7

aleatorio = random.randint(0, 1)

width_ball = 15
height_ball = 15

pygame.init()

End = False

f12 = 0
collide = 0
collide_enemy = 0
# FONTS
font = pygame.font.SysFont('fonts/Bebas.ttf', 32)
font_number = pygame.font.SysFont('fonts/One.ttf', 50)
font_number2 = pygame.font.SysFont('fonts/TitilliumWeb-Regular.ttf', 50)


class Game():
    def __init__(self, *groups):
        super().__init__(*groups)
        self.speed_ball = 5 * random.choice((1, -1))
        self.gameover = False
        self.player_ia_active = False
        self.ball_reset = False
        if aleatorio == 1:
            self.y_speed = -self.speed_ball
            self.x_speed = -self.speed_ball
        elif aleatorio == 0:
            self.y_speed = +self.speed_ball
            self.x_speed = +self.speed_ball
        self.player_point = 0
        self.enemy_point = 0

    def moving_player(self, Player1, screen, player_width):
        if not self.player_ia_active:
            key = pygame.key.get_pressed()
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                Player1.x += speed
            if key[pygame.K_a] or key[pygame.K_LEFT]:
                Player1.x -= speed

            if Player1.x <= 0:
                Player1.x = 5
            elif Player1.x >= screen.get_width() - player_width:
                Player1.x = screen.get_width() - player_width


    def ball(self, Ball, screen):
        Ball.x += self.x_speed
        Ball.y -= self.y_speed

        if Ball.x >= screen.get_width() - width_ball or Ball.x <= 0:
            self.x_speed *= -1

        if Ball.y <= 0:
            self.enemy_point += 1
            self.ball_reset = True

        elif Ball.y >= screen.get_height():
            self.player_point += 1
            self.ball_reset = True
        
    def player_ia(self, Ball, screen, Player1, player_width):
        if self.player_ia_active:
            if Ball.y >= screen.get_height() / 2:
                if Player1.x < Ball.x:
                    Player1.x += speed
                elif Player1.x > Ball.x:
                    Player1.x -= speed
                else:
                    Player1.x += 0
                
                if Player1.x <= 0:
                    Player1.x = 10
                elif Player1.x >= screen.get_width()-player_width:
                    Player1.x = screen.get_width()-player_width

            else:

                if Player1.x > int(screen.get_width() / 2 - player_width/2)-5:
                    Player1.x -= speed
                elif Player1.x < int(screen.get_width()/2 - player_width/2) - 5:
                    Player1.x += speed

    def enemy_ia(self, Ball, screen, enemy, enemy_height):
        if enemy.x < Ball.x:
            enemy.x += speed
        elif enemy.x > Ball.x:
            enemy.x -= speed
        else:
            enemy.x += 0
            
        if enemy.x <= 0:
            enemy.x = enemy_height
        elif enemy.x >= screen.get_width()-enemy_height:
            enemy.x = screen.get_width()-enemy_height
    
    def update(self, Ball, enemy, Player1, screen, enemy_height, player_width):
        if not self.player_ia_active:
            self.moving_player(Player1=Player1, screen=screen, player_width=player_width)
        else:
            self.player_ia(Ball=Ball, screen=screen,Player1=Player1, player_width=player_width)
        self.enemy_ia(Ball=Ball, screen=screen, enemy=enemy, enemy_height=enemy_height)
        self.ball(Ball=Ball, screen=screen)

def draw_text(text, fonte, color, surface, x, y):
    textobj = fonte.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
game = Game()
