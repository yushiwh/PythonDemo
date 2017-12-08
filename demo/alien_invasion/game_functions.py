import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    """按下按键方法"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    """松开按键方法"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    """响应鼠标的事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 按键按下来
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # 按键松开
            check_keyup_events(event, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen, and flip to the new screen."""
    """更新屏幕上面的图像，并且切换到新的屏幕"""
    # Redraw the screen, each pass through the loop.
    # 每次循环都会重新绘制屏幕
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Make the most recently drawn screen visible.
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """Update position of bullets, and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
