import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #Create a instance for restore game static info
    stats = GamesStats(ai_settings)

    #create a ship, a bullets group, and aliens group
    ship= Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #create a alien group
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Game Main Cycle
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
