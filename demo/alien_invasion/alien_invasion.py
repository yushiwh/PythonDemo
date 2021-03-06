import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    # 进行初始化数据和屏幕的渲染
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    # 设置背景的颜色
    bg_color = (230, 230, 230)

    # Make a ship.
    # 创建一个飞船
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    # 创建子弹
    bullets = Group()

    # Start the main loop for the game.
    # 开始循环执行主游戏
    while True:
        # 响应鼠标的事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 每次执行循环都调用飞船的方法
        ship.update()
        gf.update_bullets(bullets)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
