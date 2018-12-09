from Rocket.Engine.level_manager import Level

from Rocket.rocket import Rocket
from Rocket.space_background import SpaceBackground

class InfiniteLevel(Level):

    def setup(self):
        SpaceBackground()
        Rocket()