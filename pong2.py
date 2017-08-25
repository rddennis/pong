import pygame

# Initialize the game engine
pygame.init()
pygame.font.init()

# Set game screen size
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
speed = [8, 6]

# Off switch for the game
GAME_ON = False
done = False

# Starting location of the square
x = 740
y = 0
z = 0

paddleWidth = 20        
paddleHeight = 80
player_1_score = 0
player_2_score = 0
level = 1
currentTotalScore = 0

paddle1 = pygame.Rect(40, y, paddleWidth, paddleHeight)
paddle2 = pygame.Rect(x, z, paddleWidth, paddleHeight)
ballrect = pygame.draw.circle(screen, (230, 32, 118), (360, 360), 3, 1)

# background_image = pygame.image.load("media/beach.jpg")
bgc_image = pygame.image.load("media/bgclogo.png")

# A throttling tool to control fps
clock = pygame.time.Clock()

def drawObjectRects(p):
    return pygame.draw.rect(screen, (230, 32, 118), p)

print "Game starting...."

# Main game loop
while not done:

    pygame.display.set_mode((800,600),0,0)
    pygame.display.set_caption("Black Girls Code: Pong")
    header_font = pygame.font.Font("media/Reprineato.ttf", 50)
    header_text = header_font.render("PONG",True,(0,0,0))
    start_font=pygame.font.Font("media/Reprineato.ttf",30)
    start_text=start_font.render("Press S to Start",True,(0,0,0))
    quit_font = pygame.font.Font("media/Reprineato.ttf",30)
    quit_text = quit_font.render("Press Q to Quit",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(bgc_image, (174, 40))
    screen.blit(header_text,(350,220))
    screen.blit(start_text,(320,300))
    screen.blit(quit_text,(325,350))
    pygame.display.flip()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]: GAME_ON = True
    if pressed[pygame.K_q]: done = True


    while GAME_ON:

        # Loop through all game events
        for event in pygame.event.get():
            # If the player quits ...
            if event.type == pygame.QUIT:
                done = True
                GAME_ON = False

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        if ballrect.collidelist([paddle1, paddle2]) > -1:
            speed[0] = -speed[0]

        if ballrect.collidelist([paddle1, paddle2]) > -1:
            speed[1] = -speed[1]

        if ballrect.collidelist([paddle2]) > -1:
            if ballrect.right < (x+(paddleWidth/2)):
                player_2_score += 1

        if ballrect.collidelist([paddle1]) > -1:
            if ballrect.left > 40:
                player_1_score += 1

        totalScore = player_1_score + player_2_score

        if totalScore > (currentTotalScore + 20):
            level += 1
            currentTotalScore = totalScore
            speed[0] += 1
            speed[1] += 1
            print level


        # Validator for key presses
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: z -= 20
        if pressed[pygame.K_DOWN]: z += 20
        if pressed[pygame.K_q]: y -= 20
        if pressed[pygame.K_a]: y += 20


        # Set the background color of screen
        
        screen.fill((0,0,0))
        score_font = pygame.font.Font("media/Reprineato.ttf", 40)
        player_1_header = score_font.render("Player 1", True, (255,255,255))
        player_2_header = score_font.render("Player 2", True, (255,255,255))
        player_1_text = score_font.render(str(player_1_score),True,(255,255,255))
        player_2_text = score_font.render(str(player_2_score), True, (255,255,255))
        screen.blit(player_1_header, (40, 30))
        screen.blit(player_2_header, (680, 30))
        screen.blit(player_1_text, (40, 65))
        screen.blit(player_2_text, (700, 65))

        # create deadzones
        drawObjectRects(pygame.Rect(0, 0, 5, 800))
        drawObjectRects(pygame.Rect(795, 0, 5, 800))
        drawObjectRects(pygame.Rect(399, 0, 2, 800))

        # Draw the square on the screen
        
        paddle1 = drawObjectRects(pygame.Rect(40, y, paddleWidth, paddleHeight))
        paddle2 = drawObjectRects(pygame.Rect(x, z, paddleWidth, paddleHeight))
        ballrect = pygame.draw.circle(screen, (230, 32, 118), ballrect.center, 14)
       


        pygame.display.flip()
        # Throttle to 60fps to slow down events on the screen
        clock.tick(60)
