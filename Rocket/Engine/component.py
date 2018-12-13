

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
        self.prev_x = x
        self.prev_y = y
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

    def get_change(self):
        res = (self.x - self.prev_x, self.y - self.prev_y)
        self.prev_x = self.x
        self.prev_y = self.y
        return res

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

from pygame import image, Rect
from pygame import transform as tf
from Rocket.Engine.renderer import Renderer
from Rocket.Engine.Includes.subpixelsurface import SubPixelSurface
from copy import copy
import pygame as pg

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
        self.sprite_orig = image.load(self.path)
        self.sprite = self.sprite_orig.copy()
        if self.subpixel:
            self.sprite_subpixel = SubPixelSurface(self.sprite)
        self.sprite_rect = self.sprite.get_rect()
        self.angle = 0
        Renderer.add_drawable(self)

    def draw(self, screen):
        x, y = self.sprite_rect.center  # Save its current center.
        x1, y1 = self.transform.get_position()
        
        self.sprite_rect.x = x1
        self.sprite_rect.y = y1
        self.sprite = tf.rotate(self.sprite_orig, self.angle)
        self.angle += self.angle % 360  # Value will reapeat after 359. This prevents angle to overflow.
        x, y = self.sprite_rect.center  # Save its current center.
        self.sprite_rect = self.sprite.get_rect()  # Replace old rect with new rect.
        self.sprite_rect.center = (x, y)  # Put the new rect's center at old center.
        
        if self.tile:
            x2 = x1 + self.sprite_rect.w
            y2 = y1 + self.sprite_rect.h

            if x1 > 0:
                t_x1 = x1 - self.sprite_rect.w
                if self.subpixel:
                    screen.blit(self.sprite_subpixel.at(t_x1, y1), (t_x1, y1))
                else:
                    screen.blit(self.sprite, (t_x1, y1))
            
            if x2 < Renderer.get_viewport_width():
                t_x1 = x1 + self.sprite_rect.w
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
            screen.blit(self.sprite,self.sprite_rect)

    def get_rect(self):
        return self.sprite_rect

    def rotate(self, angle):
        if self.subpixel:
            raise AttributeError("Cannot rotate a subpixeled sprite")
        self.angle = angle



# NOTE Use this class for user defined scritps!
class Script(Component):
    def __init__(self):
        super(Script).__init__()
        # TODO save the name of the script ei the child
