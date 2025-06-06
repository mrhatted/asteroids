from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x,self.position.y),self.radius, 2)

    def update(self,dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angular_difference = random.uniform(20,50)
        angle_1 = pygame.math.Vector2.rotate(self.velocity, angular_difference)
        angle_2 = pygame.math.Vector2.rotate(self.velocity, angular_difference)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_1.velocity = angle_1 * 1.2
        asteroid_2.velocity = angle_2 * 1.2
        

    