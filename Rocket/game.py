import pygame
from time import time
import sys
import os
import configparser

from Rocket.game_loop import GameLoop
from Rocket.renderer import Renderer

from Rocket.rocket import Rocket

class Game():
    """
    This class is responisble for running the game
    """

    def __init__(self):
        pygame.init()

        settings = configparser.ConfigParser()
        settings.read("settings.ini")

        framerate = int(settings['RENDERING']['framerate'])
        size = [int(side)
                for side in settings['RENDERING']['resolution'].split("x")]

        Renderer.create_viewport(size[0], size[1])

        # TODO This should be moved to some sort of level or scene manager!
        rocket = Rocket()

        GameLoop().start()
