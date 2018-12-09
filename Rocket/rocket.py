from Rocket.Engine.entity import Entity
from Rocket.Engine.game_loop import Time
from Rocket.Engine.component import Transform, ImageSprite

from Rocket.player_controller import PlayerController


class Rocket(Entity):

    def setup(self):
        transform = self.add_component(Transform(0,0))
        self.add_component(ImageSprite("assets/Rocket.png"))
        controller = self.add_component(PlayerController())

        transform.set_position(480/2,750)
        controller.speed = 200
