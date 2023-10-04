import os

import pygame

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

IMAGE_PIPE = pygame.transform.scale2x(os.path.join("assets", "pipe.png"))
IMAGE_FLOOR = pygame.transform.scale2x(os.path.join("assets", "base.png"))
IMAGE_BACKGROUND = pygame.transform.scale2x(os.path.join("assets", "bg.png"))
IMAGE_BIRD = [
    pygame.transform.scale2x(os.path.join("assets", "bird1.png")),
    pygame.transform.scale2x(os.path.join("assets", "bird2.png")),
    pygame.transform.scale2x(os.path.join("assets", "bird3.png")),
]