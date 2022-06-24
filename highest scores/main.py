from ast import Try
from itertools import count
import arcade
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
from particlesystem import ParticleSystem
from rectangle import Rectangle
from score import Score
from math import cos, sin, radians

class Pong(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        self.ship = Ship(w/2, h/2, 35, 20, arcade.color.WHITE, 2)
        self.turn_left = False
        self.turn_right = False 
        self.turn_up = False
        self.get_username = True
        self.torpedo = None
        self.rectangle = None
        self.score = 0
        self.particlesys = None
        self.highest_scores = []
        self.username = ""
        self.asteroids = []


        # read scores
        try:
            read_scores = open("highest scores/scores.txt", "r")
            for line in read_scores.readlines():
                print(line)
            read_scores.close()
        except:
            print("no scores to read")
            
        # create asteroids 
        while len(self.asteroids) < 5: self.asteroids.append(Asteroid(50, 500))

    # collision btn torpedo and asteroid
    def bullet_target_collision(self, torpedo, asteroid):
        if torpedo and (torpedo.center_x - 10 < asteroid.center_x < torpedo.center_x + 10) and (torpedo.center_y + 15  > asteroid.center_y > torpedo.center_y - 15 ):
            self.score += 1
            self.asteroids.remove(asteroid)
            self.particlesys = ParticleSystem(10, asteroid.center_x, asteroid.center_y, 1, 10, 2)
            self.asteroids.append(Asteroid(50, 500))
        
    # draw on arcade window
    def on_draw(self):
        self.clear()

        # display ship, torpedo, rectangle
        if self.ship: self.ship.on_draw()
        if self.rectangle: self.rectangle.on_draw()
        if self.torpedo: self.torpedo.on_draw()

        # display particle system
        if self.particlesys:
            self.particlesys.display()
            self.particlesys.update()
               
        #display asteroids
        for asteroid in self.asteroids:
            asteroid.on_draw()
            if asteroid.center_y < 0:
                asteroid.center_y = 500
            self.collide(self.ship, asteroid)
            self.bullet_target_collision(self.torpedo, asteroid)

        # write on window
        if self.ship: arcade.draw_text("Your score is:" + " " + str(self.score), 200, 450)
        if self.rectangle: arcade.draw_text("Highest Score:", 200, 450)

        self.count = 30
        self.scorefile = open('highest scores/scores.txt', 'w')
        for score in self.highest_scores:
            if self.rectangle and len(self.username) > 0: arcade.draw_text(str(score.name) + ":" + str(score.score), 200, (450 - self.count))
            self.count += 30

            # write scores to the scores file. 
            self.scorefile.write(score.name + ":" + str(score.score) + "\n")
        self.scorefile.close()

        if self.rectangle: arcade.draw_text("Click to Start", 200, 245)

        # ship directions
        if self.ship and self.turn_left:
            self.ship.turn(5)
        if self.ship and self.turn_right:
            self.ship.turn(-5)
        if self.ship and self.turn_up:
            self.ship.center_x = self.ship.center_x + (self.ship.length/2 * cos(radians(self.ship.angle)))
            self.ship.center_y = self.ship.center_y + (self.ship.length/2 * sin(radians(self.ship.angle)))

    # ship motion
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.turn_left = True
        elif symbol == arcade.key.RIGHT:
            self.turn_right = True
        elif symbol == arcade.key.UP:
            self.turn_up = True
        elif symbol == arcade.key.ENTER:
            self.get_username = False
        elif self.ship and symbol == arcade.key.SPACE:
            self.torpedo = Torpedo(self.ship.center_x + self.ship.length/2, self.ship.center_y, 0, 0, 15)
            self.torpedo.center_x = self.ship.center_x + (self.ship.length/2 * cos(radians(self.ship.angle)))
            self.torpedo.center_y = self.ship.center_y + (self.ship.length/2 * sin(radians(self.ship.angle)))
            self.torpedo.x_dir = cos(radians(self.ship.angle))
            self.torpedo.y_dir = sin(radians(self.ship.angle))
        if self.get_username:
            self.username += chr(symbol)
     

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.turn_left = False
        elif symbol == arcade.key.RIGHT:
            self.turn_right = False
        elif symbol == arcade.key.UP:
            self.turn_up = False

    # start game
    def on_mouse_press(self, x: int, y: int, dx: int, dy: int):
        if self.rectangle and ( (self.rectangle.center_x - 60 < x < self.rectangle.center_x + 60) and ( self.rectangle.center_y - 20 < y < self.rectangle.center_y + 20 )):
            self.ship = Ship(self.width/2, self.height/2, 35, 20, arcade.color.WHITE, 2)
            self.rectangle = None
            self.score = 0
            self.username = ""
            self.get_username = True

            # read file
            # read_scores = open("highest scores/scores.txt", "r")
            # for line in read_scores.readlines():
            #     print(line)
            # read_scores.close()

       # end game:
    def collide(self, ship, asteroid):
        if ship and (not self.get_username) and (ship.center_x - 15 < asteroid.center_x < ship.center_x + 15) and (ship.center_y + 10  > asteroid.center_y > ship.center_y - 10 ):
            self.ship = None
            self.rectangle = Rectangle(self.width/2, self.height/2)
            highest_score = Score(self.username, self.score)
            self.highest_scores.append(highest_score)

            

           

arcade.window = Pong(500, 500, "Erick' Asteroid Game")
arcade.run()
