#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Treasure Hunt Game")

# Define classes
class Treasure:
    def __init__(self):
        self.x = random.randint(50, SCREEN_WIDTH - 50)
        self.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.radius = 20
        self.color = RED

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = 25
        self.color = WHITE

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Initialize game objects
player = Player()
treasures = [Treasure() for _ in range(10)]

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if player clicked on a treasure
                for treasure in treasures:
                    distance = ((treasure.x - player.x)**2 + (treasure.y - player.y)**2)**0.5
                    if distance <= player.radius + treasure.radius:
                        treasures.remove(treasure)

    # Update game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Draw everything
    screen.fill(BLACK)
    for treasure in treasures:
        treasure.draw(screen)
    player.draw(screen)
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()


# In[ ]:




