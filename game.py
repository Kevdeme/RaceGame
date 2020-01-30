import pygame
import time
import random


pygame.init()

# Size of the Window
display_width = 800
display_height = 1000

# Colors definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 200)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)



# Display the Window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Race Game')
clock = pygame.time.Clock()

# Load media
carIMG = pygame.image.load('media/car.png')  # Load Car.
carIMG = pygame.transform.scale(carIMG, (120, 320))  # Resize Car.

pygame.display.set_icon(carIMG)


pause = False

car_width = 120


def things_dodged(count):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Dodge: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))



def things(thingx, thingy, thingw, thingh, color):
    # Creates things with the the arguments
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    # Car function that determinate where the car is.
    #pygame.draw.rect(gameDisplay, green, [x, y, car_width, 100])
    gameDisplay.blit(carIMG, (x, y))


def text_objects(text, font, color):
    # Function to render the text
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):
    # Function to display big Messages on the screen
    largeText = pygame.font.Font('freesansbold.ttf',115)        # Sets up the font and size of the text
    TextSurf, TextRect = text_objects(text, largeText, red)          # The surface and rectangle of text = parameters
    TextRect.center = ((display_width/2),(display_width/2))     # Position of the message
    gameDisplay.blit(TextSurf, TextRect)                        # Creates the message in the background

    pygame.display.update()                                     # Update the display

    pygame.event.get()                                          # Text to fix bug
    time.sleep(2)                                               # Time that the message is going to be showing

    game_loop()                                                 # Run the game again



def crash():
    # This is what happens when you Crashed

    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects('You Crashed', largeText, red)
    TextRect.center = ((display_width / 2), (display_width / 3))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)

        button("Play Again", 250, 600, 130, 50, green, bright_green, game_loop)
        button("QUIT", 450, 600, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,color1,color2,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, color2, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, color1, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False


def paused():
    global pause
    pause = True

    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects('Pause', largeText, red)
    TextRect.center = ((display_width / 2), (display_width / 3))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)

        button("Continue", 250, 600, 100, 50, green, bright_green,unpause)
        button("QUIT", 450, 600, 100, 50, red, bright_red,quitgame)


        pygame.display.update()
        clock.tick(15)

def game_intro():
    # Intro Screen
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Race Game', largeText, red)
        TextRect.center = ((display_width/2),(display_width/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 250, 600, 100, 50, green, bright_green,game_loop)
        button("QUIT", 450, 600, 100, 50, red, bright_red,quitgame)


        pygame.display.update()
        clock.tick(15)

def game_loop():
    # Initial Car position.
    x = (display_width * 0.45)
    y = (display_height * 0.7)

    # Initialization of variable for moving the car.
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -700
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:  # Logic Loop of Events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # If you press the window X.
                pygame.quit()
                quit()                              # Quit the game.

            if event.type == pygame.KEYDOWN:        # If there is a Key being press.
                if event.key == pygame.K_LEFT:      # If the key is Left key.
                    x_change = -20                  # Adds negative value to a variable.
                elif event.key == pygame.K_RIGHT:   # If the key is Right key.
                    x_change = +20                  # Adds positive value to a variable.
                if event.key == pygame.K_p:
                    pause = True
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)     # Set background color

        # def things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed





        car(x, y)                   # Calls the car function with the new coordinates
        things_dodged(dodged)


        if x > display_width - car_width or x < 0: # If the car goes out of the screen
            crash()                 # Car crashes

        if thing_starty > display_height:           # If the object is out of screen aka there is no object
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)   # Area where the objects are going to appear
            dodged += 1
            thing_speed += 1                                    # Things moves quicker each time you dodge
            thing_width += (dodged * 1.2)                        # Make things bigger each time you dodge

        if y < thing_starty+thing_height:
            print('Y Crossover')

            if (x > thing_startx) and (x < (thing_startx + thing_width)) or ((x + car_width) > thing_startx) and ((x + car_width) < (thing_startx + thing_width)):
                print('X Crossover')
                crash()

        pygame.display.update()     # Updates screen
        clock.tick(120)             # FPS
        #print(f"Car start at position is {x} and car finish at position {x+car_width}")
        #print(f"object start at position is {thing_startx} and car finish at position {thing_startx+thing_width}")

game_intro()
game_loop()

pygame.quit()
quit()
