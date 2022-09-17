import pygame, random
from sys import exit #exits code right after it runs

#starts and initiates pygames
pygame.init()

#Create display surface (the screen players see)
#screen = pygame.displat.set.mode((width, height))
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PowerPuffs')
clock = pygame.time.Clock() #Helps with time and controlling the frame rate
test_font = pygame.font.Font('Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()
text_surface = test_font.render('PuffGirls', False, 'Black')

mojo_jojo_surface = pygame.image.load('mojojojo.png')
mojo_jojo_surface = pygame.transform.scale(mojo_jojo_surface, (120, 100)).convert_alpha()
mojo_rect = mojo_jojo_surface.get_rect(bottomright = (600,310))

bubbles_surface = pygame.image.load('blue.png')
bubbles_surface = pygame.transform.scale(bubbles_surface, (120,120)).convert_alpha()
bubbles_rect = bubbles_surface.get_rect(midbottom = (80,310))
bubbles_gravity = -15

crushed_can_surface = pygame.image.load('crushedCan.png').convert_alpha()
crushed_can_surface = pygame.transform.scale(crushed_can_surface, (75, 75)).convert_alpha()
crushed_can_rect = crushed_can_surface.get_rect(midbottom = (random.randrange(0, 800), 0))
crushed_can_gravity = -5

recyclingbin_surface = pygame.image.load('recyclingbin.png').convert_alpha()
recyclingbin_surface = pygame.transform.scale(recyclingbin_surface, (100, 100)).convert_alpha()
recyclingbin_rect = recyclingbin_surface.get_rect(midbottom = (0, 250))

trashcan_surface = pygame.image.load('trashcan.png').convert_alpha()
trashcan_surface = pygame.transform.scale(trashcan_surface, (75, 75)).convert_alpha()
recyclingbin_rect = trashcan_surface.get_rect(midbottom = (800, 250))

score = 0
#Keeps code running forever
while True:
    pygame.display.set_caption(str(score))
    # Player input; Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite of init(); closes pygame
            exit()
      # if event.type == pygame.MOUSEMOTION:
        # if   bubbles_rect.collidepoint(event.pos): print('collision')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bubbles_gravity = -20
            # if event.key == pygame.K_LEFT:
            #     bubbles_rect.x -= 20
            # if event.key == pygame.K_RIGHT:
            #     bubbles_rect.x += 20

    # places image ontop of display surface
    # anything in this while loop will be displayed to the player
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    screen.blit(recyclingbin_surface, (0, 230))
    screen.blit(trashcan_surface, (700, 230))

    mojo_rect.x -= 2
    if mojo_rect.right <= 0: mojo_rect.left = 800
    screen.blit(mojo_jojo_surface, mojo_rect)

    #crushed can
    crushed_can_rect.y += 2
    if crushed_can_rect.y > 300:
        crushed_can_rect = crushed_can_surface.get_rect(midbottom=(random.randrange(0, 800), 0))
    screen.blit(crushed_can_surface, crushed_can_rect)

   #bubbles
    bubbles_gravity += 1
    bubbles_rect.y += bubbles_gravity
    if bubbles_rect.bottom >= 300: bubbles_rect.bottom = 315
    screen.blit(bubbles_surface, (bubbles_rect))

    if bubbles_rect.colliderect(mojo_rect):
        print('collision')

    if bubbles_rect.colliderect(crushed_can_rect):
        score += 1;

    pygame.display.update()
    clock.tick(60) #tells the while loop to not run faster than 60