from Rocket.entity import Entity
from Rocket.game_loop import Time
from Rocket.component import Transform, ImageSprite, PlayerController


class Rocket(Entity):

    def setup(self):
        self.add_component(Transform(0,0))
        self.add_component(ImageSprite("assets/Rocket.png"))
        self.add_component(PlayerController())
