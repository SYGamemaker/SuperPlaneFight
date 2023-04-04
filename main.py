# -- coding: utf-8 --
# @Time : 2023/4/3 5:06 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : main.py
# @Software: PyCharm
import sys
from constans import *
from utils import *

draw_start_menu(screen_width, screen_height, img_path)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
