import pygame
from time import time

from Rocket.entity import EntityBank
from Rocket.renderer import Renderer

class Time():
    
    delta_time = 0


#TODO Make this a singleton?
class GameLoop():

    def start(self):
        [e.setup() for e in EntityBank.entities]
        while 1:
            start_time = time() 
            
            # Events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
            
            components = []
            components.extend([e.components for e in EntityBank.entities][0])

            [c.pre_update() for c in components]
            [c.update() for c in components]

            # Rendering
            Renderer.render_pool()
            
            [c.post_update() for c in components]
            
            Time.delta_time = time() - start_time
