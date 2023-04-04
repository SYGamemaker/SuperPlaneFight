# -- coding: utf-8 --
# @Time : 2023/4/3 5:21 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : listener.py
# @Software: PyCharm
import sys

import pygame

from constans import *


def handle_event(screen, btn):
    """
    处理事件
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            start_game_rect = btn[0].get_rect(topleft=(screen_width // 2 - btn[0].get_width() // 2, screen_height // 4))
            history_score_rect = btn[1].get_rect(topleft=(screen_width // 2 - btn[1].get_width() // 2, screen_height // 2))
            exit_game_rect = btn[2].get_rect(topleft=(screen_width // 2 - btn[2].get_width() // 2, screen_height * 3 // 4))

            if start_game_rect.collidepoint(x, y):
                # 开始游戏按钮点击事件
                screen.fill(black)
                pygame.display.flip()

            elif history_score_rect.collidepoint(x, y):
                # 历史分数按钮点击事件
                screen.fill(black)
                pygame.display.flip()

            elif exit_game_rect.collidepoint(x, y):
                # 退出游戏按钮点击事件
                pygame.quit()
                sys.exit()
