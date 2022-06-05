import arcade
from paddle import Paddle
from ball import Ball
from targets import Target

class Pong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paddle = Paddle(250, 20)
        self.ball = Ball(50, 250)

        # track user score
        self.score = 0
        
        # create targets at 5 levels
        self.space = 0
        self.targets = []
        while len(self.targets) < 85:
            self.target1 = Target(10 + self.space, 300, arcade.color.SKY_BLUE)
            self.target2 = Target(10 + self.space, 320, arcade.color.ARMY_GREEN)
            self.target3 = Target(10 + self.space, 340, arcade.color.YELLOW_ORANGE)
            self.target4 = Target(10 + self.space, 360, arcade.color.AFRICAN_VIOLET)
            self.target5 = Target(10 + self.space, 380, arcade.color.TOMATO)
            self.targets.append(self.target1)
            self.targets.append(self.target2)
            self.targets.append(self.target3)
            self.targets.append(self.target4)
            self.targets.append(self.target5)
            self.space += 30

    # collision btn paddle and ball
    def collide(self, paddle, ball):
        if (paddle.center_x - 30 < ball.center_x < paddle.center_x + 30) and (paddle.center_y + 10  > ball.center_y > paddle.center_y - 10 ):
            ball.x_dir *= -1
            ball.y_dir *= -1

    
    # collision btn target and ball
    def ball_target_collision(self, target, ball):
        if (target.center_x - 15 < ball.center_x < target.center_x + 15) and (target.center_y + 10  > ball.center_y > target.center_y - 10 ):
            if target.center_y == 300:
                self.score += 1
            elif target.center_y == 320:
                self.score += 2
            elif target.center_y == 340:
                self.score += 3
            elif target.center_y == 360:
                self.score += 4
            elif target.center_y == 380:
                self.score += 5

            del self.targets[self.targets.index(target)]
            ball.x_dir *= -1
            ball.y_dir *= -1

    # draw on arcade window
    def on_draw(self):
        self.clear()

        # display paddle
        self.paddle.on_draw()

        # display targets
        for target in self.targets:
            target.on_draw()

        #dispaly ball
        self.ball.on_draw()
        if self.ball.center_y < 5:
            self.ball.center_y = 250
        self.collide(self.paddle, self.ball)
        
        #target and ball collision
        if len(self.targets) > 0:
            for target in self.targets:
                self.ball_target_collision(target, self.ball)
                if len(self.targets) == 0:
                    break

        # display score
        arcade.draw_text("Your score is:" + " " + str(self.score), 200, 450)

    # move paddle by key press
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.paddle.center_x -= 50
        elif symbol == arcade.key.RIGHT:
            self.paddle.center_x += 50


arcade.window = Pong(500, 500, "Erick' Breakout Game")
arcade.run()

