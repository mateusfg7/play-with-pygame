# import the main modules
import pygame
import pygame.mixer
import pygame.display
import pygame.event
import pygame.draw
import pygame.mouse
import pygame.image

import random

import os

# config relative paths


def getPath(path: str) -> str:
    dir = os.path.dirname(__file__)
    return os.path.join(dir, path)


# paths
LOGO_PATH = getPath('assets/brain.png')
BACKGROUND_PATH = getPath('assets/background.jpeg')
OLE_SOUND_PATH = getPath('assets/ole.ogg')

# constants
SCREEN_SIZE = WIDTH, HEIGHT = (900, 600)
CENTER_POSITION = (WIDTH/2, HEIGHT/2)

# colors

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)
dark_gray = (50, 50, 50)

# create the main function that will start the program


def main():

    # initialize pygame
    pygame.init()

    # load assets
    logo = pygame.image.load(LOGO_PATH)
    oleSound = pygame.mixer.Sound(OLE_SOUND_PATH)
    background = pygame.image.load(BACKGROUND_PATH)

    # set display config
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240x180
    screen = pygame.display.set_mode(SCREEN_SIZE)

    random_pos = (random.randrange(50, WIDTH-50),
                  random.randrange(50, HEIGHT-50))

    # define the variable to controll tha main loop
    running = True

    # THE LOOP
    while running:
        screen.blit(background, (0, 0))

        circle = pygame.draw.circle(
            surface=screen,
            color=dark_gray,
            center=random_pos,
            width=10,
            radius=10
        )
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the valo of running to False, and exit the main
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()

                if circle.collidepoint(mouse_position):
                    random_pos = (random.randrange(50, WIDTH-50),
                                  random.randrange(50, HEIGHT-50))
                    oleSound.play()

        pygame.display.flip()


# run the main function only if the module is executed as the main script
# (if you import this as a module nothing is executed)
if __name__ == "__main__":
    main()
