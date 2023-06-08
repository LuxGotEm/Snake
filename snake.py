import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Define the snake and food
snake_block_size = 20
snake_speed = 15
snake_list = []
snake_length = 1
snake_head = [window_width / 2, window_height / 2]
food_x = round(random.randrange(0, window_width - snake_block_size) / 20) * 20
food_y = round(random.randrange(0, window_height - snake_block_size) / 20) * 20

# Define the direction of the snake
direction = "RIGHT"
change_to = direction

# Define the game over condition
game_over = False

# Define the function to draw the snake on the screen
def draw_snake(snake_block_size, snake_list):
    for segment in snake_list:
        pygame.draw.rect(window, green, [segment[0], segment[1], snake_block_size, snake_block_size])

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"

    # Update the direction of the snake
    direction = change_to

    # Update the position of the snake's head
    if direction == "RIGHT":
        snake_head[0] += snake_block_size
    elif direction == "LEFT":
        snake_head[0] -= snake_block_size
    elif direction == "UP":
        snake_head[1] -= snake_block_size
    elif direction == "DOWN":
        snake_head[1] += snake_block_size

    # Check if the snake hits the boundaries
    if snake_head[0] >= window_width or snake_head[0] < 0 or snake_head[1] >= window_height or snake_head[1] < 0:
        game_over = True

    # Check if the snake hits itself
    for segment in snake_list[1:]:
        if segment == snake_head:
            game_over = True

    # Update the snake's body
    snake_list.append(list(snake_head))
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Draw the snake and food on the screen
    window.fill(black)
    draw_snake(snake_block_size, snake_list)
    pygame.draw.rect(window, red, [food_x, food_y, snake_block_size, snake_block_size])

    # Update the display
    pygame.display.update()

    # Check if the snake eats the food
    if snake_head[0] == food_x and snake_head[1] == food_y:
        food_x = round(random.randrange(0, window_width - snake_block_size) / 20) * 20
        food_y = round(random.randrange(0, window_height - snake_block_size) / 20) * 20
        snake_length += 1

    # Set the game speed
    pygame.time.Clock().tick(snake_speed)

# Quit the game
pygame.quit()
