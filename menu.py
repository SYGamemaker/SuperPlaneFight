# -- coding: utf-8 --
# @Time : 2023/4/3 5:44 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : menu.py
# @Software: PyCharm
import pygame

from constans import *
from utils import *


def create_menu():
    """
    创建菜单对象
    """
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen


def create_menu_text_btn():
    """
    创建菜单文字按钮
    """
    is_font_file = os.path.isfile(font_path)
    if is_font_file:
        font = pygame.font.Font(font_path, menu_btn_font_size)
    else:
        font = pygame.font.SysFont(default_font, menu_btn_font_size)
    print(font_path)
    start_game_btn = font.render(start_game_text, True, white)
    history_score_btn = font.render(history_score_text, True, white)
    exit_game_btn = font.render(exit_game_text, True, white)
    return start_game_btn, history_score_btn, exit_game_btn
