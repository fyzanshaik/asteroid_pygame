import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS,ASTEROID_MAX_RADIUS,ASTEROID_KINDS,ASTEROID_SPAWN_RATE
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
        
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)
        
    def update(self,dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        random_angle = random.uniform(20,50)
        vel_vector1 = self.velocity.rotate(random_angle)
        vel_vector2 = self.velocity.rotate(-random_angle)
        
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        
        smaller_asteroid_one = Asteroid(self.position.x,self.position.y,smaller_radius)
        smaller_asteroid_two = Asteroid(self.position.x,self.position.y,smaller_radius)

        smaller_asteroid_one.velocity = vel_vector1
        smaller_asteroid_two.velocity = vel_vector2
        self.kill()
    