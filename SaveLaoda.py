import sys

from ship import Ship

import pygame

from settings import Settings

from bullets import Bullet

from guaiwu import Kunkun

class SaveLaoda:

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            self.fire_music()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False  

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Save Laoda")


    #创建ship实例
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.kunkuns = pygame.sprite.Group()

        self._create_fleet()
    
    def _create_kunkun(self,x_position,y_position):
        new_kunkun = Kunkun(self)
        new_kunkun.x = x_position
        new_kunkun.y = y_position
        new_kunkun.rect.x = new_kunkun.x
        new_kunkun.rect.y = new_kunkun.y
        self.kunkuns.add(new_kunkun)

    def _create_fleet(self):
        #设置间距
        kunkun = Kunkun(self)
        kunkun_width,kunkun_height = kunkun.rect.size


        current_x,current_y = kunkun_width,kunkun_height
        while current_y < (self.settings.screen_height - 3*kunkun_height):
            while current_x < (self.settings.screen_width - 2*kunkun_width):
                self._create_kunkun(current_x,current_y)
                current_x += 2*kunkun_width


            current_x = kunkun_width
            current_y += 2*kunkun_height

        kunkun = Kunkun(self)
        self.kunkuns.add(kunkun)
        

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)                

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for kunkun in self.kunkuns.sprites():
            kunkun.draw_kunkun()

        self.kunkuns.draw(self.screen)
        self.ship.blitme()

    def _check_bullets_kunkun_collision(self):
        #检查是否有子弹击中敌人
        collisions = pygame.sprite.groupcollide(self.bullets,self.kunkuns,True,True)

        if not self.kunkuns:
            self.kunkuns.empty()
            self._create_fleet()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_bullets(self):
        #更新子弹位置
        self.bullets.update()

        
        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullets_kunkun_collision()


    def _change_fleet_direction(self):
        #让坤坤们向下移动，同时修改左右方向
        for kunkun in self.kunkuns.sprites():
            kunkun.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1


    def _check_fleet_edges(self):
        for kunkun in self.kunkuns.sprites():
            if kunkun.check_edges():
                self._change_fleet_direction()
                break


    def _update_kunkun(self):
        #检查是否有坤坤到达屏幕边缘
        self._check_fleet_edges()
        self.kunkuns.update()
        
    def run_game(self):
        while True:
            self._check_events()

            self.ship.update()
                    #刷新屏幕
            self._update_screen()
            self._update_kunkun()
            self._update_bullets()
            pygame.display.flip()
            self.clock.tick(60)
            self.bullets.update()


    #输入背景音乐see you again
    file = r"see_you_again.mp3"
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    def fire_music(self):
        filee = r"man.mp3"
        pygame.mixer.init()
        track = pygame.mixer.music.load(filee)
        pygame.mixer.music.play()
if __name__ == "__main__":
    ai = SaveLaoda()
    ai.run_game()