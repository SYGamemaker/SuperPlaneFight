# -- coding: utf-8 --
# @Time : 2023/4/3 5:44 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : menu.py.py
# @Software: PyCharm
import os
import sys
from utils import render_text, calculate_button_position
import pygame
from constans import *


class Menu:
    """
    游戏菜单类
    """
    def __init__(self, screen):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        if os.path.exists("resource/photo/menu_bg.jpg"):
            self.menu_bg = pygame.image.load("resource/photo/menu_bg.jpg")
        else:
            self.menu_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.menu_bg.fill((255, 255, 255))  # Fill with white color
            print("Warning: menu_bg.jpg not found. Using default white background.")

        if os.path.exists("resource/photo/start_btn.png"):
            self.start_btn = pygame.image.load("resource/photo/start_btn.png")
        else:
            self.start_btn = render_text("开始游戏", FONT_PATH, 30, (0, 255, 0))
            print("Warning: start_btn.png not found. Using default green text.")

        btn_width, btn_height = self.start_btn.get_size()
        btn_gap = btn_height // 2

        btn_x, btn_y = calculate_button_position(0, btn_width, btn_height, btn_gap, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.start_btn_rect = self.start_btn.get_rect()
        self.start_btn_rect.topleft = (btn_x, btn_y)

        if os.path.exists("resource/photo/score_btn.png"):
            self.score_btn = pygame.image.load("resource/photo/score_btn.png")
        else:
            self.score_btn = render_text("历史分数", FONT_PATH, 30, (0, 0, 255))
            print("Warning: score_btn.png not found. Using default blue text.")

        btn_x, btn_y = calculate_button_position(1, btn_width, btn_height, btn_gap, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.score_btn_rect = self.score_btn.get_rect()
        self.score_btn_rect.topleft = (btn_x, btn_y)

        if os.path.exists("resource/photo/exit_btn.png"):
            self.exit_btn = pygame.image.load("resource/photo/exit_btn.png")
        else:
            self.exit_btn = render_text("退出游戏", FONT_PATH, 30, (255, 0, 0))
            print("Warning: exit_btn.png not found. Using default red text.")

        btn_x, btn_y = calculate_button_position(2, btn_width, btn_height, btn_gap, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.exit_btn_rect = self.exit_btn.get_rect()
        self.exit_btn_rect.topleft = (btn_x, btn_y)

    def draw(self):
        """
        绘制菜单
        """
        self.screen.blit(self.menu_bg, (0, 0))
        self.screen.blit(self.start_btn, self.start_btn_rect.topleft)
        self.screen.blit(self.score_btn, self.score_btn_rect.topleft)
        self.screen.blit(self.exit_btn, self.exit_btn_rect.topleft)
        pygame.display.update()

    def handle_events(self, events):
        """
        处理d点击事件
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if self.start_btn_rect.collidepoint(pos):
                    print("Start game")
                    return GameState.PLAYING
                elif self.exit_btn_rect.collidepoint(pos):
                    print("Exit game")
                    return GameState.QUIT
        return GameState.MENU
