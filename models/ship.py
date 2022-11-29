import pygame
from settings import Settings

class Ship:
    def __init__(self, screen) -> None:
        self.screen = screen
        
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.is_turn_right = False
        self.is_turn_left = False
        
    def update(self):
        if self.is_turn_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += Settings.SHIP_SPEED_FACTOR
        if self.is_turn_left and self.rect.left > 0:
            self.rect.centerx -= Settings.SHIP_SPEED_FACTOR
        
    def blitme(self):
        self.screen.blit(self.image , self.rect)