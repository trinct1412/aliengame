import pygame
from settings import Settings
from pygame.sprite import  Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, Settings.BULLET_WIDTH, Settings.BULLET_HEIGHT)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        
        self.color = Settings.BULLET_COLOR
        self.speed_factor = Settings.BULLET_SPEED_FACTOR
        
    
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    