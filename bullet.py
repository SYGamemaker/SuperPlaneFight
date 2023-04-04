import pygame
from constants import *


class PlayerBullet(pygame.sprite.Sprite):
    """
    玩家子弹类
    """
    def __init__(self, x, y):
        super().__init__()

        if os.path.exists("resource/photo/bullet.png"):
            self.image = pygame.image.load("resource/photo/bullet.png")
        else:
            self.image = pygame.Surface((5, 10))
            self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        self.rect.y -= 10
        if self.rect.y < -10:
            self.kill()
