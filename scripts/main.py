import pygame
import sys
from player import Player
from tilemap import TileMap

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zelda Style Game")

clock = pygame.time.Clock()

# Load the Map
map = TileMap('assets/maps/level1.tmx')
map_img = map.make_map()
map_rect = map_img.get_rect()

# Create player instance
player = Player((WIDTH // 2, HEIGHT // 2))

# Sprite group to update/draw everything
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main loop
running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(keys)

    # Draw everything
    screen.blit(map_img,map_rect)
    all_sprites.draw(screen)

    #screen.fill((30, 30, 30))  # Dark gray background
    #all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
