import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """response for key down""" 
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

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

                
        
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update screen, switch to new screen"""
    # Each time cycle re-draw screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    # Re-draw all bullets after ship and Alien.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Let recent drawing can be seen on screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """update bullets position, and delete missed bullets"""
    #update bullets position
    bullets.update()

    #delete missed bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """response bullet and alien collision"""
    # Delete collision B and A
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        #delete current bullets and create new group of aliens
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
    

    
def get_number_aliens_x(ai_settings, alien_width):
    """calc how many aliens can be in one line"""
    available_space_x = ai_settings.screen_width - 2* alien_width
    number_aliens_x = int(available_space_x / (2* alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """calc rows for alien"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create a alien and insert to current line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2* alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    

def create_fleet(ai_settings, screen, ship, aliens):
    """create aliens group"""
    #alien distance equals width of alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    #create aliens group
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)

def check_fleet_edge(ai_settings, aliens):
    """alien reach edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """move aliens down, and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """response the collision ship"""
    if stats.ships_left > 0:
        # ships_left -1
        stats.ships_left -=1

        #clear aliens list and bullets list
        aliens.empty()
        bullets.empty()

        #create a group aliens, and put new ship on the center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #stop
        sleep(0.5)

    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check if alien reach to bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #handle it like ship crash
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
        
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """check if aliens at edge, update all aliens position"""
    check_fleet_edge(ai_settings, aliens)
    aliens.update()

    #check A and S collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # check if alien reach the bottom
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


        

        
    

    
