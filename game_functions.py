# all the functions used to make ALien Invasion work
import sys
import pygame

def check_events():
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()