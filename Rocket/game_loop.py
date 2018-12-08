import pygame
from time import time

from Rocket.entity import EntityBank
from Rocket.renderer import Renderer
from Rocket.event_handler import EventHandler, Keys

class Time():
    
    delta_time = 0


#TODO Make this a singleton?
class GameLoop():

    def start(self):
        [e.setup() for e in EntityBank.entities]

        # Exit events, one for a key and one for the X button on the screen
        EventHandler.add_event_callback('Quit',EventHandler.quit_game)
        Keys.add_down_callback('escape',EventHandler.quit_game)
        
        while 1:
            start_time = time() 
            
            # Events 
            EventHandler.handle_events()

            components = []
            components.extend([e.components for e in EntityBank.entities][0])

            [c.pre_update() for c in components]
            [c.update() for c in components]

            # Rendering
            Renderer.render_pool()
            
            [c.post_update() for c in components]
            
            Time.delta_time = time() - start_time
