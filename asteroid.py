import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, pygame.Color(255, 255, 255), self.position, self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self._spawn()

    def _spawn(self):
        rng = random.randrange(20, 50)
        dir1 = self.velocity.rotate(rng)
        dir2 = self.velocity.rotate(-rng)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child1.velocity = dir1 * 1.2
        child2 = Asteroid(self.position.x, self.position.y, new_radius)
        child2.velocity = dir2 * 1.2
