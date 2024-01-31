import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
PINK = (255, 182, 193)

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

    if keys[pygame.K_RIGHT]:
        cursor_rect.x += 5
        # Check for strict collision with the right window wall of room_pink
        if current_room == room_pink and cursor_rect.right > WIDTH:
            cursor_rect.right = WIDTH

    if keys[pygame.K_UP]:
        cursor_rect.y -= 5
        # Check for strict collision with the top window wall of room_pink
        if current_room == room_pink and cursor_rect.top < 0:
            cursor_rect.top = 0

    if keys[pygame.K_DOWN]:
        cursor_rect.y += 5

    # Check for collision with the north wall and teleport to the pink room
    if cursor_rect.top < 0:
        current_room = room_pink
        cursor_rect.topleft = (WIDTH // 2, HEIGHT - 20)  # Teleport to the bottom of the pink room

    # Check for collision with the south wall of the pink room and go back to the white room
    if current_room == room_pink and cursor_rect.bottom > HEIGHT:
        current_room = room_white
        cursor_rect.topleft = (WIDTH // 2, 0)  # Teleport to the top of the white room

    # Draw the current room and cursor
    screen.blit(current_room, (0, 0))
    screen.blit(cursor, cursor_rect.topleft)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
