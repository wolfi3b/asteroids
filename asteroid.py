import random

import pygame.draw
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from explosion import Explosion


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.num_vertices = random.randint(8, 30)


    def draw(self, screen):
        angle_step = 360 / self.num_vertices
        vertices = []

        for i in range(self.num_vertices):
            angle = i * angle_step
            distance = self.radius + i
            vertex = pygame.Vector2(distance, 0).rotate(angle) + self.position
            vertices.append(vertex)
        vertices = vertices

        pygame.draw.polygon(screen, "white", vertices, 2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        explosion = Explosion(self.position, self.radius)
        explosion.add(self.containers)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        left_velocity = self.velocity.rotate(random_angle)
        right_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = left_velocity * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = right_velocity * 1.2
