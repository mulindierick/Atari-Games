from turtle import clear
import arcade
from random import randint
class Ship:
    def __init__(self, x, y, length, width, color, breadth):
        self.center_x = x
        self.center_y = y
        self.length = length
        self.width = width
        self.angle = 0

        self.color = color
        self.breadth = breadth

    def turn(self, amount):
        self.angle += amount

    def on_draw(self):
        (x1,y1) = arcade.rotate_point(self.center_x + self.length/2, self.center_y, self.center_x, self.center_y, self.angle)
        (x2,y2) = arcade.rotate_point(self.center_x - self.length/2, self.center_y + self.width/2, self.center_x, self.center_y, self.angle)
        (x3,y3) = arcade.rotate_point(self.center_x - self.length/2, self.center_y - self.width/2, self.center_x, self.center_y, self.angle)
        arcade.draw_triangle_outline(x1, y1, x2, y2, x3, y3, self.color, self.breadth)
       




