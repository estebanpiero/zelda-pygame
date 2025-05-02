import pygame
import pytmx

class TileMap:
    def __init__(self, filename):
        self.tmxdata = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

        # Create a surface for the entire map
        self.image = pygame.Surface((self.width, self.height))
        self.render(self.image)
        self.rect = self.image.get_rect()

        # Wall Detection

        self.walls = []
        self.load_walls()

    def load_walls(self):
            """Load wall rects from the 'collision' layer."""
            for layer in self.tmxdata.visible_layers:
                if layer.name == 'collision':  # <--- Your collision layer name
                    for x, y, gid in layer:
                        if gid:  # If there is a tile (not empty)
                            wall_rect = pygame.Rect(
                                x * self.tmxdata.tilewidth,
                                y * self.tmxdata.tileheight,
                                self.tmxdata.tilewidth,
                                self.tmxdata.tileheight
                            )
                            self.walls.append(wall_rect)

    def render(self, surface):
        """Draw all tiles onto the given surface."""
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def draw(self, surface, offset):
        """Blit the map surface with camera offset."""
        surface.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))
