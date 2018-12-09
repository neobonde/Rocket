

class Component():
    def __init__(self):
        self.parent = None

    def set_parent(self,parent):
        self.parent = parent

    def setup(self):
        pass

    def pre_update(self):
        pass

    def update(self):
        pass

    def post_update(self):
        pass 

#NOTE For now all basic components in this file maybe move later!

# Position component for entities
class Transform(Component):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        self.x += x
        self.y += y
    
    def get_position(self):
        return (self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

from pygame import image
from Rocket.Engine.renderer import Renderer

class Drawable():
    def draw(self):
        pass

class ImageSprite(Component, Drawable):

    def __init__(self, path):
        self.path = path

    def setup(self):
        self.transform = self.parent.get_component(Transform)
        self.sprite = image.load(self.path)
        self.sprite_rect = self.sprite.get_rect()
        Renderer.add_drawable(self)

    def draw(self, screen):
        self.sprite_rect.x = self.transform.get_x()
        self.sprite_rect.y = self.transform.get_y()
        screen.blit(self.sprite, self.sprite_rect)

    def get_rect(self):
        return self.sprite_rect


# NOTE Use this class for user defined scritps!
class Script(Component):
    def __init__(self):
        super(Script).__init__()
        # TODO save the name of the script ei the child
