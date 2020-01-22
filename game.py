import pygame
import time

pygame.init()

# Size of the Window
display_width = 1080
display_height = 800

# Colors definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Display the Window
gameDisplay = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('Race Game')
clock = pygame.time.Clock()

# Load media
carIMG = pygame.image.load('media/car.png')  # Load Car.
carIMG = pygame.transform.scale(carIMG, (120, 320))  # Resize Car.

car_width = 400


def car(x, y):
    # Car function that determinate where the car is.
    gameDisplay.blit(carIMG, (x, y))


def text_objects(text, font):
    # Function to render the text
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    # Function to display big Messages on the screen
    largeText = pygame.font.Font('freesansbold.ttf',115)        # Sets up the font and size of the text
    TextSurf, TextRect = text_objects(text, largeText)          # The surface and rectangle of text = parameters
    TextRect.center = ((display_width/2.7),(display_width/2))   # Position of the message
    gameDisplay.blit(TextSurf, TextRect)                        # Creates the message in the background

    pygame.display.update()                                     # Update the display

    pygame.event.get()                                          # Text to fix bug
    time.sleep(2)                                               # Time that the message is going to be showing

    game_loop()                                                 # Run the game again



def crash():
    # This is what happens when you Crashed
    message_display('You Crashed')






def game_loop():
    # Initial Car position.
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    # Initialization of variable for moving the car.
    x_change = 0

    gameExit = False

    while not gameExit:  # Logic Loop of Events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # If you press the window X.
                pygame.quit()
                quit()                              # Quit the game.

            if event.type == pygame.KEYDOWN:        # If there is a Key being press.
                if event.key == pygame.K_LEFT:      # If the key is Left key.
                    x_change = -10                  # Adds negative value to a variable.
                elif event.key == pygame.K_RIGHT:   # If the key is Right key.
                    x_change = +10                  # Adds positive value to a variable.

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)     # Set background color
        car(x, y)                   # Calls the car function with the new coordinates

        if x > display_width - car_width or x < 0: # If the car goes out of the screen
            crash()                 # Car crashes

        pygame.display.update()     # Updates screen
        clock.tick(120)             # FPS


game_loop()

pygame.quit()
quit()
