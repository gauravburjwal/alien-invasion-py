import sys
import pygame

def run_game():
    # initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # set the background color.
    bg_color = (175, 175, 175)

    # start the main loop for the game
    while True:

        # watch for keyboar and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen during each pass through the loop.
        screen.fill(bg_color)

        # make the most recently drawn screen visible.
        pygame.display.flip()

run_game()