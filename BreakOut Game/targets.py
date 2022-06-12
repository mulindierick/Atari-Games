import arcade
class Target:
    def __init__(self, x, y, color):
        self.center_x = x
        self.center_y = y
        self.color = color

    def on_draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, 30, 20, self.color)





