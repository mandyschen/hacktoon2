import pygame, random
from gui import GameGUI
from sys import exit #exits code right after it runs

from pygame.examples.eventlist import font

# starts and initiates pygames
pygame.init()
# Load and play background soundtrack
gui = GameGUI()
gui.start()
gui.play_sound('game-soundtrack')

# Create display surface (the screen players see)
# screen = pygame.displat.set.mode((width, height))
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PowerPuffs')
clock = pygame.time.Clock()  # Helps with time and controlling the frame rate
test_font = pygame.font.Font('Pixeltype.ttf', 50)

sky_surface = pygame.image.load('./images/Sky.png').convert()
ground_surface = pygame.image.load('./images/ground.png').convert()
text_surface = test_font.render('PuffGirls', False, 'Black')

mojo_jojo_surface = pygame.image.load('./images/mojojojo.png')
mojo_jojo_surface = pygame.transform.scale(mojo_jojo_surface, (120, 100)).convert_alpha()
mojo_rect = mojo_jojo_surface.get_rect(bottomright=(600, 310))

bubbles_surface = pygame.image.load('./images/blue.png')
bubbles_surface = pygame.transform.scale(bubbles_surface, (120,120)).convert_alpha()
bubbles_rect = bubbles_surface.get_rect(midbottom = (80,310))
bubbles_gravity = -15
bubbles_velocity = 5

crushed_can_surface = pygame.image.load('./images/crushedCan.png').convert_alpha()
crushed_can_surface = pygame.transform.scale(crushed_can_surface, (75, 75)).convert_alpha()
crushed_can_rect = crushed_can_surface.get_rect(midbottom = (random.randrange(50, 750), 0))
crushed_can_gravity = -3

cherry_surface = pygame.image.load('cherry.png').convert_alpha()
cherry_surface = pygame.transform.scale(cherry_surface, (75, 75)).convert_alpha()
cherry_rect = cherry_surface.get_rect(midbottom = (random.randrange(50, 750), random.randrange(-75, -50)))
cherry_gravity = -3

recyclingbin_surface = pygame.image.load('./images/recyclingbin.png').convert_alpha()
recyclingbin_surface = pygame.transform.scale(recyclingbin_surface, (100, 100)).convert_alpha()
recyclingbin_rect = recyclingbin_surface.get_rect(midbottom = (0, 250))

trashcan_surface = pygame.image.load('./images/trashcan.png').convert_alpha()
trashcan_surface = pygame.transform.scale(trashcan_surface, (75, 75)).convert_alpha()
trashcan_rect = trashcan_surface.get_rect(midbottom = (800, 250))

over_font = pygame.font.Font('freesansbold.ttf', 64)

score = 0

active = True


def isCollision(x1, y1, x2, y2):
    distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    if distance < 27:
        return True

needRecycle = False
needCompost = False
torf = False



# Keeps code running forever
while True:
    pygame.display.set_caption(str(score))
    # Player input; Exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # opposite of init(); closes pygame
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bubbles_rect.y == 195:
                    bubbles_gravity = -20
            if event.key == pygame.K_LEFT:
                bubbles_velocity = bubbles_velocity - 5
            if event.key == pygame.K_RIGHT:
                bubbles_velocity = bubbles_velocity + 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                bubbles_velocity = 0
            if event.key == pygame.K_RIGHT:
                bubbles_velocity = 0

    # places image ontop of display surface
    # anything in this while loop will be displayed to the player
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(recyclingbin_surface, (0, 230))
    screen.blit(trashcan_surface, (700, 230))

    mojo_rect.x -= 2
    if mojo_rect.right <= 0: mojo_rect.left = 800
    screen.blit(mojo_jojo_surface, mojo_rect)

    # crushed can
    crushed_can_rect.y += 2
    if crushed_can_rect.y > 300:
        crushed_can_rect = crushed_can_surface.get_rect(midbottom=(random.randrange(50, 750), 0))
    screen.blit(crushed_can_surface, crushed_can_rect)

    # cherry
    cherry_rect.y += 1
    if cherry_rect.y > 300:
        cherry_rect = cherry_surface.get_rect(midbottom=(random.randrange(50, 750), random.randrange(-75, -50)))
    screen.blit(cherry_surface, cherry_rect)

    # bubbles
    bubbles_gravity += 1
    bubbles_rect.y += bubbles_gravity
    bubbles_rect.x += bubbles_velocity
    if bubbles_rect.x < 0:
        bubbles_rect.x = 0
    elif bubbles_rect.x > 700:
        bubbles_rect.x = 700
    if bubbles_rect.bottom >= 300: bubbles_rect.bottom = 315
    screen.blit(bubbles_surface, bubbles_rect)

    if bubbles_rect.colliderect(mojo_rect):
        print('collision')
    if bubbles_rect.colliderect(crushed_can_rect):
        crushed_can_rect.y = 300
        needRecycle = True

    if bubbles_rect.colliderect(cherry_rect):
        cherry_rect.y = 300
        needCompost = True

    if needRecycle:
        recycle_surface = test_font.render('RECYCLE', False, 'Green')
        screen.blit(recycle_surface, (50, 50))
    if needCompost:
        compost_surface = test_font.render('COMPOST', False, 'Brown')
        screen.blit(compost_surface, (600, 50))

    if needRecycle == True:
        if bubbles_rect.colliderect(recyclingbin_rect):
            score += 1
            needRecycle = False

    if needCompost == True:
        if bubbles_rect.colliderect(trashcan_rect):
            score += 1
            needCompost = False


    if (isCollision(bubbles_rect.x, bubbles_rect.y, mojo_rect.x, mojo_rect.y)):
        active = False
        clock.tick(0)
        break

    if(active):
        pygame.display.update()
        clock.tick(60)  # tells the while loop to not run faster than 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # opposite of init(); closes pygame
            exit()
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 200))
    pygame.display.update()
    clock.tick(60)