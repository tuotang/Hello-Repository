class Settings():
    """Restore <AI> all configured Class"""

    def __init__(self):
        """initiate setting"""
        #screen setting
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color= (230,230,230)

        # Ship Parameter
        self.ship_speed_factor = 1.5

        #Bullet Parameter
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
