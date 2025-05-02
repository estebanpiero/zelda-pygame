import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, walls):
        super().__init__(groups)
        self.image = pygame.image.load('assets/graphics/enemies/enemy.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(1, 0)  # Initial direction
        self.speed = 1
        self.walls = walls
        self.move_timer = 0  # Track time to change direction

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed
        self.check_collision('horizontal')
        self.rect.y += self.direction.y * self.speed
        self.check_collision('vertical')

        self.move_timer += dt
        if self.move_timer > 3000:  # Change direction every 3 seconds
            self.move_timer = 0
            self.direction = pygame.math.Vector2.random().normalize()

    def check_collision(self, direction):
        for wall in self.walls:
            if self.rect.colliderect(wall):
                if direction == 'horizontal':
                    if self.direction.x > 0:
                        self.rect.right = wall.left
                    else:
                        self.rect.left = wall.right
                if direction == 'vertical':
                    if self.direction.y > 0:
                        self.rect.bottom = wall.top
                    else:
                        self.rect.top = wall.bottom
