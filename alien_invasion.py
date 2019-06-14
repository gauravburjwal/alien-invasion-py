import sys
import pygame
from settings import Settings

def run_game():
    # initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # start the main loop for the game
    while True:

        # watch for keyboar and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        # make the most recently drawn screen visible.
        pygame.display.flip()

run_game()