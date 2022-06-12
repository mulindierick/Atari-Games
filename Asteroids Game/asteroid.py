import arcade
from paddle import Paddle
from ball import Ball
from bullets import Bullet
from particlesystem import ParticleSystem
from math import cos, sin, radians


class Pong(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        self.paddle = Paddle(w/2, h/2, 35, 20, arcade.color.WHITE, 2)
        self.turn_left = False
        self.turn_right = False 
        self.turn_up = False
        self.bullet = None
        # track user score
        self.score = 0

        # create particle systems 
        self.particlesys = None

        # create balls 
        self.balls = []
        while len(self.balls) < 5:
            self.ball = Ball(50, 500)
            self.balls.append(self.ball)

    # paddle and ball collision:
    def collide(self, paddle, ball):
        if (paddle.center_x - 15 < ball.center_x < paddle.center_x + 15) and (paddle.center_y + 10  > ball.center_y > paddle.center_y - 10 ):
            print("yes")
            self.balls = []


    # collision btn bullet and target
    def bullet_target_collision(self, target, ball):
        if target:
            if (target.center_x - 10 < ball.center_x < target.center_x + 10) and (target.center_y + 15  > ball.center_y > target.center_y - 15 ):
                self.score += 2
                self.particle_system = ParticleSystem(10, ball.center_x, ball.center_y, 1, 10, 2)
                self.balls.remove(ball)
                self.particlesys = self.particle_system
                self.ball = Ball(50, 500)
                self.balls.append(self.ball)
        
    # draw on arcade window
    def on_draw(self):
        self.clear()

        # display paddle
        self.paddle.on_draw()

        # show bullet
        if self.bullet:
            self.bullet.on_draw()

        # display particle system
        if self.particlesys:
            self.particlesys.display()
            self.particlesys.update()
               

        #display cirlces
        for ball in self.balls:
            ball.on_draw()
            if ball.center_y < 0:
                ball.center_y = 500
            self.collide(self.paddle, ball)
            self.bullet_target_collision(self.bullet, ball)

        # display score
        arcade.draw_text("Your score is:" + " " + str(self.score), 200, 450)

         # change directions of the ship
        if self.turn_left:
            self.paddle.turn(5)
        if self.turn_right:
            self.paddle.turn(-5)
        if self.turn_up:
            self.paddle.center_x = self.paddle.center_x + (self.paddle.length/2 * cos(radians(self.paddle.angle)))
            self.paddle.center_y = self.paddle.center_y + (self.paddle.length/2 * sin(radians(self.paddle.angle)))

    # ship motion
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.turn_left = True
        elif symbol == arcade.key.RIGHT:
            self.turn_right = True
        elif symbol == arcade.key.UP:
            self.turn_up = True
        elif symbol == arcade.key.SPACE:
            self.bullet = Bullet(self.paddle.center_x + self.paddle.length/2, self.paddle.center_y, 0, 0, 15)
            self.bullet.center_x = self.paddle.center_x + (self.paddle.length/2 * cos(radians(self.paddle.angle)))
            self.bullet.center_y = self.paddle.center_y + (self.paddle.length/2 * sin(radians(self.paddle.angle)))
            self.bullet.x_dir = cos(radians(self.paddle.angle))
            self.bullet.y_dir = sin(radians(self.paddle.angle))

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.turn_left = False
        elif symbol == arcade.key.RIGHT:
            self.turn_right = False
        elif symbol == arcade.key.UP:
            self.turn_up = False

arcade.window = Pong(500, 500, "Erick' Asteroid Game")
arcade.run()
