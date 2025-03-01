from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2 )

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20.0, 50.0)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            velocity1 = self.velocity * 1.2
            velocity1 = velocity1.rotate(-split_angle)
            child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_1.velocity = velocity1
            velocity2 = self.velocity * 1.2
            velocity2 = velocity2.rotate(split_angle)
            child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            child_asteroid_2.velocity = velocity2