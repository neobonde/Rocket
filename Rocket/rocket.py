import pygame
from Rocket.entity import Entity
from Rocket.game_loop import Time


class Rocket(Entity):

    def setup(self):
        self.sprite = pygame.image.load("assets/Rocket.png")
        self.rect = self.sprite.get_rect()

        self.speed = 100

        self.x = 0.0

    def update(self):
        self.x += self.speed * Time.delta_time
        print(self.x)
        # self.rect.move(self.speed * Time.delta_time,0)
        self.rect.x = self.x
        if self.rect.left < 0 or self.rect.right > 480:
            self.speed = -self.speed