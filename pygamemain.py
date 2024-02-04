import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Navigation Game")

# Create the player (black box)
player_color = (0, 0, 0)  # Black color for the player
player_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)

# Load chest image and scale to the original red block size
chest_image = pygame.transform.scale(pygame.image.load("chest.png").convert_alpha(), (50, 50))  # Replace "chest.png" with the actual image file
chest_rect = pygame.Rect(200, 200, 50, 50)  # Adjust the coordinates and dimensions as needed

font = pygame.font.Font(None, 36)

chest_opened = False

# Create the rooms with PNG background images
room_white = pygame.image.load("room_white.png").convert_alpha()
room_pink = pygame.image.load("room_pink.png").convert_alpha()
room_blue = pygame.image.load("room_blue.png").convert_alpha()
room_tomato = pygame.image.load("room_tomato.png").convert_alpha()
room_green = pygame.image.load("room_green.png").convert_alpha()

current_room = room_white

# Game loop
running = True
chest_open_time = 0  # Variable to store the time when the chest was opened

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                # Check if the cursor is near the chest in room_green
                if current_room == room_green and player_rect.colliderect(chest_rect):
                    chest_opened = True
                    chest_open_time = current_time
    keys = pygame.key.get_pressed()

    # Move the player (black box)
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
        # Check for strict collision with the left window wall of room_pink
        if current_room == room_pink and player_rect.left < 0:
            player_rect.left = 0
        # Check for strict collision with the left window wall of room_blue
        elif current_room == room_blue and player_rect.left < 0:
            player_rect.left = 0
        # Check for strict collision with the left window wall of room_green
        elif current_room == room_green and player_rect.left < 0:
            player_rect.left = 0

    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
        # Check for strict collision with the right window wall of room_pink
        if current_room == room_pink and player_rect.right > WIDTH:
            player_rect.right = WIDTH
        # Check for strict collision with the right window wall of room_blue
        elif current_room == room_blue and player_rect.right > WIDTH:
            player_rect.right = WIDTH
        # Check for strict collision with the right window wall of room_tomato
        elif current_room == room_tomato and player_rect.right > WIDTH:
            player_rect.right = WIDTH

        # Check for collision with the east wall of the white room and teleport to room_tomato
        elif current_room == room_white and player_rect.right > WIDTH:
            current_room = room_tomato
            player_rect.topleft = (0, HEIGHT // 2)  # Teleport to the left side of the room_tomato

    if keys[pygame.K_UP]:
        player_rect.y -= 5
        # Check for strict collision with the top window wall of room_pink
        if current_room == room_pink and player_rect.top < 0:
            player_rect.top = 0
        # Check for strict collision with the top window wall of room_tomato
        elif current_room == room_tomato and player_rect.top < 0:
            player_rect.top = 0
        # Check for strict collision with the top window wall of room_green
        elif current_room == room_green and player_rect.top < 0:
            player_rect.top = 0

        # Check for collision with the north wall of the blue room and go back to the white room
        elif current_room == room_blue and player_rect.top < 0:
            current_room = room_white
            player_rect.topleft = (WIDTH // 2, HEIGHT - 20)  # Teleport to the bottom of the white room

    if keys[pygame.K_DOWN]:
        player_rect.y += 5
        # Check for strict collision with the south window wall of room_blue
        if current_room == room_blue and player_rect.bottom > HEIGHT:
            player_rect.bottom = HEIGHT
        # Check for strict collision with the south window wall of room_tomato
        elif current_room == room_tomato and player_rect.bottom > HEIGHT:
            player_rect.bottom = HEIGHT
        # Check for strict collision with the south window wall of room_green
        elif current_room == room_green and player_rect.bottom > HEIGHT:
            player_rect.bottom = HEIGHT

        # Check for collision with the south wall of the white room and teleport to room_blue
        elif current_room == room_white and player_rect.bottom > HEIGHT:
            current_room = room_blue
            player_rect.topleft = (WIDTH // 2, 0)  # Teleport to the top of the room_blue

    # Check for collision with the north wall and teleport to the pink room
    if player_rect.top < 0:
        current_room = room_pink
        player_rect.topleft = (WIDTH // 2, HEIGHT - 20)  # Teleport to the bottom of the pink room

    # Check for collision with the south wall of the pink room and go back to the white room
    if current_room == room_pink and player_rect.bottom > HEIGHT:
        current_room = room_white
        player_rect.topleft = (WIDTH // 2, 0)  # Teleport to the top of the white room

    # Check for strict collision with the east wall of room_tomato
    if current_room == room_tomato and player_rect.right > WIDTH:
        player_rect.right = WIDTH

    # Check for collision with the west wall of room_tomato and go back to the white room
    if current_room == room_tomato and player_rect.left < 0:
        current_room = room_white
        player_rect.topleft = (WIDTH // 2, HEIGHT // 2)  # Teleport to the center of the white room

    # Check for collision with the west wall of room_green and teleport to room_green
    if current_room == room_white and player_rect.left < 0:
        current_room = room_green
        player_rect.topright = (WIDTH, player_rect.centery)  # Teleport to the right side of the room_green

    # Check for strict collision with the north wall of room_green
    if current_room == room_green and player_rect.top < 0:
        player_rect.top = 0

    # Check for strict collision with the west wall of room_green
    if current_room == room_green and player_rect.left < 0:
        player_rect.left = 0

    # Check for strict collision with the south wall of room_green
    if current_room == room_green and player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    # Check for collision with the east wall of room_green and go back to the white room
    if current_room == room_green and player_rect.right > WIDTH:
        current_room = room_white
        player_rect.topleft = (0, player_rect.centery)  # Teleport to the left side of the white room

    # Draw the current room, player, chest, and interaction text
    screen.blit(current_room, (0, 0))
    pygame.draw.rect(screen, player_color, player_rect)  # Draw player rectangle

    if current_room == room_green:
        screen.blit(chest_image, chest_rect.topleft)  # Draw chest image

        distance_to_chest = pygame.math.Vector2(chest_rect.center) - pygame.math.Vector2(player_rect.center)
        if distance_to_chest.length() < 50:  # Adjust the interaction distance as needed
            interaction_text = font.render("Press E to open chest", True, (255, 255, 255))
            text_rect = interaction_text.get_rect(center=chest_rect.center)
            screen.blit(interaction_text, text_rect.topleft)

    if chest_opened:
        message_surface = font.render("You opened the chest!", True, (255, 255, 255))
        message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(message_surface, message_rect.topleft)

        if current_time - chest_open_time > 3000:
            chest_opened = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
