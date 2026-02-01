import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)

# Snake and food setup
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, WIDTH//BLOCK_SIZE) * BLOCK_SIZE,
            random.randrange(1, HEIGHT//BLOCK_SIZE) * BLOCK_SIZE]
food_spawn = True

# Movement
direction = 'RIGHT'
change_to = direction

# Speed
speed = 15
clock = pygame.time.Clock()

# Score function
def show_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

# Game loop
running = True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    # Move snake
    if direction == 'UP':
        snake_pos[1] -= BLOCK_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += BLOCK_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= BLOCK_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += BLOCK_SIZE

    # Snake body growing
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    # Food spawn
    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH//BLOCK_SIZE) * BLOCK_SIZE,
                    random.randrange(1, HEIGHT//BLOCK_SIZE) * BLOCK_SIZE]
        food_spawn = True

    # Draw snake and food
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    # Game Over conditions
    if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
        snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
        running = False
    for block in snake_body[1:]:
        if snake_pos == block:
            running = False

    show_score(len(snake_body) - 3)
    pygame.display.update()
    clock.tick(speed)

pygame.quit()


