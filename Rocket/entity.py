

class EntityBank():
    entities = []

    @staticmethod
    def add(entity):
        EntityBank.entities.append(entity)


class Entity():
    def __init__(self):
        self.sprite = None
        self.rect = None
        EntityBank.add(self)

    def setup(self):
        pass

    def pre_update(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        if self.sprite is not None and self.rect is not None:
            screen.blit(self.sprite, self.rect)

    def post_update(self):
        pass

