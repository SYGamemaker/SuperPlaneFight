# -- coding: utf-8 --
# @Time : 2023/4/3 5:06 PM
# @Author : 夏宇奇
# @Email : yuqi.xia@shanbay.com
# @File : main.py.py
# @Software: PyCharm
import sys

import pygame

from plane import Player
from constans import *
from menu import Menu


def main():
    """
    主函数
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Super Plane Fight")
    menu = Menu(screen)
    player = Player()
    clock = pygame.time.Clock()
    game_state = GameState.MENU

    last_frame_time = pygame.time.get_ticks()
    current_time = pygame.time.get_ticks()
    delta_time = current_time - last_frame_time

    running = True
    while running:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if game_state == GameState.MENU:
            new_state = menu.handle_events(events)
            if new_state != GameState.MENU:
                game_state = new_state
            menu.draw()
        elif game_state == GameState.PLAYING:
            screen.fill((0, 0, 0))
            player.update(delta_time)
            player.draw(screen)
            pygame.display.update()
        elif game_state == GameState.QUIT:
            running = False
    pygame.quit()


if __name__ == "__main__":
    main()
