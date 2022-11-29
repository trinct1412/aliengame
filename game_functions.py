import sys
import pygame

def get_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_turn_right = False
    if event.key == pygame.K_LEFT:
        ship.is_turn_left = False

def get_keydown_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_turn_right = True
    if event.key == pygame.K_LEFT:
        ship.is_turn_left = True



def check_event(ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            get_keydown_event(event, ship)            

        elif event.type == pygame.KEYUP:
            get_keyup_event(event, ship)            
             
                
def update_screen(background_color, screen, ship, bullets):
    screen.fill(background_color)
    ship.blitme()
        
    pygame.display.flip()
        