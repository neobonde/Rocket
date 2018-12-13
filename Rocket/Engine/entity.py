

class EntityBank():
    entities = []

    @staticmethod
    def add(entity):
        EntityBank.entities.append(entity)


class Entity():
    def __init__(self, *args, **kwargs):
        EntityBank.add(self)
        self.components = []
        self.setup(*args, **kwargs)

    def get_component(self, component_type):
        return next(component for component in self.components if isinstance(component, component_type))

    def add_component(self,component):
        component.set_parent(self)
        self.components.append(component)
        component.setup()
        return component


    def setup(self):
        pass

