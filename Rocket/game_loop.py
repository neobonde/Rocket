import pygame
from time import time

from Rocket.entity import EntityBank

class Time():
    
    delta_time = 0


#TODO Make this a singleton?
class GameLoop():
    def __init__(self, screen):
        self.screen = screen
    
    def start(self):
        [e.setup() for e in EntityBank.entities]
        while 1:
            start_time = time() 
            
            # Events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # TODO Add escape key exit
                    pygame.quit()
                    return

            [e.pre_update() for e in EntityBank.entities]
            
            [e.update() for e in EntityBank.entities]

            # Rendering
            self.screen.fill((0, 0, 0))
            [e.draw(self.screen) for e in EntityBank.entities]
            pygame.display.flip()
            
            [e.post_update() for e in EntityBank.entities]
            
            Time.delta_time = time() - start_time
