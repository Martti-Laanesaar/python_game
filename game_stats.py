class GameStats():
    """Game statistics"""
    def __init__(self, game_settings):
        """Initialize statistics"""
        self.game_settings = game_settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics, change during the game"""
        self.ships_left = self.game_settings.ship_limit