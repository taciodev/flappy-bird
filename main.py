import os

import pygame

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

IMAGE_PIPE = pygame.transform.scale2x(os.path.join("assets", "pipe.png"))
IMAGE_FLOOR = pygame.transform.scale2x(os.path.join("assets", "base.png"))
IMAGE_BACKGROUND = pygame.transform.scale2x(os.path.join("assets", "bg.png"))
IMAGES_BIRDS = [
    pygame.transform.scale2x(os.path.join("assets", "bird1.png")),
    pygame.transform.scale2x(os.path.join("assets", "bird2.png")),
    pygame.transform.scale2x(os.path.join("assets", "bird3.png")),
]

pygame.font.init()
FONT_POINTS = pygame.font.SysFont("arial", 50)

class Bird:
    IMAGES = IMAGES_BIRDS

    # Animação de rotação
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    TIME_ANIMATION = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.velocity = 0
        self.height = self.y
        self.time = 0
        self.image_count = 0
        self.image = self.IMAGES[0]
    
    def jump(self):
        self.velocity = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        # Calcular deslocamento
        self.time += 1
        displacement = 1.5 * (self.time ** 2) + self.velocity * self.time

        # Restringit o deslocamento
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2
        
        self.y += displacement

        # O angulo do pássaro
        if displacement < 0 or self.y < (self.height + 50):
            if self.angle < self.MAX_ROTATION:
                self.angle = self.MAX_ROTATION
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_VELOCITY
    
    def design(self, screen):
        # Definir a imagem do pássaro
        self.image_count += 1

        if self.image_count < self.TIME_ANIMATION:
            self.image = self.IMAGES[0]
        elif self.image_count < self.TIME_ANIMATION*2:
            self.image = self.IMAGES[1]
        elif self.image_count < self.TIME_ANIMATION*3:
            self.image = self.IMAGES[2]
        elif self.image_count < self.TIME_ANIMATION*4:
            self.image = self.IMAGES[1]
        elif self.image_count < (self.TIME_ANIMATION*4 + 1):
            self.image = self.IMAGES[0]
            self.image_count = 0

        # Não vai bater asa caso o pássaro esteja caindo
        if self.angle <= -80:
            self.image = self.IMAGES[1]
            self.image_count = self.TIME_ANIMATION*2
        
        image_rotation = pygame.transform.rotate(self.image, self.angle)
        position_center_image = self.image.get_rect(topleft=(self.x, self.y))
        rectangle = image_rotation.get_rect(center=position_center_image)
        screen.blit(image_rotation, rectangle)
    
    def get_mask(self):
        pygame.mask.from_surface(self.image)


class Pipe:
    ...

class Floor:
    ...