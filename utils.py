# -- coding: utf-8 --
# @Time : 2023/4/3 5:21 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : utils.py
# @Software: PyCharm
import os
from menu import *
from constans import *
import pygame


def draw_start_menu(width, height, img):
    """
    绘制开始菜单
    """
    screen = create_menu()
    if os.path.isfile(img):
        background = pygame.image.load(img).convert()
        screen.blit(background, (0, 0))
    else:
        screen.fill(black)
    btn = create_menu_text_btn()
    screen.blit(btn[0], (width // 2 - btn[0].get_width() // 2, height // 4))
    screen.blit(btn[1], (width // 2 - btn[1].get_width() // 2, height // 2))
    screen.blit(btn[2], (width // 2 - btn[2].get_width() // 2, height * 3 // 4))
    pygame.display.flip()
    return screen, btn
