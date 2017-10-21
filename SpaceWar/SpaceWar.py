
from settings import Settings
import pygame
from ship import Ship
import game_founctions


def run_game():
    #初始化并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_helight))
    pygame.display.set_caption('Space War')


    #创建飞船
    ship = Ship(screen, ai_settings)

    #主循环
    while True:
        game_founctions.check_events(ship)
        ship.update()
        game_founctions.update_screen(ai_settings, screen, ship)


run_game()

