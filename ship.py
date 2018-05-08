import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """init ship and set position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship.bmp and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #let each ship on the bottom
        self.rect.centerx= self.screen_rect.centerx
        self.rect.bottom= self.screen_rect.bottom

        # Restore float value in center parameter
        self.center = float(self.rect.centerx)

        #Moving Label
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """justify ship position according to the moving label"""
        #update center value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object according to selfcenter
        self.rect.centerx = self.center

    def blitme(self):
        """draw ship at the appoint position"""
        self.screen.blit(self.image, self.rect)
