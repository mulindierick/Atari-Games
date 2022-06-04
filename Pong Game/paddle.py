from turtle import clear
import arcade
from random import randint
class Paddle:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.x_dir = -1
        self.y_dir = 1

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.center_x = x
    def on_draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, 30, 20, arcade.color.YELLOW)



