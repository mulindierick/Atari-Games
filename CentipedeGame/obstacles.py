import arcade
# from random import randint

class Obstacle:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.color = arcade.color.YELLOW
        
    def on_draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 10, self.color)