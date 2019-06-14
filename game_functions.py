# all the functions used to make ALien Invasion work
import sys
import pygame

def check_events():
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make the most recently drawn screen visible.
    pygame.display.flip()