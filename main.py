import pygame
from pygame.locals import *
import sys
import random
from teste import *

pygame.init()

screen = pygame.display.set_mode((800, 500))
font = pygame.font.SysFont('Bebas.ttf', 32)
clock = pygame.time.Clock()
gameover_text = "GAME OVER"

Player1 = pygame.Rect(50, screen.get_height()/2 - player_height/2, 5, player_height)
enemy = pygame.Rect(screen.get_width() - 50, screen.get_height()/2 - enemy_height/2, 5, enemy_height)
Ball = pygame.Rect(screen.get_width () / 2 - width_ball / 2, screen.get_height() / 2 - height_ball/2, width_ball, height_ball)

# Botao para baixo
image_move_down = pygame.image.load('button_down.png').convert_alpha()
image_move_down = pygame.transform.scale(image_move_down, (50, 50))  

# Botao para cima
image_move_up = pygame.image.load('button_up2.png').convert_alpha()
image_move_up = pygame.transform.scale(image_move_up, (50, 50))


click_move_down = pygame.Rect(100, screen.get_height()-60, 50, 50)
click_move_up = pygame.Rect(screen.get_width()-100, screen.get_height()/2+190, 50, 50)


def GameOver():
    while game.gameover:
        image = pygame.image.load('back.png').convert_alpha()
        image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
        screen.blit(image, (0,0))
        draw_text(gameover_text, font, (0,255,0), screen,screen.get_width()/2-70, screen.get_height()/2-50)
        draw_text('para jogar novamente aperte ESPAÇO, para SAIR aperte ESC', 
                font, (0,255,0), screen,screen.get_width()/2-320, screen.get_height()/2)    

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    pygame.display.flip()
                    game.gameover = False
                    game.enemy_point = 0
                    game.player_point = 0
                    Player1.x = 50
                    Player1.y = screen.get_height()/2 - player_height/2
                    main()
                    #para jogar novamente aperte ESPAÇO, para SAIR aperte ESC

game = Game()
def main():
    f12 = 0
    click = False
    while True:    
        GameOver()
        fps = int(clock.get_fps())
        pygame.display.set_caption("Ping Pong - " + "FPS: " + str(fps))

        mx, my = pygame.mouse.get_pos()

        screen.fill((52, 63, 82))

        if game.enemy_point >= 5:
            game.gameover = True

        draw_text(str(game.player_point), font, (255, 255, 255), screen, screen.get_width()/2 - 100, screen.get_height()/2- 230)
        draw_text(str(game.enemy_point), font, (255, 255, 255), screen, screen.get_width()/2 + 100, screen.get_height()/2- 230)


        # linha no meio
        pygame.draw.rect(screen, (255, 255, 255), Ball)
        pygame.draw.rect(screen, (255, 255, 255), enemy)

        # suposto player 1
        pygame.draw.rect(screen, (255, 255, 255), Player1)

        pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()/2, 0, 2, screen.get_height()))

        # botão para mover para baixos
        pygame.draw.rect(screen, (52, 63, 82), click_move_down)
        screen.blit(image_move_down, (100, screen.get_height()-60))

        #botao para mover para baixo
        pygame.draw.rect(screen, (52, 63, 82), click_move_up)
        screen.blit(image_move_up, (screen.get_width()-100, screen.get_height()/2+190))


        if click_move_down.collidepoint((mx, my)):          
            if click:    
                Player1.y += 5
        if click_move_up.collidepoint((mx, my)):          
            if click:    
                Player1.y -= 5

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
            if event.type == MOUSEBUTTONDOWN:
                click = True
            if event.type == MOUSEBUTTONUP:
                click = False
                
        clock.tick(90)

        if not game.gameover:
            game.update(Ball=Ball, screen=screen, enemy=enemy,Player1=Player1)
        pygame.display.flip()

if __name__ == '__main__':
    main()
