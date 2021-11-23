import pygame
from pygame.locals import *
import sys
import random


pygame.init()

speed = 5

aleatorio = random.randint(0, 1)
enemy_height = 100
player_height = 100
width_ball = 22
height_ball = 22

class Game():
    def __init__(self, *groups):
        super().__init__(*groups)
        self.speed_ball = 4 * random.choice((1, -1))
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

    def moving_player(self, Player1, screen):
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


    def ball(self, Ball, screen):
        Ball.x += self.x_speed
        Ball.y -= self.y_speed

        if Ball.y >= screen.get_height() - 15 or Ball.y <= 0:
            self.y_speed *= -1

        if Ball.x <= 0:
            self.enemy_point += 1
            self.ball_reset = True

        elif Ball.x >= screen.get_width():
            self.player_point += 1
            self.ball_reset = True
        
    def player_ia(self, Ball, screen, Player1):
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

    def enemy_ia(self, Ball, screen, enemy):
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

    def update(self, Ball, enemy, Player1, screen):
        if not self.player_ia_active:
            self.moving_player(Player1=Player1, screen=screen)
        else:
            self.player_ia(Ball=Ball, screen=screen,Player1=Player1)
        self.enemy_ia(Ball=Ball, screen=screen, enemy=enemy)
        self.ball(Ball=Ball, screen=screen)

def draw_text(text, fonte, color, surface, x, y):
    textobj = fonte.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)