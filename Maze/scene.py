import arcade
class Scene:
    def __init__(self, x, y, length, width, color, breadth, vertice, cost, treasures):
        self.center_x = x
        self.center_y = y
        self.length = length
        self.width = width
        self.color = color
        self.breadth = breadth
        self.vertice = vertice
        self.cost = cost
        self.treasures = treasures

    def on_draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.breadth, self.color)
       




