import arcade

class Centipede:
    def __init__(self, x, y, x_dir, y_dir, speed):
        self.center_x = x
        self.center_y = y
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.speed = speed
        self.color = arcade.color.RED
        
    def on_draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 10, self.color)
        self.center_x += self.x_dir * self.speed