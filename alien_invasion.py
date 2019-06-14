import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship.
    ship = Ship(screen)

    # start the main loop for the game
    while True:

        # watch for keyboard and mouse events
        gf.check_events()

        # redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the most recently drawn screen visible.
        pygame.display.flip()

run_game()