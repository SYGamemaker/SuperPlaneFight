# -- coding: utf-8 --
# @Time : 2023/4/3 5:21 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : utils.py.py
# @Software: PyCharm
import pygame
from constans import FONT_PATH


def render_text(text, font_name, font_size, color):
    """
    渲染文字方法
    :param text: 文字文本
    :param font_name: 字体
    :param font_size: 字体大小
    :param color: 字体颜色
    :return:
    """
    font = pygame.font.Font(FONT_PATH, font_size)
    return font.render(text, True, color)


def calculate_button_position(index, btn_width, btn_height, btn_gap, screen_width, screen_height):
    """
    计算按键位置
    :param index:
    :param btn_width:
    :param btn_height:
    :param btn_gap:
    :param screen_width:
    :param screen_height:
    :return:
    """
    btn_x = (screen_width - btn_width) // 2
    total_height = btn_height * 3 + btn_gap * 2
    btn_y_start = (screen_height - total_height) // 2
    btn_y = btn_y_start + (btn_height + btn_gap) * index
    return btn_x, btn_y
