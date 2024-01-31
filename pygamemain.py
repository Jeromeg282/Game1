import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
PINK = (255, 182, 193)
BLUE = (0, 191, 255)
TOMATO = (255, 99, 71)
GREEN = (60, 179, 113)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Navigation Game")

# Create the player cursor
cursor = pygame.Surface((20, 20))
cursor.fill((0, 0, 0))  # Black color for the cursor
cursor_rect = cursor.get_rect()
cursor_rect.topleft = (WIDTH // 2, HEIGHT // 2)

# Create the rooms
room_white = pygame.Surface((WIDTH, HEIGHT))
room_white.fill(WHITE)

room_pink = pygame.Surface((WIDTH, HEIGHT))
room_pink.fill(PINK)

room_blue = pygame.Surface((WIDTH, HEIGHT))
room_blue.fill(BLUE)

room_tomato = pygame.Surface((WIDTH, HEIGHT))
room_tomato.fill(TOMATO)

room_green = pygame.Surface((WIDTH, HEIGHT))
room_green.fill(GREEN)

current_room = room_white

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move the cursor
    if keys[pygame.K_LEFT]:
        cursor_rect.x -= 5
        # Check for strict collision with the left window wall of room_pink
        if current_room == room_pink and cursor_rect.left < 0:
            cursor_rect.left = 0
        # Check for strict collision with the left window wall of room_blue
        elif current_room == room_blue and cursor_rect.left < 0:
            cursor_rect.left = 0
        # Check for strict collision with the left window wall of room_green
        elif current_room == room_green and cursor_rect.left < 0:
            cursor_rect.left = 0

    if keys[pygame.K_RIGHT]:
        cursor_rect.x += 5
        # Check for strict collision with the right window wall of room_pink
        if current_room == room_pink and cursor_rect.right > WIDTH:
            cursor_rect.right = WIDTH
        # Check for strict collision with the right window wall of room_blue
        elif current_room == room_blue and cursor_rect.right > WIDTH:
            cursor_rect.right = WIDTH
        # Check for strict collision with the right window wall of room_tomato
        elif current_room == room_tomato and cursor_rect.right > WIDTH:
            cursor_rect.right = WIDTH

        # Check for collision with the east wall of the white room and teleport to room_tomato
        elif current_room == room_white and cursor_rect.right > WIDTH:
            current_room = room_tomato
            cursor_rect.topleft = (0, HEIGHT // 2)  # Teleport to the left side of the room_tomato

    if keys[pygame.K_UP]:
        cursor_rect.y -= 5
        # Check for strict collision with the top window wall of room_pink
        if current_room == room_pink and cursor_rect.top < 0:
            cursor_rect.top = 0
        # Check for strict collision with the top window wall of room_tomato
        elif current_room == room_tomato and cursor_rect.top < 0:
            cursor_rect.top = 0
        # Check for strict collision with the top window wall of room_green
        elif current_room == room_green and cursor_rect.top < 0:
            cursor_rect.top = 0

        # Check for collision with the north wall of the blue room and go back to the white room
        elif current_room == room_blue and cursor_rect.top < 0:
            current_room = room_white
            cursor_rect.topleft = (WIDTH // 2, HEIGHT - 20)  # Teleport to the bottom of the white room

    if keys[pygame.K_DOWN]:
        cursor_rect.y += 5
        # Check for strict collision with the south window wall of room_blue
        if current_room == room_blue and cursor_rect.bottom > HEIGHT:
            cursor_rect.bottom = HEIGHT
        # Check for strict collision with the south window wall of room_tomato
        elif current_room == room_tomato and cursor_rect.bottom > HEIGHT:
            cursor_rect.bottom = HEIGHT
        # Check for strict collision with the south window wall of room_green
        elif current_room == room_green and cursor_rect.bottom > HEIGHT:
            cursor_rect.bottom = HEIGHT

        # Check for collision with the south wall of the white room and teleport to room_blue
        elif current_room == room_white and cursor_rect.bottom > HEIGHT:
            current_room = room_blue
            cursor_rect.topleft = (WIDTH // 2, 0)  # Teleport to the top of the room_blue

    # Check for collision with the north wall and teleport to the pink room
    if cursor_rect.top < 0:
        current_room = room_pink
        cursor_rect.topleft = (WIDTH // 2, HEIGHT - 20)  # Teleport to the bottom of the pink room

    # Check for collision with the south wall of the pink room and go back to the white room
    if current_room == room_pink and cursor_rect.bottom > HEIGHT:
        current_room = room_white
        cursor_rect.topleft = (WIDTH // 2, 0)  # Teleport to the top of the white room

    # Check for strict collision with the east wall of room_tomato
    if current_room == room_tomato and cursor_rect.right > WIDTH:
        cursor_rect.right = WIDTH

    # Check for collision with the west wall of room_tomato and go back to the white room
    if current_room == room_tomato and cursor_rect.left < 0:
        current_room = room_white
        cursor_rect.topleft = (WIDTH // 2, HEIGHT // 2)  # Teleport to the center of the white room

    # Check for collision with the west wall of room_green and teleport to room_green
    if current_room == room_white and cursor_rect.left < 0:
        current_room = room_green
        cursor_rect.topright = (WIDTH, cursor_rect.centery)  # Teleport to the right side of the room_green

    # Check for strict collision with the north wall of room_green
    if current_room == room_green and cursor_rect.top < 0:
        cursor_rect.top = 0

    # Check for strict collision with the west wall of room_green
    if current_room == room_green and cursor_rect.left < 0:
        cursor_rect.left = 0

    # Check for strict collision with the south wall of room_green
    if current_room == room_green and cursor_rect.bottom > HEIGHT:
        cursor_rect.bottom = HEIGHT

    # Check for collision with the east wall of room_green and go back to the white room
    if current_room == room_green and cursor_rect.right > WIDTH:
        current_room = room_white
        cursor_rect.topleft = (0, cursor_rect.centery)  # Teleport to the left side of the white room

    # Draw the current room and cursor
    screen.blit(current_room, (0, 0))
    screen.blit(cursor, cursor_rect.topleft)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
