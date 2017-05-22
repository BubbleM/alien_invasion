# 玩家退出时，将使用模块sys来退出游戏
import sys

import pygame

def check_events(ship):
	# 响应键盘和鼠标事件
	# pygame.event.get() 为访问Pygame检测到的事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False

def update_screen(ai_settings,screen,ship):
	"""更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	# 让最近绘制的屏幕可见
	# 每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见
	pygame.display.flip()