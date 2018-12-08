import pygame # This is just to import all events
import os


class EventHandler():

    _registered_events = { }

    @staticmethod
    def add_event_callback(event, callback):
        if event not in EventHandler._registered_events:
            EventHandler._registered_events[event] = [callback]
        else:
            EventHandler._registered_events[event].append(callback)

        return EventHandler._registered_events[event][-1] # Return just added event index

    @staticmethod
    def remove_event_callback(event, index):
        EventHandler._registered_events[event][index] = None

    @staticmethod
    def has_callback(event):
        return event in EventHandler._registered_events

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            event_name = pygame.event.event_name(event.type)
            if event_name in EventHandler._registered_events:
                for callback in EventHandler._registered_events[event_name]:
                    args = callback.__code__.co_varnames
                    if 'event' in args:
                        callback(event)
                    else:
                        callback()

    @staticmethod
    def quit_game():
        pygame.quit()
        os._exit(1)

    @staticmethod
    def get_event_names():
        names = []
        i = 0
        while True:
            name = pygame.event.event_name(i)
            print(name)
            if name == 'Unknown':
                break
            names.append(name)
            i += 1
        return names


class Keys():

    _registered_key_down_callbacks = {}
    _registered_key_up_callbacks = {}

    @staticmethod
    def add_down_callback(key, callback):
        if not EventHandler.has_callback('KeyDown'):
            EventHandler.add_event_callback('KeyDown', Keys._key_down_event)

        if key not in Keys._registered_key_down_callbacks:
            Keys._registered_key_down_callbacks[key] = [callback]
        else:
            Keys._registered_key_down_callbacks[key].append(callback)

        return Keys._registered_key_down_callbacks[key][-1] # Return just added event index

    @staticmethod
    def add_up_callback(key, callback):
        if not EventHandler.has_callback('KeyUp'):
            EventHandler.add_event_callback('KeyUp', Keys._key_up_event)

        if key not in Keys._registered_key_up_callbacks:
            Keys._registered_key_up_callbacks[key] = [callback]
        else:
            Keys._registered_key_up_callbacks[key].append(callback)

        return Keys._registered_key_up_callbacks[key][-1] # Return just added event index

    @staticmethod
    def _key_up_event(event):
        key = pygame.key.name(event.key)
        if key in Keys._registered_key_up_callbacks:
            _ = [callback() for callback in Keys._registered_key_up_callbacks[key]]

    @staticmethod
    def _key_down_event(event):
        key = pygame.key.name(event.key)
        if key in Keys._registered_key_down_callbacks:
            _ = [callback() for callback in Keys._registered_key_down_callbacks[key]]

    @staticmethod
    def get_key_names():
        pass