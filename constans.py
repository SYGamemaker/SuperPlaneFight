# -- coding: utf-8 --
# @Time : 2023/4/3 5:21 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : constans.py.py
# @Software: PyCharm
import os
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_PATH = os.path.join("resources", "font", "NotoSansSC-Light.otf")


class GameState(Enum):
    """
    游戏状态码
    """
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2
    QUIT = 3
