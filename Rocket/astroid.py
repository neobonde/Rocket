from Rocket.Engine.entity import Entity
from Rocket.Engine.component import Script, Transform, ImageSprite
from Rocket.Engine.game_loop import Time
from Rocket.Engine.renderer import Renderer

import math

from random import uniform

class AstroidSpawnerScript(Script):
    def __init__(self):
        super(AstroidSpawnerScript).__init__()

    def setup(self):
        self.astroids = []

        self.spawn_range = [0,Renderer.get_viewport_width()]
        self.spawn_time = 1 # seconds
        self.last_spawn = Time.get_time()

    def update(self):
        if Time.get_time() > self.last_spawn + self.spawn_time:
            self.last_spawn = Time.get_time()
            random_x = uniform(self.spawn_range[0],self.spawn_range[1])
            astroid = Astroid(random_x)
            astroid_rect = astroid.get_component(ImageSprite).get_rect()
            # astroid.get_component(Transform).set_y(-astroid_rect.h)
            self.astroids.append(astroid)



class AstroidSpawner(Entity):

    def setup(self):
        self.add_component(AstroidSpawnerScript())


# TODO add destroy on exit screen functionallity

class AstroidMovement(Script):
    def __init__(self, speed_range, rotation_speed):
        super(AstroidMovement).__init__()
        self.speed_range = speed_range
        self.rotation_speed = rotation_speed

    def setup(self):
        self.sprite = self.parent.get_component(ImageSprite)
        self.angle = uniform(0,360) % 360
        self.sprite.rotate(self.angle)
        self.speed = uniform(self.speed_range[0], self.speed_range[1])
        self.transform = self.parent.get_component(Transform)
        self.slope = uniform(-0.1, 0.1)

    def update(self):
        self.angle += self.rotation_speed * Time.delta_time
        self.sprite.rotate(self.angle)
        self.transform.translate(self.slope*self.speed*Time.delta_time, self.speed*Time.delta_time)

    def get_angle(self, x1, y1, x2, y2):
        return math.atan2(y2-y1, x2-x1)


class Astroid(Entity):

    def setup(self, x):
        self.add_component(Transform(x,0))
        self.add_component(ImageSprite("Assets/Astroid.png", subpixel=False))
        self.add_component(AstroidMovement((75,150),100))