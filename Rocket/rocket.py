from Rocket.Engine.entity import Entity
from Rocket.Engine.game_loop import Time
from Rocket.Engine.component import Transform, ImageSprite

from Rocket.player_controller import PlayerController


class Rocket(Entity):

    def setup(self):
        self.add_component(Transform(480/2,750))
        self.add_component(ImageSprite("assets/Rocket.png",subpixel=True))
        controller = self.add_component(PlayerController())

        controller.speed = 100
