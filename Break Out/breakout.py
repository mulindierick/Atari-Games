import arcade
from paddle import Paddle
from ball import Ball
from targets import Target

class Pong(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paddle = Paddle(250, 20)
        self.ball = Ball(50, 250, 2, -2)

        #track user score
        self.score = 0
        self.targets = []
        
        # create targets at 5 levels
    def start_game(self):
        space = 0
        while len(self.targets) < 85:
            target1 = Target(10 + space, 300, arcade.color.SKY_BLUE)
            target2 = Target(10 + space, 320, arcade.color.ARMY_GREEN)
            target3 = Target(10 + space, 340, arcade.color.YELLOW_ORANGE)
            target4 = Target(10 + space, 360, arcade.color.AFRICAN_VIOLET)
            target5 = Target(10 + space, 380, arcade.color.TOMATO)
            self.targets.append(target1)
            self.targets.append(target2)
            self.targets.append(target3)
            self.targets.append(target4)
            self.targets.append(target5)
            space += 30
    

    # collision btn paddle and ball
    def collide(self, paddle, ball):
        if (paddle.center_x - 40 < ball.center_x < paddle.center_x + 40) and (paddle.center_y + 10  > ball.center_y > paddle.center_y - 10 ):
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
            #delete with something else other than index 
            del self.targets[self.targets.index(target)]
            ball.x_dir += 1
            ball.y_dir -= -1
            ball.x_dir *= -1
            ball.y_dir *= -1
            
            
    # draw on arcade window
    def on_draw(self):
        self.clear()
        # display bricks
        self.start_game()
        # display paddle
        self.paddle.on_draw()
        # display targets
        for target in self.targets:
            target.on_draw()
        #dispaly ball
        self.ball.on_draw()
        self.collide(self.paddle, self.ball)
        
        #target and ball collision
        if len(self.targets) > 0:
            for target in self.targets:
                self.ball_target_collision(target, self.ball)
                if len(self.targets) == 0:
                    break

        # display score
        arcade.draw_text("Your score is:" + " " + str(self.score), 200, 450)

        # reset game
        if self.ball.center_y < 0:
            self.score = 0
            self.targets = []
            self.start_game()
            self.ball.x_dir = 2
            self.ball.y_dir = -2
            self.ball.center_y = 250
            
            
    # move paddle by key press
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.paddle.center_x -= 50
        elif symbol == arcade.key.RIGHT:
            self.paddle.center_x += 50


arcade.window = Pong(500, 500, "Erick' Breakout Game")
arcade.run()

