import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # Load the full spritesheet
        self.import_player_assets()

        # Set up first image and rect
        self.frame_index = 0
        self.status = 'down'
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.animation_speed = 0.15

    def import_player_assets(self):
        """Load and slice the spritesheet into frames."""
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}
        
        sheet = pygame.image.load('assets/player/player_spritesheet.png').convert_alpha()

        frame_width = sheet.get_width() // 3
        frame_height = sheet.get_height() // 4

        directions = ['down', 'left', 'right', 'up']

        for row_index, direction in enumerate(directions):
            for frame_index in range(3):  # 3 frames per direction
                x = frame_index * frame_width
                y = row_index * frame_height
                frame = sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))
                self.animations[direction].append(frame)



    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

    def check_collision(self, walls, direction):
        """Undo movement if colliding with a wall."""
        for wall in walls:
            if self.rect.colliderect(wall):
                if direction == 'horizontal':
                    if self.direction.x > 0:  # Moving right
                        self.rect.right = wall.left
                    if self.direction.x < 0:  # Moving left
                        self.rect.left = wall.right
                if direction == 'vertical':
                    if self.direction.y > 0:  # Moving down
                        self.rect.bottom = wall.top
                    if self.direction.y < 0:  # Moving up
                        self.rect.top = wall.bottom

    def move(self, walls):
        """Move and check collision."""
        # Move horizontally
        self.rect.x += self.direction.x * self.speed
        self.check_collision(walls, 'horizontal')

        # Move vertically
        self.rect.y += self.direction.y * self.speed
        self.check_collision(walls, 'vertical')

    def animate(self):
        animation = self.animations[self.status]

        if self.direction.magnitude() != 0:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(animation):
                self.frame_index = 0
        else:
            self.frame_index = 1  # Stay on middle frame when idle (optional tweak)

        self.image = animation[int(self.frame_index)]

    def update(self, walls):
        self.input()
        self.move(walls)
        self.animate()
