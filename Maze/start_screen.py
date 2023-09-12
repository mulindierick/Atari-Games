import arcade


class StartScreen:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y

    def on_draw(self):
        arcade.draw_text("How the game works: ",
                         self.center_x-950, self.center_y-40)
        arcade.draw_text("Once the game starts, enter your name using keyboard. click the enter key to save your name ",
                         self.center_x-950, self.center_y-60)
        arcade.draw_text("Treasures: You begin with zero treasures. you might find treasures in some scenes as you move a long ",
                         self.center_x-950, self.center_y-80)
        arcade.draw_text("DFS - finds a treasure and returns path to it, so does BFS. Robot uses BFS or DFS returned path to get you the treasure: ",
                         self.center_x-950, self.center_y-100)
        arcade.draw_text("Robot dies if path is too long. The no_use treasure will only give you points. It has no other use",
                         self.center_x-950, self.center_y-120)
        arcade.draw_text("Exit treasure: returns cheapest path to exit, and needs map to do so. You get a map using the map treasure ",
                         self.center_x-950, self.center_y-140)
        arcade.draw_text("You lose enery as you move from scene to scene. you gain points as you collect treasures: ",
                         self.center_x-950, self.center_y-160)
        arcade.draw_text("Your goal is to exit the game before you run out of energy ",
                         self.center_x-950, self.center_y-180)
        arcade.draw_text("The game ends when energy is used up or you exited the game: ",
                         self.center_x-950, self.center_y-200)
        arcade.draw_text("Once the game ends, use keyboard to search for player scores by username: ",
                         self.center_x-950, self.center_y-220)
