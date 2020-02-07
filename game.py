import pygame
import time
import random

pygame.init()

# Load media
# Images:
carIMG = pygame.image.load('media/car.png')  # Load Car.
carIMG = pygame.transform.scale(carIMG, (120, 320))  # Resize Car.

carIMG_2 = pygame.image.load('media/car_2.png')


pygame.display.set_icon(carIMG) # Game Icon

# Sounds:
crash_sound = pygame.mixer.Sound('media/car-crash.ogg')
pygame.mixer.music.load('media/song.ogg')

# Size of the Window

#Solid Screen Size
display_width = 800
display_height = 1000

#Dinamic Screen Size
infoObject = pygame.display.Info()
#display_width = infoObject.current_w
#display_height = infoObject.current_h

# Colors definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 0, 0)
green = (0, 150, 0)
blue = (0, 0, 200)
grey = (192,192,192)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)

dark_green = (0,100,00)

background=white



# Display the Window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Race Game')
clock = pygame.time.Clock()


pause = False

car_width = 120


def score(count,text,x,y):
    # Display text on screen
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render(text+str(count), True, white)
    gameDisplay.blit(text,(x,y))


def cars(thingx, thingy, car_type):
    # Creates cars obstacles.
    #pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(car_type, (thingx, thingy))


def things(thingx, thingy, thingw, thingh, color):
    # Draw objects with the the arguments
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
    TextSurf, TextRect = text_objects(text, largeText, red)     # The surface and rectangle of text = parameters
    TextRect.center = ((display_width/2),(display_width/2))     # Position of the message
    gameDisplay.blit(TextSurf, TextRect)                        # Creates the message in the background

    pygame.display.update()                                     # Update the display

    pygame.event.get()                                          # Text to fix bug
    time.sleep(2)                                               # Time that the message is going to be showing

    game_loop()                                                 # Run the game again



def crash():
    # Stops the music, plays crash sound, display message and buttons to retry or exit

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

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
    # Reads mouse position/click, draw rectangle w/ arg and execute actions if mouse is over or click the rectangle
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

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
    pygame.mixer.music.unpause()
    pause = False


def paused():
    # Pause music, generate pause screen with text and buttons to return or quit.
    pygame.mixer.music.pause()

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
    # Generates Intro screen with GO! and QUIT buttons.

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

        button("GO!", 250, display_height/1.66, 100, 50, green, bright_green,game_loop)
        button("QUIT", 450, display_height/1.66, 100, 50, red, bright_red,quitgame)


        pygame.display.update()
        clock.tick(15)

def game_loop():

    global pause

    dodged = 0
    scores = 0

    # Start the music
    pygame.mixer.music.play(-1) # Attribute indicates the amount of time the song is going to play
    music = True

    # Initial Car position.
    x = (display_width * 0.45)
    y = (display_height * 0.7)

    # Inside the road
    inside_l = round(display_width / 6)
    inside_r = round(display_width/1.5)


    # Initialization of variable for moving the car.
    x_change = 0

    # Parameters for the street lines
    lines_startx = display_width / 2
    lines_starty = -1
    lines_width = 15
    lines_height = 80

    # Exact position for the 3 lanes
    lanes = [display_width / 4.7, display_width / 2.2, display_width / 1.47]


    # Parameters for Road cars
    thing_startx = random.choice(lanes)
    thing_starty = -700
    thing_speed = 7
    thing_width = 96
    thing_height = 192

    thing2_startx = random.choice(lanes)
    thing2_starty = random.randrange(-700,0)


    level1 = True

    #gameExit

    while level1:  # Logic Loop of Events.

        for event in pygame.event.get():
            # If you press the window X.
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # If there is a Key being press.
                if event.key == pygame.K_LEFT:
                    # Side Movement
                    x_change = -12
                if event.key == pygame.K_RIGHT:
                    x_change = +12

                if event.key == pygame.K_UP:
                    # Acceleration
                    thing_speed = +30
                    scores += 2

                if event.key == pygame.K_DOWN:
                    # Brake
                    thing_speed = 5

                if event.key == pygame.K_p:
                    # Pause
                    paused()

                if event.key == pygame.K_m:
                    # Music on/off
                    if music == True:
                        pygame.mixer.music.pause()
                        music = False
                    else:
                        pygame.mixer.music.unpause()
                        music = True


            if event.type == pygame.KEYUP:
                # If key is release.
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    thing_speed = 10

        x += x_change

        gameDisplay.fill(dark_green)
        # Set background color

        # Road, Left and Right guardrail.
        pygame.draw.rect(gameDisplay, grey, (inside_l, 0, inside_r, display_height))
        pygame.draw.rect(gameDisplay, black, (inside_l-30, 0, 20, display_height))
        pygame.draw.rect(gameDisplay, black, ((inside_l+inside_r) + 10, 0, 20, display_height))


        #Street Lines
        for i in range(1,2000,150):
            things(lines_startx-100,(lines_starty-display_height)+i,lines_width,lines_height,white)

        for i in range(1,2000,150):
            things(lines_startx+100,(lines_starty-display_height)+i,lines_width,lines_height,white)
        lines_starty += thing_speed+10

        # Respawn the lines
        if lines_starty > display_height:
            lines_starty = 0 - lines_height/2


        # Road Cars
        cars(thing2_startx, thing2_starty, carIMG_2)
        thing2_starty += thing_speed

        # More Cars
        #if dodged > 5:
        #    things(thing2_startx, thing2_starty,carIMG_2)
        #    thing2_starty += thing_speed

        # Car Initialization
        car(x, y)

        # Scores
        scores += 1
        if thing_speed == 37:
            scores += 5
        elif thing_speed == 5:
            scores -= 5
        else:
            scores += 1

        # Score Visualization
        score(dodged,"Dodged: ",0,0)
        score(scores, "Score: ",0,50)



        if x > display_width - car_width or x < 0:
            # If the car goes out of the screen
            crash()

        if thing2_starty > display_height:
            # If the object is out of screen aka there is no object
            thing2_starty = random.randrange(-700,0) - thing_height
            thing2_startx = random.choice(lanes)
            dodged += 1

        if thing_starty > display_height:
            # If the object is out of screen aka there is no object
            thing_starty = 0 - thing_height
            thing_startx = random.choice(lanes)
            # random.randrange(inside_l, inside_r)   # Area where the objects are going to appear
            dodged += 1
            #thing_speed += 1 # Things moves quicker each time you dodge
            #thing_width += (dodged * 1.2) # Make things bigger each time you dodge

        if y < thing_starty+thing_height:
            #print('Y Crossover')

            if (x > thing_startx) and (x < (thing_startx + thing_width)) or ((x + car_width) > thing_startx) and \
                    ((x + car_width) < (thing_startx + thing_width)):
                #print('X Crossover')
                crash()

        if y < thing2_starty + thing_height:

            if (x > thing2_startx) and (x < (thing2_startx + thing_width)) or ((x + car_width) > thing2_startx) \
                    and ((x + car_width) < (thing2_startx + thing_width)):
                crash()

        # Update Screen and FPS
        pygame.display.update()
        clock.tick(120)

        #print(f"Car start at position is {x} and car finish at position {x+car_width}")
        #print(f"object start at position is {thing_startx} and car finish at position {thing_startx+thing_width}")


game_intro()
game_loop()

pygame.quit()
quit()
