# -- coding: utf-8 --
# @Time : 2023/4/3 5:06 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : main.py
# @Software: PyCharm
import sys
from constans import *
from utils import *
from listener import *

screen = draw_start_menu(screen_width, screen_height, img_path)

while True:
    handle_event(screen[0], screen[1])
