import sys
import pygame



def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """更新屏幕图像，并切换到屏幕"""

    #每次循环时重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()


    #让最近绘制的屏幕可见
    pygame.display.flip()



def check_keydown_events(event, ship):
    """响应按键"""
    #向右开始移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        #向左开始移动飞船
    elif event.key == pygame.K_LEFT:
            ship.moving_left = True



def check_keyup_events(event, ship):
    """响应松开"""
    #向右停止移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    #向左停止移动飞船
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
