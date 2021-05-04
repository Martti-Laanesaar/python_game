import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet control class"""
    def __init__(self, game_setting, screen, ship):
        """Create bullet object at ship position"""
        super().__init__()
        self.screen = screen
        # create bullet
        self.rect = pygame.Rect(0, 0, game_setting.bullet_width, game_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # bullet position
        self.y = float(self.rect.y)
        # bullet settings
        self.color = game_setting.bullet_color
        self.speed_factor = game_setting.bullet_speed_factor
    def update(self):
        """Update bullet position"""
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        """Draw bullet at screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)