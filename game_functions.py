import sys

import pygame

def check_keydown_events(event, ship):
    """response for key down""" 
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """response for key up""" 
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """response KB and Mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

                
        
def update_screen(ai_settings, screen, ship):
    """update screen, switch to new screen"""
    # Each time cycle re-draw screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Let recent drawing can be seen on screen
    pygame.display.flip()
