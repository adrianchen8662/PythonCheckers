# Import Statments
import pygame

# Classes defines position and sprite appearance for black, white, king black and king white checkerpieces
# Includes mouse capture and movement
class blackcp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((100,100))
        self.image = pygame.image.load('blackcp.jpg').convert_alpha()
        self.rect = self.surf.get_rect()
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.rect.collidepoint(event.pos):
                        return
                        '''
                        
class whitecp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((100,100))
        self.image = pygame.image.load('whitecp.jpg').convert_alpha()
        self.rect = self.surf.get_rect()
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.rect.collidepoint(event.pos):
                        return
                        '''

class kingblackcp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((100,100))
        self.image = pygame.image.load('kingblackcp.jpg').convert_alpha()
        self.rect = self.surf.get_rect()
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.rect.collidepoint(event.pos):
                        return
                        '''

class kingwhitecp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((100,100))
        self.image = pygame.image.load('kingwhitecp.jpg').convert_alpha()
        self.rect = self.surf.get_rect()
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.rect.collidepoint(event.pos):
                        return
                        '''