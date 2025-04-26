import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # Camera offset
        self.offset = pygame.math.Vector2()

        # To center the camera on the player
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        self.player = None  # We will set this later

    def center_target(self, target):
        """Center the camera on the target sprite (player)."""
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height

    def custom_draw(self, player):
        """Draw all sprites relative to the camera offset."""
        self.center_target(player)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.copy()
            offset_rect.topleft -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
