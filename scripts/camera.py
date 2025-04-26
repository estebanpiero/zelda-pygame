import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self, tilemap):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        self.tilemap = tilemap  # <-- Save the TileMap here!

        self.player = None  # We will set this later



    def center_target(self, target):
        """Center the camera on the target sprite (player)."""
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height

    def custom_draw(self, player):
        self.center_target(player)

        # Draw the map
        self.tilemap.draw(self.display_surface, self.offset)

        # Draw all sprites
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
