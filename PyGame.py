import math

from gui import GameGUI
import pygame, random
from sys import exit  # exits code right after it runs

# starts and initiates pygames
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PowerPuffs')
clock = pygame.time.Clock()  # Helps with time and controlling the frame rate
test_font = pygame.font.Font('Pixeltype.ttf', 50)

# Load and play background soundtrack
gui = GameGUI()
gui.start()
gui.play_sound('game-soundtrack')

def playAgain():


    # Create display surface (the screen players see)
    # screen = pygame.display.set.mode((width, height))

    sky_surface = pygame.image.load('./images/Sky.png').convert()
    ground_surface = pygame.image.load('./images/ground.png').convert()

    mojo_jojo_surface = pygame.image.load('./images/mojojojo.png')
    mojo_jojo_surface = pygame.transform.scale(mojo_jojo_surface, (120, 100)).convert_alpha()
    mojo_rect = mojo_jojo_surface.get_rect(bottomright=(600, 310))

    bubbles_surface = pygame.image.load('./images/blue.png')
    bubbles_surface = pygame.transform.scale(bubbles_surface, (120, 120)).convert_alpha()
    bubbles_rect = bubbles_surface.get_rect(midbottom=(80, 310))
    bubbles_gravity = -15
    bubbles_velocity = 5

    # Recycling items

    crushed_can_surface = pygame.image.load('./images/crushedCan.png').convert_alpha()
    crushed_can_surface = pygame.transform.scale(crushed_can_surface, (75, 75)).convert_alpha()
    crushed_can_rect = crushed_can_surface.get_rect(midbottom=(random.randrange(50, 750), 0))
    crushed_can_gravity = -1

    paper_surface = pygame.image.load('./images/paper.png').convert_alpha()
    paper_surface = pygame.transform.scale(paper_surface, (60, 60)).convert_alpha()
    paper_rect = paper_surface.get_rect(midbottom=(random.randrange(50, 750), random.randrange(-75, -50)))
    paper_gravity = -3

    # Trash items

    cherry_surface = pygame.image.load('./images/cherry.png').convert_alpha()
    cherry_surface = pygame.transform.scale(cherry_surface, (75, 75)).convert_alpha()
    cherry_rect = cherry_surface.get_rect(midbottom=(random.randrange(50, 750), random.randrange(-75, -50)))
    cherry_gravity = -1

    bananapeel_surface = pygame.image.load('./images/bananapeel.png').convert_alpha()
    bananapeel_surface = pygame.transform.scale(bananapeel_surface, (75, 75)).convert_alpha()
    bananapeel_rect = bananapeel_surface.get_rect(midbottom=(random.randrange(50, 750), random.randrange(-75, -50)))
    bananapeel_gravity = -3

    recyclingbin_surface = pygame.image.load('./images/recyclingbin.png').convert_alpha()
    recyclingbin_surface = pygame.transform.scale(recyclingbin_surface, (100, 100)).convert_alpha()
    recyclingbin_rect = recyclingbin_surface.get_rect(midbottom=(0, 250))

    trashcan_surface = pygame.image.load('./images/trashcan.png').convert_alpha()
    trashcan_surface = pygame.transform.scale(trashcan_surface, (75, 75)).convert_alpha()
    trashcan_rect = trashcan_surface.get_rect(midbottom=(800, 250))

    over_font = pygame.font.Font('freesansbold.ttf', 64)

    score = 0

    facingRight = True

    color = 'blue'

    def isCollision(x1, y1, x2, y2):
        distance = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
        if distance < 50:
            return True

    needRecycle = False
    needCompost = False
    torf = False
    recycleAmount = 0
    compostAmount = 0
    speed = 1

    # Keeps code running forever
    while True:

        # Player input; Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # opposite of init(); closes pygame
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                    if bubbles_rect.y == 195:
                        bubbles_gravity = -20
                    elif bubbles_rect.y - 20 > 10:
                        bubbles_gravity = -10
                if event.key == pygame.K_1 and color != 'blue':
                    bubbles_surface = pygame.image.load('./images/blue.png')
                    bubbles_surface = pygame.transform.scale(bubbles_surface, (120, 120)).convert_alpha()
                    facingRight = True
                    color = 'blue'
                if event.key == pygame.K_2 and color != 'red':
                    bubbles_surface = pygame.image.load('./images/red.png')
                    bubbles_surface = pygame.transform.scale(bubbles_surface, (70, 110)).convert_alpha()
                    facingRight = True
                    color = 'red'
                if event.key == pygame.K_3 and color != 'green':
                    bubbles_surface = pygame.image.load('./images/green.png')
                    bubbles_surface = pygame.transform.scale(bubbles_surface, (90, 100)).convert_alpha()
                    facingRight = True
                    color = 'green'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    bubbles_velocity = bubbles_velocity - 5
                    if facingRight == True:
                        bubbles_surface = pygame.transform.flip(bubbles_surface, True, False)
                        facingRight = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    bubbles_velocity = bubbles_velocity + 5
                    if facingRight == False:
                        bubbles_surface = pygame.transform.flip(bubbles_surface, True, False)
                        facingRight = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    bubbles_velocity = 0
                if event.key == pygame.K_RIGHT:
                    bubbles_velocity = 0
                if event.key == pygame.K_a:
                    bubbles_velocity = 0
                if event.key == pygame.K_d:
                    bubbles_velocity = 0

        # places image ontop of display surface
        # anything in this while loop will be displayed to the player
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(recyclingbin_surface, (0, 230))
        screen.blit(trashcan_surface, (700, 230))

        scoreboard = over_font.render(("Score:" + str(score)), True, (255, 255, 255))
        screen.blit(scoreboard, (300, 345))

        mojo_rect.x -= speed * 2
        if mojo_rect.right <= 0: mojo_rect.left = 800
        screen.blit(mojo_jojo_surface, mojo_rect)

        # crushed can
        crushed_can_rect.y += 2
        if crushed_can_rect.y > 300:
            crushed_can_rect = crushed_can_surface.get_rect(midbottom=(random.randrange(50, 750), 0))
        screen.blit(crushed_can_surface, crushed_can_rect)

        # cherry
        cherry_rect.y += speed
        if cherry_rect.y > 300:
            cherry_rect = cherry_surface.get_rect(midbottom=(random.randrange(50, 750), random.randrange(-75, -50)))
        screen.blit(cherry_surface, cherry_rect)

        # bananapeel
        bananapeel_rect.y += 2
        if bananapeel_rect.y > 300:
            bananapeel_rect = bananapeel_surface.get_rect(
                midbottom=(random.randrange(50, 750), random.randrange(-75, -50)))
        screen.blit(bananapeel_surface, bananapeel_rect)

        # paper
        paper_rect.y += speed
        if paper_rect.y > 300:
            paper_rect = paper_surface.get_rect(midbottom=(random.randrange(50, 750), random.randrange(-75, -50)))
        screen.blit(paper_surface, paper_rect)

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

        if bubbles_rect.colliderect(crushed_can_rect):
            crushed_can_rect.y = 300
            needRecycle = True
            recycleAmount += 1

        if bubbles_rect.colliderect(cherry_rect):
            cherry_rect.y = 300
            needCompost = True
            compostAmount += 1

        if bubbles_rect.colliderect(bananapeel_rect):
            bananapeel_rect.y = 300
            needCompost = True
            compostAmount += 1

        if bubbles_rect.colliderect(paper_rect):
            paper_rect.y = 300
            needCompost = True
            compostAmount += 1

        if needRecycle:
            recycle_surface = test_font.render('RECYCLE', False, 'Green')
            screen.blit(recycle_surface, (50, 50))
        if needCompost:
            compost_surface = test_font.render('COMPOST', False, 'Brown')
            screen.blit(compost_surface, (600, 50))

        if needRecycle == True:
            if bubbles_rect.colliderect(recyclingbin_rect):
                score += recycleAmount
                recycleAmount = 0
                needRecycle = False

        if needCompost == True:
            if bubbles_rect.colliderect(trashcan_rect):
                score += compostAmount
                compostAmount = 0
                needCompost = False

        if score > 30:
            speed = 2
        elif score > 40:
            speed = 3
        elif score > 50:
            speed = 4
        elif score > 70:
            speed = 5
        elif score > 80:
            speed = 6
        elif score > 100:
            speed = 7
        elif score > 120:
            speed = 8
        elif score > 130:
            speed = 9
        elif score > 150:
            speed = 10

        if (isCollision(bubbles_rect.x, bubbles_rect.y, mojo_rect.x, mojo_rect.y)):
            clock.tick(0)
            break

        pygame.display.update()
        clock.tick(60)  # tells the while loop to not run faster than 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playAgain()
            if event.type == pygame.QUIT:
                pygame.quit()  # opposite of init(); closes pygame
                exit()
        gui.play_sound('game-over-sound')
        text = test_font.render('(PRESS SPACE TO PLAY AGAIN)', True, 'White')
        screen.blit(text, (200, 260))
        pygame.display.update()
        over_text = test_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200, 200))
        pygame.display.update()
        clock.tick(60)

