import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """response for key down""" 
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """if not reach the limitation, shoot one bullet"""
    #create a bullet, add it to B group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """response for key up""" 
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """response KB and Mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

                
        
def update_screen(ai_settings, screen, ship, bullets):
    """update screen, switch to new screen"""
    # Each time cycle re-draw screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Re-draw all bullets after ship and Alien.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Let recent drawing can be seen on screen
    pygame.display.flip()


def update_bullets(bullets):
    """update bullets position, and delete missed bullets"""
    #update bullets position
    bullets.update()

    #delete missed bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    
