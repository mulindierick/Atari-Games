import arcade
class Circle:
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
        arcade.draw_circle_filled(self.center_x, self.center_y, 10, arcade.color.WHITE)
       




