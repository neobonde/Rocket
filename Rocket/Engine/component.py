

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
from Rocket.Engine.Includes.subpixelsurface import SubPixelSurface
from copy import copy

class Drawable():
    def draw(self):
        pass

class ImageSprite(Component, Drawable):

    def __init__(self, path, subpixel = False, tile = False):
        self.path = path
        self.subpixel = subpixel
        self.tile = tile

    def setup(self):
        self.transform = self.parent.get_component(Transform)
        self.sprite = image.load(self.path)
        if self.subpixel:
            self.sprite_subpixel = SubPixelSurface(self.sprite)
        self.sprite_rect = self.sprite.get_rect()
        Renderer.add_drawable(self)

    def draw(self, screen):
        x1 = self.transform.get_x()
        y1 = self.transform.get_y()
        self.sprite_rect.x = x1
        self.sprite_rect.y = y1

        if self.tile:
            x2 = x1 + self.sprite_rect.w
            y2 = y1 + self.sprite_rect.h

            if x1 > 0:
                t_x1 = x1 - self.sprite_rect.wx1
                if self.subpixel:
                    screen.blit(self.sprite_subpixel.at(t_x1, y1), (t_x1, y1))
                else:
                    screen.blit(self.sprite, (t_x1, y1))
            
            if x2 < Renderer.get_viewport_width():
                t_x1 = x1 - self.sprite_rect.wx1
                if self.subpixel:
                    screen.blit(self.sprite_subpixel.at(t_x1, y1), (t_x1, y1))
                else:
                    screen.blit(self.sprite, (t_x1, y1))

            if y1 > 0:
                t_y1 = y1 - self.sprite_rect.h
                if self.subpixel:
                    screen.blit(self.sprite_subpixel.at(x1, t_y1), (x1,t_y1))
                else:
                    screen.blit(self.sprite, (x1,t_y1))

            if y2 < Renderer.get_viewport_height():
                t_y1 = y1 + self.sprite_rect.h
                if self.subpixel:
                    screen.blit(self.sprite_subpixel.at(x1, t_y1), (x1,t_y1))
                else:
                    screen.blit(self.sprite, (x1,t_y1))


        if self.subpixel:
            screen.blit(self.sprite_subpixel.at(x1, y1), self.sprite_rect)
        else:
            screen.blit(self.sprite, self.sprite_rect)

    def get_rect(self):
        return self.sprite_rect


# NOTE Use this class for user defined scritps!
class Script(Component):
    def __init__(self):
        super(Script).__init__()
        # TODO save the name of the script ei the child
