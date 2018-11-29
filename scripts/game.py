import pygame
from time import time
import sys
import os
import configparser


class Game():
    """
    This class is responisble for running the game
    """

    def __init__(self):
        pygame.init()

        settings = configparser.ConfigParser()
        settings.read("settings.ini")
        print(settings.sections())

        framerate = int(settings['RENDERING']['framerate'])
        size = [int(side)
                for side in settings['RENDERING']['resolution'].split("x")]
        screen = pygame.display.set_mode(size)
        last_frame = time()

        # TODO MOVE THIS
        rocket_sprite = pygame.image.load("assets/Rocket.png")
        rocket_rect = rocket_sprite.get_rect()
        speed = 1

        # Game loop  - NOTE maybe this should also go in its own class at one point!
        while 1:
            # Event loop  - NOTE Move this to its own class at some point
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # TODO Add escape key exit
                    pygame.quit()
                    return


            # Tick / Framerate
            if last_frame + (1/framerate) < time():
                last_frame = time()
                rocket_rect = rocket_rect.move([speed,0])
                if rocket_rect.left < 0 or rocket_rect.right > size[0]:
                    speed = -speed
                screen.fill((0, 0, 0))
                screen.blit(rocket_sprite, rocket_rect)
                pygame.display.flip()
