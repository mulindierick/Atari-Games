import arcade
from circle import Circle
from obstacles import Obstacle
from torpedo import Torpedo
from rectangle import Rectangle
from centipede import Centipede
from random import randint


class Main(arcade.Window):
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
        while len(self.obstacles) < 30: self.obstacles.append(Obstacle( randint(50, 950), randint(120, 450)))

        # create centipede
        while len(self.centipede_arr) < 10: self.centipede_arr.append(Centipede(w/2 - (len(self.centipede_arr) * 20), h, 1, 1, 5))

    # collision btn torpedo and obstacle
    def torpedo_obstacle_collision(self, torpedo, obstacle):
        if torpedo and (torpedo.center_x - 15 < obstacle.center_x < torpedo.center_x + 15) and (torpedo.center_y + 15  > obstacle.center_y > torpedo.center_y - 15 ):
            self.score += 1
            self.obstacles.remove(obstacle)
            self.torpedo = None
    
     # collision btn torpedo and centipede
    def torpedo_centipede_collision(self, torpedo, centipede):
        if torpedo and (torpedo.center_x - 15 < centipede.center_x < torpedo.center_x + 15) and (torpedo.center_y + 15  > centipede.center_y > torpedo.center_y - 15 ):
            self.score += 1
            self.centipede_arr.remove(centipede)
            self.torpedo = None
            self.obstacles.append(Obstacle( centipede.center_x, centipede.center_y))
    
    # collision between centipede and obstacle
    def centipede_obstacle_collision(self, centipedes, obstacles):
        for centipede in centipedes:
            for obstacle in obstacles:
                if obstacle and (obstacle.center_x - 15 < centipede.center_x < obstacle.center_x + 15) and (obstacle.center_y + 15  > centipede.center_y > obstacle.center_y - 15 ):
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
        
        # detect centipede obstacle collision
        self.centipede_obstacle_collision(self.centipede_arr, self.obstacles)

        # detect centipede circle collision
        self.collide(self.centipede_arr, self.circle)

        #display obstacles
        for obstacle in self.obstacles:
            obstacle.on_draw()
            if obstacle.center_y < 0:
                obstacle.center_y = 500
            self.torpedo_obstacle_collision(self.torpedo, obstacle)            

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
            self.rectangle = None
            self.score = 0
            self.circle = Circle(self.width/2, self.height/5, 35, 20, arcade.color.WHITE, 2)
            self.centipede = Centipede(self.width/2, self.height, 1, 1, 2)
            self.obstacles = []
            while len(self.obstacles) < 30: self.obstacles.append(Obstacle( randint(50, 950), randint(120, 450)))
            self.centipede_arr = []
            while len(self.centipede_arr) < 10: self.centipede_arr.append(Centipede(self.width/2 - (len(self.centipede_arr) * 20), self.height, 1, 1, 5))
            
    # end game:
    def collide(self, centipedes, circle):

        # end game if all segments of centipede are hit
        if len(centipedes) == 0:
            self.circle = None
            self.centipede_arr = []
            self.rectangle = Rectangle(self.width/2, self.height/2)
        
        # end game if any segment of centipede collides with circle
        for centipede in centipedes:
            if circle and (circle.center_x - 15 < centipede.center_x < circle.center_x + 15) and (circle.center_y + 15  > centipede.center_y > circle.center_y - 15 ):
                self.circle = None
                self.centipede_arr = []
                self.rectangle = Rectangle(self.width/2, self.height/2)


arcade.window = Main(1000, 500, "Erick's Centipade Game")
arcade.run()