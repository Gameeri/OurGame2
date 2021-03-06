import pygame
from Exceptions import *
from Map import *
from pygame.math import Vector2
from os import path
#hi

img_dir = path.join(path.dirname(__file__), 'image')

RED = (255, 0, 0)
WIDTH = 650*2
HEIGHT = 700*2

tomato = pygame.image.load(path.join(img_dir,'tomato.png'))
tomato = pygame.transform.scale(tomato, (20,20))
bul = pygame.image.load(path.join(img_dir,'bullet_gun.png'))
bul = pygame.transform.scale(bul, (20,20))

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = Vector2(0,0)
        self.direction = 'DOWN'
        self.vel = 0

    def update(self):
        if self.direction == 'RIGHT':
            self.speed.x = self.vel
            self.speed.y = 0
        elif self.direction == 'LEFT':
            self.speed.x = -self.vel
            self.speed.y = 0
        elif self.direction == 'DOWN':
            self.speed.y = self.vel
            self.speed.x = 0
        elif self.direction == 'UP':
            self.speed.y = -self.vel
            self.speed.x = 0
        self.rect.center += self.speed
        # убить, если он заходит за верхнюю часть экрана
        if import pygame
from Exceptions import *
from Map import MAP
from pygame.math import Vector2
from os import path

img_dir = path.join(path.dirname(__file__), 'image')

RED = (255, 0, 0)
WIDTH = 650*2
HEIGHT = 700*2

tomato = pygame.image.load(path.join(img_dir,'tomato.png'))
tomato = pygame.transform.scale(tomato, (20,20))
bul = pygame.image.load(path.join(img_dir,'bullet_gun.png'))
bul = pygame.transform.scale(bul, (20,20))

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = Vector2(0,0)
        self.direction = 'DOWN'
        self.vel = 0

    def update(self):
        if self.direction == 'RIGHT':
            self.speed.x = self.vel
            self.speed.y = 0
        elif self.direction == 'LEFT':
            self.speed.x = -self.vel
            self.speed.y = 0
        elif self.direction == 'DOWN':
            self.speed.y = self.vel
            self.speed.x = 0
        elif self.direction == 'UP':
            self.speed.y = -self.vel
            self.speed.x = 0
        self.rect.center += self.speed
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.y < 0 or self.rect.y > total_level_height or self.rect.x < 0 or self.rect.x > total_level_width or checkBoolet(MAP, self.rect.center):
            self.kill()

class Tomato(Weapon):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = tomato
        self.rect = self.image.get_rect()
        self.vel = 10
        self.rect.center = pos
    def update(self):
        super().update()


class Gun(Weapon):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = bul
        self.rect = self.image.get_rect()
        self.vel = 12
        self.rect.center = pos
    def update(self):
        super().update() or checkBoolet(MAP, self.rect.center):
            self.kill()

class Tomato(Weapon):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = tomato
        self.rect = self.image.get_rect()
        self.vel = 10
        self.rect.center = pos
    def update(self):
        super().update()


class Gun(Weapon):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = bul
        self.rect = self.image.get_rect()
        self.vel = 12
        self.rect.center = pos
    def update(self):
        super().update()
