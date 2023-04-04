# -- coding: utf-8 --
# @Time : 2023/4/3 5:11 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : plane.py.py
# @Software: PyCharm
import os
import pygame
from bullet import PlayerBullet
from constans import SCREEN_WIDTH, SCREEN_HEIGHT


class Player:
    """
    玩家的飞机类
    """

    def __init__(self):
        if os.path.exists("resource/photo/player_plane.png"):
            self.image = pygame.image.load("resource/photo/player_plane.png")
        else:
            self.image = pygame.Surface((20, 20))
            self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)
        self.bullets = pygame.sprite.Group()
        self.shoot_delay = 200  # 控制子弹发射速度的延迟（毫秒）
        self.shoot_timer = 0  # 记录上次发射子弹的时间

    def update(self, dt):
        """
        玩家的操作类
        w、s、a、d：上下左右移动
        j发射子弹
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5

        if keys[pygame.K_j]:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_timer > self.shoot_delay:
                self.shoot()
                self.shoot_timer = current_time

        self.bullets.update()

        new_x = self.rect.x
        new_y = self.rect.y
        screen_height = pygame.display.get_surface().get_height()
        screen_width = pygame.display.get_surface().get_width()
        if (new_y >= screen_height * 2 / 3) and (new_y + self.rect.height <= screen_height) and (new_x >= 0) and (
                new_x + self.rect.width <= screen_width):
            self.rect.x = new_x
            self.rect.y = new_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)

    def shoot(self):
        bullet = PlayerBullet(self.rect.x, self.rect.y)
        self.bullets.add(bullet)
