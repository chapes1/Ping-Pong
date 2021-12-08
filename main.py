import pygame
import sys
from pygame.locals import *
import random
from teste import *

pygame.init()

resolution = pygame.display.Info()
width = resolution.current_w
height = resolution.current_h

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

x = 10 * width
enemy_height = x / 100
player_width = x / 100

metade_com_player_height = screen.get_height() - 100
metade_com_player_width = screen.get_width()/2 - player_width / 2

Enemy = pygame.Rect(metade_com_player_width, 100, player_width, 2)
Player = pygame.Rect(metade_com_player_width, metade_com_player_height, player_width, 2)

Ball = pygame.Rect(screen.get_width()/2 - width_ball/2, screen.get_height()/2 - height_ball/2, width_ball, height_ball)

while True:
    screen.fill((52, 63, 82)) 
    pygame.display.set_caption("Ping Pong")
    mx, my = pygame.mouse.get_pos()

    #Desenhando os pontos de cada jogador
    draw_text('P: '+str(game.player_point), font_number, (255,255,255), screen, 100, 50)
    draw_text('E: '+str(game.enemy_point), font_number, (255,255,255), screen, screen.get_width()-100,50)


    # Personagens
    pygame.draw.rect(screen, (255, 255, 255), (5, height/2, width, 2))
    pygame.draw.rect(screen, (255, 255, 255), Player)
    pygame.draw.rect(screen, (255, 255, 255), Enemy)
    pygame.draw.rect(screen, (255, 255, 255), Ball, border_radius=50)

    if Ball.colliderect(Player) or Ball.colliderect(Enemy):
        game.y_speed *= -1
        
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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_F12:
                f12 += 1
                if f12 == 1:
                    game.player_ia_active = True
                elif f12 == 2:
                    game.player_ia_active = False
                    f12 = 0

    if not End:
        game.update(Ball=Ball, screen=screen, enemy=Enemy,Player1=Player, player_width=player_width, enemy_height=enemy_height)
    clock.tick(60)
    pygame.display.update()