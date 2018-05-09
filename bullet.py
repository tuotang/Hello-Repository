import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class for managing the bullet from ship"""

    def __init__(self, ai_settings, screen, ship):
        """create one B @ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create rect at (0,0), and set correctly position for B
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #restore the float value for postion of bullet
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """moving up"""
        #update B position float value
        self.y -= self.speed_factor
        #update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw B"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
