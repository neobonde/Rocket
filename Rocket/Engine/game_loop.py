import pygame
from time import time

from Rocket.Engine.entity import EntityBank
from Rocket.Engine.renderer import Renderer
from Rocket.Engine.event_handler import EventHandler, Keys
from Rocket.Engine.level_manager import LevelManager

 
class Time():
    
    delta_time = 0

    @staticmethod
    def get_time():
        return time()

    @staticmethod
    def get_fps():
        if Time.delta_time > 0:
            return 1/Time.delta_time
        return float("inf")

#TODO Make this a singleton?
class GameLoop():

    def start(self):

        LevelManager.start_game()    

        # Exit events, one for a key and one for the X button on the screen
        EventHandler.add_event_callback('Quit',EventHandler.quit_game)
        Keys.add_down_callback('escape',EventHandler.quit_game)
        
        while 1:
            start_time = Time.get_time() 
            
            # Events 
            EventHandler.handle_events()

            components = [component for entities in EntityBank.entities for component in entities.components]

            [c.pre_update() for c in components]
            [c.update() for c in components]

            # Rendering
            Renderer.render_pool()
            
            [c.post_update() for c in components]
            
            Time.delta_time = Time.get_time() - start_time
            # print(Time.get_fps())