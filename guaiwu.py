import pygame

from pygame.sprite import Sprite

class Kunkun(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #加载外星人图像,设置rect属性

        self.image = pygame.image.load("images/kunkun.png")
        self.rect = self.image.get_rect()

        
        #设置外星人初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.settings = ai_game.settings

    def check_edges(self):
        screen_rect = self.screen.get_rect()

        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        #向右移动坤坤
        self.x += self.settings.kunkun_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def draw_kunkun(self):
        self.screen.blit(self.image,self.rect)

        