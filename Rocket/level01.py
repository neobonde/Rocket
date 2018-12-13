from Rocket.Engine.level_manager import Level

from Rocket.rocket import Rocket
from Rocket.space_background import SpaceBackground
from Rocket.astroid import AstroidSpawner, Astroid
class InfiniteLevel(Level):

    def setup(self):
        SpaceBackground()
        Rocket()
        # Astroid(0)
        AstroidSpawner()
