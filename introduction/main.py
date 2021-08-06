# import the main modules
import pygame
import os

# config relative paths


def getPath(path: str) -> str:
    dir = os.path.dirname(__file__)
    return os.path.join(dir, path)


# create the main function that will start the program


def main():

    # initialize pygame
    pygame.init()

    # load a set logo
    logo = pygame.image.load(getPath('assets/brain.png'))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240x180
    screen = pygame.display.set_mode((240, 180))

    # define the variable to controll tha main loop
    running = True

    # THE LOOP
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the valo of running to False, and exit the main
                running = False

# run the main function only if the module is executed as the main script
# (if you import this as a module nothing is executed)


if __name__ == "__main__":
    main()
