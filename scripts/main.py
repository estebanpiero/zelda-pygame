import pygame
import sys
from player import Player
from tilemap import TileMap
from camera import CameraGroup
from enemy import Enemy

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zelda Style Game")

clock = pygame.time.Clock()

# Load the Map
tilemap = TileMap('assets/maps/map.tmx')

# Create player instance
player = Player((WIDTH // 2, HEIGHT // 2))

# Sprite group to update/draw everything
camera_group = CameraGroup(tilemap)
camera_group.add(player)


# Create enemy instance
enemy = Enemy((500, 500), camera_group, tilemap.walls)




# Main loop
running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    camera_group.update(tilemap.walls)

    # Draw everything
    
    camera_group.custom_draw(player)

    #screen.fill((30, 30, 30))  # Dark gray background
    #all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
