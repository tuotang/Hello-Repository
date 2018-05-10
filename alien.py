import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """one alien class"""

    def __init__(self, ai_settings, screen):
        """initial alien and set first position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image, set rect parameter
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #each alien postion left up corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #restore alien real postion
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien at appoint position"""
        self.screen.blit(self.image, self.rect)
