import arcade
from random import uniform
class Particle:
    def __init__(self, x, y, speed, x_dir, y_dir, size, color=arcade.color.WHITE):
        self.center_x = x
        self.center_y = y
        self.speed = speed
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.size = size
        self.color = color
        self.life = 255
    def display(self):
        arcade.draw_ellipse_outline(self.center_x, self.center_y, self.size, self.size, self.color + (self.life,))
    def update(self):
        self.center_x += self.speed * self.x_dir 
        self.center_y += self.speed * self.y_dir
        self.life -= 1
    def is_alive(self):
        return self.life > 0

    

class ParticleSystem:
    def __init__(self, number, center_x, center_y, speed, size, h):
        self.particle_list = []
        self.directions = []
        self.center_x = center_x
        self.center_y = center_y
        self.speed = speed
        self.size = size
        self.h = h
        while len(self.directions) < 20:
            self.directions.append( (uniform(-1, 1), uniform(-1, 1)) )
        while len(self.particle_list) < number:
            self.particle_list.append(Particle(center_x, center_y, speed, self.directions[len(self.particle_list)%len(self.directions)][0], self.directions[len(self.particle_list)%len(self.directions)][1], size))

    def display(self):
        for particle in self.particle_list:
            particle.display()
    
    def update(self):
        for i in range(len(self.particle_list)-1, -1, -1):
            particle = self.particle_list[i]
            particle.update()
            if not particle.is_alive():
                del self.particle_list[i]

        # print(self.h)


# class StarTrek(arcade.Window):
#     def __init__(self, w, h, t):
#         super().__init__(w, h, t)
#         self.particle_system = ParticleSystem(100, w/2, h/2, 1, 10)

#     def on_draw(self):
#         self.clear()
#         self.particle_system.display()
#         self.particle_system.update()

# arcade.window = StarTrek(1000, 500, 'StarTrek')
# arcade.run()
