import pygame
from sys import exit #exits code right after it runs

#starts and initiates pygames
pygame.init()

#Create display surface (the screen players see)
#screen = pygame.displat.set.mode((width, height))
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PowerPuffs')
clock = pygame.time.Clock() #Helps with time and controlling the frame rate
test_font = pygame.font.Font('Pixeltype.ttf', 50)
y = 310

direction = pygame.math.Vector2()

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()
text_surface = test_font.render('PuffGirls', False, 'Black')

mojo_jojo_surface = pygame.image.load('mojojojo.png')
mojo_jojo_surface = pygame.transform.scale(mojo_jojo_surface, (120, 100)).convert_alpha()
mojo_rect = mojo_jojo_surface.get_rect(bottomright = (600,310))

bubbles_surface = pygame.image.load('blue.png').convert_alpha()
bubbles_surface = pygame.transform.scale(bubbles_surface, (120,120)).convert_alpha()
bubbles_rect = bubbles_surface.get_rect(midbottom = (80,y))
bubbles_gravity = -15
running = True
#player_running = 0

#Keeps code running forever
while running:
    # Player input; Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite of init(); closes pygame
            exit()
      # if event.type == pygame.MOUSEMOTION:
        # if   bubbles_rect.collidepoint(event.pos): print('collision')

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bubbles_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bubbles_rect.x += -100

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                bubbles_rect.x += 100



    # places image ontop of display surface
    # anything in this while loop will be displayed to the player
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))

    mojo_rect.x -= 2
    if mojo_rect.right <= 0: mojo_rect.left = 800
    screen.blit(mojo_jojo_surface, mojo_rect)

   #bubbles
    bubbles_gravity += 1
    bubbles_rect.y += bubbles_gravity
    if bubbles_rect.bottom >= 300: bubbles_rect.bottom = 315
    screen.blit(bubbles_surface, (bubbles_rect))

    if bubbles_rect.colliderect(mojo_rect):
        print('collision')

    pygame.display.update()
    clock.tick(60) #tells the while loop to not run faster than 60
