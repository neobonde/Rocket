from Rocket.Engine.component import Script, Transform
from Rocket.Engine.event_handler import Keys
from Rocket.Engine.game_loop import Time

class PlayerController(Script):
    
    def setup(self):
        self.speed = 100
        
        self.transform = self.parent.get_component(Transform)
        
        Keys.add_down_callback('a',self.left_down)
        Keys.add_up_callback('a',self.left_up)
        Keys.add_down_callback('d',self.right_down)
        Keys.add_up_callback('d',self.right_up)

        self.left = 0
        self.right = 0

    def update(self):
        direction = -self.left+ self.right
        self.transform.translate(direction * Time.delta_time * self.speed, 0)
        # print(self.left, self.right, direction, self.transform.get_position())

    def left_down(self):
        self.left = 1

    def left_up(self):
        self.left = 0
        
    def right_down(self):
        self.right = 1

    def right_up(self):
        self.right = 0