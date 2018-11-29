import pygame
from time import time
import sys
import os
import configparser

from Rocket.game_loop import GameLoop

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
        screen = pygame.display.set_mode(size)

        rocket = Rocket()

        # TODO screen should not be passed like this!
        GameLoop(screen).start()
