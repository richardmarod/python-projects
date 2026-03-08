"""
GameSession class for storing one gaming session.
"""

class GameSession:
    """
    Represents a single game session.
    Stores game name, date, hours played, and platform.
    """
    
    def __init__(self, game, date, hours, platform):
        self.game = game
        self.date = date
        self.platform = platform
        self.__hours = hours # private attribute

    def get_hours(self):
        return self.__hours

    def set_hours(self, new_hours):
        if new_hours > 0:
            self.__hours = new_hours
            return True
        return False

    def __str__(self):
        return (
            f"Game: {self.game} | Date: {self.date} | "
            f"Hours: {self.__hours} | Platform: {self.platform}"
)

# magic method (not __str__)
def __len__(self):
    return int(self.__hours)