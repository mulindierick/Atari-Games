from turtle import clear
import arcade
from random import randint
from random import choice

class Torpedo:
    def __init__(self, x, y, x_dir, y_dir, speed):
        self.center_x = x
        self.center_y = y
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.speed = speed
        
    def on_draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 5, arcade.color.WHITE)
        self.center_y += self.y_dir * self.speed

        

           

     
   
        


