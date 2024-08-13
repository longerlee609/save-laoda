import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        #创建子弹，再设置子弹位置
        self.imagee = pygame.image.load("images/bullets.png")
        self.rect = self.imagee.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        #储存子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        #向上移动子弹
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    

    def draw_bullet(self):
        self.screen.blit(self.imagee,self.rect)