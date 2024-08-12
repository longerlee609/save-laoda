import pygame 

class Ship:

    def __init__(self,ai_game):
        #初始飞船位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #加载飞船图像，获取rect

        self.image = pygame.image.load("images/laoda.jpg")
        self.rect = self.image.get_rect()

        #设置飞船位置
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        #self.y = float(self.rect.y)

        #移动标志位置
        self.moving_right = False
        self.moving_left = False
        #self.moving_up = False
        #self.moving_down = False
        #设置飞船速度
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        #if self.moving_up and self.rect.up < self.screen_rect.up:
            #self.y -= self.settings.ship_speed
        #if self.moving_down and self.rect.down > self.screen_rect.down:
            #self.y += self.settings.ship_speed

        self.rect.x = self.x
        #self.rect.y = self.y

    def blitme(self):
        #绘制飞船
        self.screen.blit(self.image,self.rect)