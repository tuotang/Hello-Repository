class Settings():
    """Restore <AI> all configured Class"""

    def __init__(self):
        """initiate setting"""
        #screen setting
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color= (230,230,230)

        #Aliens Para
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction = 1 means move to right, vice versa
        self.fleet_direction = 1

        # Ship Parameter
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet Parameter
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
