import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, direction: pygame.Vector2):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = direction * PLAYER_SHOT_SPEED

    def draw(self, screen):
        pygame.draw.line(
            screen,
            pygame.Color(255, 255, 255),
            self.position - self.velocity.normalize() * SHOT_RADIUS,
            self.position + self.velocity.normalize() * SHOT_RADIUS,
            SHOT_RADIUS,
        )

    def update(self, dt):
        self.position += self.velocity * dt
