import arcade
from circle import Circle
from obstacles import Obstacle
from torpedo import Torpedo
from rectangle import Rectangle
from centipede import Centipede
from math import cos, sin, radians

class Pong(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        self.circle = Circle(w/2, h/5, 35, 20, arcade.color.WHITE, 2)
        self.centipede = Centipede(w/2, h, 1, 1, 2)
        self.turn_left = False
        self.turn_right = False 
        self.torpedo = None
        self.rectangle = None
        self.score = 0
        self.particlesys = None
        self.obstacles = []
        self.centipede_arr = []

        # create obstacles 
        while len(self.obstacles) < 100: self.obstacles.append(Obstacle(120, 1000))
        while len(self.centipede_arr) < 15: self.centipede_arr.append(Centipede(w/2 - (len(self.centipede_arr) * 20), h, 1, 1, 2))

    # collision btn torpedo and obstacle
    def torpedo_obstacle_collision(self, torpedo, obstacle):
        if torpedo and (torpedo.center_x - 10 < obstacle.center_x < torpedo.center_x + 10) and (torpedo.center_y + 15  > obstacle.center_y > torpedo.center_y - 15 ):
            self.score += 1
            self.obstacles.remove(obstacle)
            self.torpedo = None

     # collision btn torpedo and centipede
    def torpedo_centipede_collision(self, torpedo, centipede):
        if torpedo and (torpedo.center_x - 10 < centipede.center_x < torpedo.center_x + 10) and (torpedo.center_y + 15  > centipede.center_y > torpedo.center_y - 15 ):
            self.score += 1
            self.centipede_arr.remove(centipede)
            self.torpedo = None
    
    # collision btn obstacle and centipede
    def obstacle_centipede_collision(self, centipede, obstacle):
        if obstacle and (obstacle.center_x - 10 < centipede.center_x < obstacle.center_x + 10) and (obstacle.center_y + 15  > centipede.center_y > obstacle.center_y - 15 ):
           print(obstacle.center_x)
           for centipede in self.centipede_arr:
            if centipede.center_x >= obstacle.center_x:
                centipede.x_dir *= -1
                centipede.center_y -= 18
        
    # draw on arcade window
    def on_draw(self):
        self.clear()

        # display circle, torpedo, rectangle
        if self.circle: self.circle.on_draw()
        if self.rectangle: self.rectangle.on_draw()
        if self.torpedo: self.torpedo.on_draw()

        # display centipade
        for centipede in self.centipede_arr:
            if centipede: centipede.on_draw()
            if centipede.center_x > 1000:
                centipede.x_dir *= -1
                centipede.center_y -= 18
            if centipede.center_x < 0:
                centipede.x_dir *= -1
                centipede.center_y -= 18
            self.torpedo_centipede_collision(self.torpedo, centipede)
            

        # display particle system
        if self.particlesys:
            self.particlesys.display()
            self.particlesys.update()
               
        #display obstacles
        for obstacle in self.obstacles:
            obstacle.on_draw()
            if obstacle.center_y < 0:
                obstacle.center_y = 500
            self.collide(self.circle, obstacle)
            self.torpedo_obstacle_collision(self.torpedo, obstacle)
            self.obstacle_centipede_collision(self.centipede_arr[0], obstacle)
            

        # write on window
        if self.circle: arcade.draw_text("Your score is:" + " " + str(self.score), 200, 450)
        if self.rectangle: arcade.draw_text("Final Score:" + " " + str(self.score), 200, 450)
        if self.rectangle: arcade.draw_text("Click to Start", 450, 245)

        # circle directions
        if self.circle and self.turn_left:
            self.circle.center_x = self.circle.center_x - 3
        if self.circle and self.turn_right:
            self.circle.center_x = self.circle.center_x + 3

    # circle motion
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.turn_left = True
        elif symbol == arcade.key.RIGHT:
            self.turn_right = True
        elif self.circle and symbol == arcade.key.SPACE:
            self.torpedo = Torpedo(self.circle.center_x, self.circle.center_y, 1, 1, 15)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.turn_left = False
        elif symbol == arcade.key.RIGHT:
            self.turn_right = False

    # start game
    def on_mouse_press(self, x: int, y: int, dx: int, dy: int):
        if self.rectangle and ( (self.rectangle.center_x - 60 < x < self.rectangle.center_x + 60) and ( self.rectangle.center_y - 20 < y < self.rectangle.center_y + 20 )):
            self.circle = Circle(self.width/2, self.height/5, 35, 20, arcade.color.WHITE, 2)
            self.obstacles = []
            while len(self.obstacles) < 100: self.obstacles.append(Obstacle(120, 1000))
            self.rectangle = None
            self.score = 0


       # end game:
    def collide(self, circle, obstacle):
        if circle and (circle.center_x - 15 < obstacle.center_x < circle.center_x + 15) and (circle.center_y + 10  > obstacle.center_y > circle.center_y - 10 ):
            self.circle = None
            self.rectangle = Rectangle(self.width/2, self.height/2)

arcade.window = Pong(1000, 500, "Erick's Centipade Game")
arcade.run()
