import sys
import pygame
from models import Ship
from settings import Settings
from game_functions import check_event, update_screen
from pygame.sprite import Group

def main():
    pygame.init()
    screen = pygame.display.set_mode((Settings.SCREEN_WIDTH,Settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Alien")
    
    ship = Ship(screen)
    
    bullets = Group()
    
    while True:
        check_event(ship, bullets)  
        ship.update()   
        bullets.update()
        update_screen(Settings.BG_COLOR, screen, ship, bullets)        
        
main()
