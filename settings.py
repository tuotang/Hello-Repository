class Settings():
    """Restore <AI> all configured Class"""

    def __init__(self):
        """initiate setting"""
        #screen setting
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color= (230,230,230)

        #Aliens Para
        self.fleet_drop_speed = 10


        # Ship Parameter
        self.ship_limit = 3

        #Bullet Parameter
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #speed up scale
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """init settings according to game running"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction = 1 means move to right, vice versa
        self.fleet_direction = 1

        #points
        self.alien_points = 50

    def increase_speed(self):
        """speed up settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        
        
        
        
