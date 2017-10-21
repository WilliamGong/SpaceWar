import pygame



class Ship():
    def __init__(self, screen, ai_settings):
        """初始化飞船，设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        #加载图像并获取外接矩形
        self.image = pygame.image.load('images\ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #将新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的center存储小数
        self.center = float(self.rect.centerx)
        #移动标志
        self.moving_right = False
        self.moving_left = False



    def blitme(self):
            """在指定位置绘制飞船"""
            self.screen.blit(self.image, self.rect)

    def update(self):
        """
        更新飞船位置
        根据移动标志
        """
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx = self.center