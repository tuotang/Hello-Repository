class GameStats():
    """trace game statstic info"""

    def __init__(self, ai_settings):
        """init statstic info"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #game starting active status
        self.game_active = False

        
    def reset_stats(self):
        """init stat info in the game running"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

        
