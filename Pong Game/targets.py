import arcade
class Rec:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.x_dir = -2
        self.y_dir = 2
    def on_draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, 30, 20, arcade.color.AFRICAN_VIOLET)
        self.center_x += self.x_dir




