import random

import pygame.sprite


class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, radius):
        super().__init__()
        self.position = position
        self.radius = radius
        self.lifetime = 0.5
        self.elapsed_time = 0

        self.particles = []

        num_particles = random.randint(10, 20)
        for _ in range(num_particles):
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 150)
            velocity = pygame.Vector2(speed, 0).rotate(angle)
            self.particles.append({
                'position': pygame.Vector2(position),
                'velocity': velocity,
                'radius': random.uniform(2, 5)
            })

    def update(self, dt):
        self.elapsed_time += dt
        if self.elapsed_time > self.lifetime:
            self.kill()
        for particle in self.particles:
            particle['position'] += particle['velocity'] * dt


    def draw(self, screen):
        # alpha = max(0, 255 * (1 - self.elapsed_time / self.lifetime))
        # color = (255, 255, 255, alpha)
        # pygame.draw.circle(screen, color, self.position, int(self.radius * (1 - self.elapsed_time / self.lifetime)))
        alpha = max(0, 255 * (1 - self.elapsed_time / self.lifetime))
        for particle in self.particles:
            color = (255, 0, 0, alpha)
            pygame.draw.circle(screen, color, particle['position'], int(particle['radius']))
