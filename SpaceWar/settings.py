class Settings():
    """存储所有设置"""
    def __init__(self):
        """初始化设置"""
        #屏幕设置
        self.screen_width = 840
        self.screen_helight = 640 
        self.bg_color = (230, 230, 230)

        #飞船设置
        self.ship_speed_factor = 1.5