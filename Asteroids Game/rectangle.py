import arcade
class Rectangle:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
    def on_draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, 120, 40, arcade.color.TOMATO)



