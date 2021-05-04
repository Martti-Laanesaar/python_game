import pygame
from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # init game and create display object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")
    # game statistics object
    stats = GameStats(game_settings)

    # create ship
    ship = Ship(game_settings, screen)
    bullets = Group()
    # create alien group
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, aliens, ship, bullets)
            gf.update_aliens(game_settings, stats, screen,ship, aliens, bullets)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)
# test game
run_game()