import pygame

# Initialize the game engine
pygame.init()

# Set game screen size
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
speed = [10, 8]

# Off switch for the game
done = False

# Starting location of the square
x = 740
y = 0
z = 0

ball = pygame.image.load('media/pink-ball.png')
ballrect = ball.get_rect()

# A throttling tool to control fps
clock = pygame.time.Clock()


print("Game starting ...")

# Main game loop
while not done:
    #####################################################
    # STEP 1: EVENTS
    # Check for new events such as movement and closing
    ######################################################

    # Loop through all game events
    for event in pygame.event.get():
        # If the player quits ...
        if event.type == pygame.QUIT:
            done = True

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    ################################################
    # STEP 2: GAME LOOP
    # Code below will repeat until the game ends!
    ################################################

    # Validator for key presses
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_q]: z -=3
    if pressed[pygame.K_a]: z+= 3

 
    color = (255, 255, 255)

    ##########################################################
    # STEP 3: RENDER
    # Finish up by drawing all the objects to the game world
    ##########################################################

    # Set the background color of screen
    screen.fill((0, 0, 0))
    screen.blit(ball, ballrect)

    # Draw the square on the screen
    paddle1 = pygame.draw.rect(screen, color, pygame.Rect(x, y, 20, 80))
    paddle2 = pygame.draw.rect(screen, color, pygame.Rect(40, z, 20, 80))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 5, 800))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(795, 0, 5, 800))

    pygame.display.flip()
    # Throttle to 60fps to slow down events on the screen
    clock.tick(60)
