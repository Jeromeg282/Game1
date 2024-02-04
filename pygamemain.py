import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Navigation Game")


player_color = (0, 0, 0) 
player_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)


chest_image = pygame.transform.scale(pygame.image.load("chest.png").convert_alpha(), (50, 50)) 
chest_rect = pygame.Rect(200, 200, 50, 50)  
font = pygame.font.Font(None, 36)

chest_opened = False


room_white = pygame.image.load("room_white.png").convert_alpha()
room_pink = pygame.image.load("room_pink.png").convert_alpha()
room_blue = pygame.image.load("room_blue.png").convert_alpha()
room_tomato = pygame.image.load("room_tomato.png").convert_alpha()
room_green = pygame.image.load("room_green.png").convert_alpha()

current_room = room_white


running = True
chest_open_time = 0  

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
               
                if current_room == room_green and player_rect.colliderect(chest_rect):
                    chest_opened = True
                    chest_open_time = current_time
    keys = pygame.key.get_pressed()

   
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
        
        if current_room == room_pink and player_rect.left < 0:
            player_rect.left = 0
       
        elif current_room == room_blue and player_rect.left < 0:
            player_rect.left = 0
       
        elif current_room == room_green and player_rect.left < 0:
            player_rect.left = 0

    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
     
        if current_room == room_pink and player_rect.right > WIDTH:
            player_rect.right = WIDTH
      
        elif current_room == room_blue and player_rect.right > WIDTH:
            player_rect.right = WIDTH
       
        elif current_room == room_tomato and player_rect.right > WIDTH:
            player_rect.right = WIDTH

        
        elif current_room == room_white and player_rect.right > WIDTH:
            current_room = room_tomato
            player_rect.topleft = (0, HEIGHT // 2)  

    if keys[pygame.K_UP]:
        player_rect.y -= 5
        
        if current_room == room_pink and player_rect.top < 0:
            player_rect.top = 0
       
        elif current_room == room_tomato and player_rect.top < 0:
            player_rect.top = 0
     
        elif current_room == room_green and player_rect.top < 0:
            player_rect.top = 0

       
        elif current_room == room_blue and player_rect.top < 0:
            current_room = room_white
            player_rect.topleft = (WIDTH // 2, HEIGHT - 20) 

    if keys[pygame.K_DOWN]:
        player_rect.y += 5
        
        if current_room == room_blue and player_rect.bottom > HEIGHT:
            player_rect.bottom = HEIGHT
       
        elif current_room == room_tomato and player_rect.bottom > HEIGHT:
            player_rect.bottom = HEIGHT
        
        elif current_room == room_green and player_rect.bottom > HEIGHT:
            player_rect.bottom = HEIGHT

        
        elif current_room == room_white and player_rect.bottom > HEIGHT:
            current_room = room_blue
            player_rect.topleft = (WIDTH // 2, 0)  

   
    if player_rect.top < 0:
        current_room = room_pink
        player_rect.topleft = (WIDTH // 2, HEIGHT - 20)  

    
    if current_room == room_pink and player_rect.bottom > HEIGHT:
        current_room = room_white
        player_rect.topleft = (WIDTH // 2, 0)  

    
    if current_room == room_tomato and player_rect.right > WIDTH:
        player_rect.right = WIDTH

    
    if current_room == room_tomato and player_rect.left < 0:
        current_room = room_white
        player_rect.topleft = (WIDTH // 2, HEIGHT // 2)  

    
    if current_room == room_white and player_rect.left < 0:
        current_room = room_green
        player_rect.topright = (WIDTH, player_rect.centery)  

    
    if current_room == room_green and player_rect.top < 0:
        player_rect.top = 0

   
    if current_room == room_green and player_rect.left < 0:
        player_rect.left = 0

    
    if current_room == room_green and player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    
    if current_room == room_green and player_rect.right > WIDTH:
        current_room = room_white
        player_rect.topleft = (0, player_rect.centery) 

    
    screen.blit(current_room, (0, 0))
    pygame.draw.rect(screen, player_color, player_rect) 

    if current_room == room_green:
        screen.blit(chest_image, chest_rect.topleft) 

        distance_to_chest = pygame.math.Vector2(chest_rect.center) - pygame.math.Vector2(player_rect.center)
        if distance_to_chest.length() < 50:  
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
