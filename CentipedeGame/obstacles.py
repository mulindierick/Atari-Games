import arcade
from random import randint

class Obstacle:
    def __init__(self, x, y):
        self.center_x = randint(50, x)
        self.center_y = randint(120, y)
        self.color = arcade.color.YELLOW
        
    def on_draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 10, self.color)