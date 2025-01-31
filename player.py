import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        self.rotation = 0
        super().__init__(x, y, PLAYER_RADIUS)
        self.shot_cooldown = 0

    def triangle(self):

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color(255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.shot_cooldown <= 0:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
            self.shoot()
        self.shot_cooldown -= dt

    def move(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt

    def shoot(self):
        pos_0 = self.position
        dir = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet = Shot(pos_0.x, pos_0.y, dir)
