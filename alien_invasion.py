# 模块pygame包含开发游戏所需的功能
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init() 
	ai_settings = Settings()
	# 创建一个名为screen的显示窗口，这个游戏的所有图形元素都将在其中绘制
	# 参数(1200,800)是一个元组，指定了游戏窗口的尺寸
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
	pygame.display.set_caption("Alien Invasion")
	# 创建一艘飞船
	ship = Ship(screen)
	# 开始游戏的主循环
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)

run_game()