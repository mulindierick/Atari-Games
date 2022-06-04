import arcade
from paddle import Paddle
from ball import Ball
from targets import Rec

class Pong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paddle = Paddle(250, 250)

        # track user score
        self.score = 0

        # create targets
        self.targets = []
        while len(self.targets) < 3:
            self.target = Rec(100 + len(self.targets * 150), 350)
            self.targets.append(self.target)

        # create balls 
        self.balls = []
        while len(self.balls) < 5:
            self.ball = Ball(50, 500)
            self.balls.append(self.ball)
    
    # collision btn paddle and ball
    def collide(self, paddle, ball):
        if (paddle.center_x - 15 < ball.center_x < paddle.center_x + 15) and (paddle.center_y + 10  > ball.center_y > paddle.center_y - 10 ):
            ball.x_dir *= -1
            ball.y_dir *= -1
            if ball.color == arcade.color.GREEN:
                self.score = self.score  + 1
            if ball.color == arcade.color.RED:
                self.score = self.score  - 1
    
    # collision btn target and ball
    def ball_target_collision(self, target, ball):
        if (target.center_x - 15 < ball.center_x < target.center_x + 15) and (target.center_y + 10  > ball.center_y > target.center_y - 10 ):
            self.score += 2
            del self.targets[self.targets.index(target)]

    # draw on arcade window
    def on_draw(self):
        self.clear()
        # display paddle
        self.paddle.on_draw()

        # display targets
        for target in self.targets:
            target.on_draw()
            if target.center_x < 5:
                target.center_x = 500


        #display cirlces
        for ball in self.balls:
            ball.on_draw()
            if ball.center_y < 5:
                ball.center_y = 500
            self.collide(self.paddle, ball)
        
        #target and ball collision
        if len(self.targets) > 0:
            for target in self.targets:
                for ball in self.balls:
                    self.ball_target_collision(target, ball)
                    if len(self.targets) == 0:
                        break

        # display score
        arcade.draw_text("Your score is:" + " " + str(self.score), 200, 450)

    # move target by mouse motion
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.paddle.center_x = x


arcade.window = Pong(500, 500, "Erick' Pong Game")
arcade.run()

