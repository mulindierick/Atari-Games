import arcade
from random import randint

class Obstacle:
    def __init__(self, x, y):
        self.center_x = randint(x, y)
        self.center_y = randint(x, y)
        self.color = arcade.color.WHITE
        
    def on_draw(self):
        arcade.draw_circle_outline(self.center_x, self.center_y, 10, self.color)

           

     
   
        


