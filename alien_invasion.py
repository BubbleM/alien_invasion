# 玩家退出时，将使用模块sys来退出游戏
import sys

# 模块pygame包含开发游戏所需的功能
import pygame

def run_game():

	# 初始化游戏并创建一个屏幕对象

	# 初始化背景设置
	pygame.init() 
	# 创建一个名为screen的显示窗口，这个游戏的所有图形元素都将在其中绘制
	# 参数(1200,800)是一个元组，指定了游戏窗口的尺寸
	screen = pygame.display.set_mode((1200,800)) 
	pygame.display.set_caption("Alien Invasion")
	# 设置背景色
	bg_color = (230,230,230)

	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		# pygame.event.get() 为访问Pygame检测到的事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# 每次循环时都重绘屏幕
		screen.fill(bg_color)

		# 让最近绘制的屏幕可见
		# 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见
		pygame.display.flip()

run_game()