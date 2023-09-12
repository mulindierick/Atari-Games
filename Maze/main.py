import arcade
from scene import Scene
import dijkstra_algorithm
import os
import graph
from random import randint
from start_screen import StartScreen

class Main(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)

        # player
        self.energy = 1000
        self.score = 0
        self.username = ''
        self.get_username = False
        self.end_game = True
        self.start_game = False

        # player functions
        self.treasures = {}
        self.player_treasures = []
        self.display_treasures = []
        self.show_scores = []
        self.path_to_object = None
        self.has_map = False
        self.exit_path = []
        self.game_info = "game info shows here!"

        # get maze
        self.map = graph.build_graph()
        self.curr_scene = self.map.getStart()
        self.exit = self.map.get_exit()

        # list of scenes
        self.scenes = []

        # randomly give treasures to some scenes
    def create_treasures(self):
        possible_treasures = ["DFS", "BFS", "robot", "map", "exit", "no_use"]
        all_scenes = list(self.map.graph.keys())
        for scene in all_scenes:
            r = randint(-3, 6)
            if (r > -1 and r < 6):
                if scene not in self.treasures:
                    self.treasures[scene] = possible_treasures[r]

    # create new scenes
    def create_scenes(self, number_of_scenes):

        # possible treasures
        treasures = []
        count = len(number_of_scenes)-1

        while len(self.scenes) < len(number_of_scenes):

            # if scene has a treasure, display it.
            if number_of_scenes[count]["vertice"] in self.treasures:

                treasures.append(
                    self.treasures[number_of_scenes[count]["vertice"]])
                self.scenes.append(Scene(self.width/1.4 - (len(self.scenes) * 150), self.height-100, 35, 20,
                                         arcade.color.RED_BROWN, 40, number_of_scenes[count]["vertice"], number_of_scenes[count]["cost"], treasures))
                count -= 1
                treasures = []
            else:
                self.scenes.append(Scene(self.width/1.4 - (len(self.scenes) * 150), self.height-100, 35, 20,
                                         arcade.color.RED_BROWN, 40, number_of_scenes[count]["vertice"], number_of_scenes[count]["cost"], []))
                count -= 1

        count = len(number_of_scenes)-1

    # display player treasures on screen
    def display_player_treasures(self, player_treasures):
        if len(player_treasures) > 0:
            count = len(player_treasures)-1
            while len(self.display_treasures) < len(player_treasures):
                self.display_treasures.append(Scene(self.width/4 - (len(self.display_treasures) * 70),
                                              self.height-430, 25, 10, arcade.color.YELLOW_ORANGE, 25, player_treasures[count], None, None))
                count -= 1
            count = len(player_treasures)-1

    # get map
    def map_probe(self):
        graph.get_map()

    # use BFS to find treasure and return path
    def bfs_probe(self, curr_scene, object):
        if object in self.treasures:
            self.path_to_object = None
            self.path_to_object = self.map.bfs(curr_scene, object)
            self.game_info = "path: " + " -> ".join(
                [str(i) for i in self.path_to_object[1:]])
        else:
            self.game_info = "no treasure found :("

    # use DFS to find treasure and return path
    def dfs_probe(self, curr_scene, object):
        if object in self.treasures:
            self.path_to_object = None
            self.path_to_object = self.map.dfs(curr_scene, object)
            self.game_info = "path: " + " -> ".join(
                [str(i) for i in self.path_to_object[1:]])
        else:
            self.game_info = "no treasure found :("

    # if treasure, send robot to find it
    # robot dies if path is too long.
    def robot_probe(self, path):
        cost = 0
        i = 0
        j = 1
        end = False
        while j < len(path) and not end:
            values = self.map.graph[path[i]]
            for v in values:
                if v["vertice"] == path[j]:
                    cost += v["cost"]
            i += 1
            j += 1

            if cost > self.energy:
                self.game_info = "path too long, robot died on the way :("
                end = True

        # robot found treasure
        if cost < self.energy:
            if path[-1] in self.treasures:
                self.game_info = " you got treasure: " + \
                    self.treasures[path[-1]]
                self.player_treasures.append(self.treasures[path[-1]])
                if self.treasures[path[-1]] != "no_use":
                    self.display_treasures = []
                    self.display_player_treasures(self.player_treasures)
                self.score += 2
                del self.treasures[path[-1]]

            else:
                self.game_info = "Treasure already taken"

    # uses map and dj's algorithm - find cheapest path to exit
    # return cheapest path to exit
    def cheapest_path_probe(self, start, exit, map):
        self.exit_path = dijkstra_algorithm.dijkstra(start, exit, map)

    # draw on arcade window
    def on_draw(self):

        self.clear()

        # show start screen
        if (not self.start_game):
            start_screen = StartScreen(self.width, self.height)
            start_screen.on_draw()

            # click btn to start game
            arcade.draw_rectangle_filled(
                500, 100, 120, 40, arcade.color.TOMATO)
            arcade.draw_text("Start game ", 460, 95)

        if (self.start_game):
            # draw scenes on arcade window
            self.create_scenes(self.map.graph[self.curr_scene])
            for scene in self.scenes:
                scene.on_draw()
                arcade.draw_text(str(scene.vertice),
                                 scene.center_x-3, scene.center_y-3)

            # draw player treasures on the screen
            if self.player_treasures:
                self.display_player_treasures(self.player_treasures)
                for treasure in self.display_treasures:
                    treasure.on_draw()
                    arcade.draw_text(str(treasure.vertice),
                                     treasure.center_x-16, treasure.center_y-6)

            # print current scence and game stats
            arcade.draw_text("Game info: ", 650, 100)
            arcade.draw_text(self.game_info, 650, 80)
            arcade.draw_text("You are currently in scene: " +
                             str(self.curr_scene), 400, 100)
            arcade.draw_text("Energy left: " + str(self.energy), 400, 80)
            arcade.draw_text("Total score: " + str(self.score), 400, 60)
            arcade.draw_text("Treasures: " +
                             str(len(self.player_treasures)), 100, 100)


    def on_mouse_press(self, x: int, y: int, dx: int, dy: int):

        # if player enters any of the four scenes
        for scene in self.scenes:
            if (scene.center_x - 30 < x < scene.center_x + 30) and (scene.center_y - 30 < y < scene.center_y + 30):

                # show next scenes
                self.scenes = []
                self.create_scenes(self.map.graph[scene.vertice])
                self.curr_scene = scene.vertice

                # player loses energy
                self.energy -= scene.cost

                # collect treasure if there are any
                # remove a treasure from scene if it has been collected
                if scene.treasures:
                    if scene.treasures[0] == "no_use":
                        self.score += 2
                        if (self.curr_scene in self.treasures):
                            del self.treasures[self.curr_scene]
                        # print(self.treasures)
                    else:
                        self.player_treasures = list(
                            set(self.player_treasures + scene.treasures))
                        if (self.curr_scene in self.treasures):
                            del self.treasures[self.curr_scene]
                        self.display_treasures = []
                        self.display_player_treasures(self.player_treasures)
                        self.score += 2

        # if player users any of their treasures
        for treasure in self.display_treasures:
            if (treasure.center_x - 20 < x < treasure.center_x + 20) and (treasure.center_y - 20 < y < treasure.center_y + 20):

                # set used to true in each case

                if treasure.vertice == "DFS":
                    random_scene = randint(1, 100)
                    self.dfs_probe(self.curr_scene, random_scene)
                    self.player_treasures.remove("DFS")

                elif treasure.vertice == "BFS":
                    random_scene = randint(1, 100)
                    self.bfs_probe(self.curr_scene, random_scene)
                    self.player_treasures.remove("BFS")

                elif treasure.vertice == "robot":
                    if self.path_to_object:
                        self.robot_probe(self.path_to_object)
                        self.player_treasures.remove("robot")
                    else:
                        self.game_info = "You need a path to use the robot probe"

                elif treasure.vertice == "map":
                    self.map_probe()
                    self.player_treasures.remove("map")
                    self.has_map = True
                    self.game_info = "you now have a map"

                elif treasure.vertice == "exit":
                    if (self.has_map):
                        self.cheapest_path_probe(
                            self.curr_scene, self.map.get_exit(), self.map.graph)
                        self.player_treasures.remove("exit")
                        self.has_map = False
                        print(self.exit_path)
                        self.game_info = "exit: " + " -> ".join(
                            [str(i) for i in self.exit_path][1:])
                        os.remove(
                            "/Users/erickmulindi/Desktop/CS209/graph.svg")
                    else:
                        self.game_info = "You need a map to use the exit probe"
                self.display_treasures = []
                self.display_player_treasures(self.player_treasures)

        # start the game:
        if (not self.start_game and (300 < x < 600 and 80 < y < 150)):
            self.start_game = True
            self.get_username = True
            self.end_game = False
            self.energy = 1000
            self.score = 0
            self.player_treasures = []
            self.treasures = {}
            self.display_player_treasures(self.player_treasures)
            self.create_treasures()
            self.scenes = []
            self.curr_scene = self.map.getStart()
            self.create_scenes(self.map.graph[self.curr_scene])
            self.game_info = "game info shows here!"

        # end the game
        if self.energy < 0 or self.curr_scene == self.exit:
            with open('/Users/erickmulindi/Desktop/CS209/Maze/scores.txt', 'a') as scores:
                scores.write(self.username + "," + str(self.score) + "\n")
            scores.close()
            self.end_game = True
            self.start_game = False
            self.username = ''
            self.score = 0
            self.energy = 0
            self.treasures = {}

    # get user name or search user
    def on_key_press(self, symbol: int, modifiers: int):
        if self.get_username and symbol != arcade.key.ENTER:
            self.username += chr(symbol)
        if symbol == arcade.key.ENTER:
            self.get_username = False


arcade.window = Main(1000, 500, "Maze Game")
arcade.run()
