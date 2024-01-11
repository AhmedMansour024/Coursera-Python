import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Create the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake attributes
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_dir = (0, 0)
snake_speed = 0.5

# Food attributes
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    win.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_dir = (1, 0)
    
    # Update snake position
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake = [new_head] + snake[:-1]

    # Check for collisions
    if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
        new_head in snake[1:]):
        running = False
    
    # Check if snake eats food
    if new_head == food:
        snake.append(snake[-1])
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(win, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    # Draw food
    pygame.draw.rect(win, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