while True:
    background_screen_surf = pygame.image.load('./images/puffbackground.png')
    screen.blit(background_screen_surf, (0, 0))

    title_font = pygame.font.Font('Pixeltype.ttf', 75)
    intro_font = pygame.font.Font('Pixeltype.ttf', 35)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # opposite of init(); closes pygame
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playAgain()
        title = title_font.render('EcoPuffs', True, 'Black')
        screen.blit(title, (295, 20))
        spaces ="                           "
        spaces2 ="                                         "
        spaces3 ="                                                          "
        spaces4 ="                                                      "
        spaces5 ="   "
        spaces6 ="                                                                       "
        intro1 = intro_font.render(spaces+'Blossom, Bubbles, and Buttercup are The Powerpuff Girls!', True, 'Black')
        intro2 = intro_font.render(spaces2+'These little girls are motivated with one mission,', True, 'Black')
        intro2_5 = intro_font.render(spaces3+'SAVING THE WORLD BEFORE BEDTIME! ', True, 'Black')
        intro3 = intro_font.render(spaces5+'And this time, they look outside their window to see trash polluting the town of ', True, 'Black')
        intro4 = intro_font.render(spaces3+'Townsville...it’s time for saving.', True, 'Black')
        intro5 = intro_font.render(spaces6+'Press SPACE to Continue', True, 'Black')
        screen.blit(intro1, (0, 80))
        screen.blit(intro2, (0, 110))
        screen.blit(intro2_5,(0, 160))
        screen.blit(intro3, (0, 210))
        screen.blit(intro4, (0, 240))
        screen.blit(intro5, (0, 290))
        pygame.display.update()




