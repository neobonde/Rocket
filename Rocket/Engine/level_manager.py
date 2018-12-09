from Rocket.Engine.event_handler import EventHandler

class LevelException(Exception):
    pass

class LevelManager():

    _levels = []

    @staticmethod
    def add(level):
        LevelManager._levels.append(level)

    @staticmethod
    def start_game(level=0):
        if not LevelManager._levels:
            raise LevelException("No levels where instantiated") 
        LevelManager._levels[level].setup()

class Level():
    def __init__(self):
        LevelManager.add(self)

    def setup(self):
        pass
