from turtle import clear
import arcade
from random import randint
from random import choice

class Asteroid:
    def __init__(self, x, y):
        self.center_x = randint(x, y)
        self.center_y = randint(x, y)
        self.color = arcade.color.WHITE
        self.x_dir = 2
        self.y_dir = -2
        
    def on_draw(self):
        arcade.draw_circle_outline(self.center_x, self.center_y, 15, self.color)
        self.center_x += self.x_dir
        self.center_y += self.y_dir
        if self.center_x < 0 or self.center_x > 500:
            self.x_dir *= -1
        if self.center_y < 0  or self.center_y > 500:
            self.y_dir *= -1

           

     
   
        


