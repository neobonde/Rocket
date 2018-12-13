from Rocket.Engine.entity import Entity
from Rocket.Engine.component import ImageSprite, Transform, Script
from Rocket.Engine.game_loop import Time
from Rocket.Engine.renderer import Renderer

class AutoScroll(Script):

    def setup(self):
        self.transform = self.parent.get_component(Transform)
        self.sprite = self.parent.get_component(ImageSprite)

    def update(self):
        self.transform.translate(0,200 * Time.delta_time)

        if self.transform.get_y() > Renderer.get_viewport_height()/2:
            self.transform.set_y((-self.sprite.get_rect().h+Renderer.get_viewport_height())/2)


class SpaceBackground(Entity):
    def setup(self):
        self.add_component(Transform(0,0))
        self.add_component(ImageSprite("assets/Space.png",subpixel=False, tile=True))
        self.add_component(AutoScroll())