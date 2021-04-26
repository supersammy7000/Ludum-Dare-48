import os

import pygame
import random


class Main(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(350, 350, 64, 64)
        self.image = pygame.Surface((64, 64)).convert_alpha()
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image, (0, 50, 0), (32, 32), 15, 15)
        self.pos = pygame.display.get_surface().get_rect().center
        self.pos = self.pos[0] - 32 + x,self.pos[1] - 32 + y
        self.speed = 10

    def move(self, direction):
        if direction == 0:
            self.pos = self.pos[0],self.pos[1] - self.speed
        if direction == 1:
            self.pos = self.pos[0] + self.speed,self.pos[1]
        if direction == 2:
            self.pos = self.pos[0],self.pos[1] + self.speed
        if direction == 3:
            self.pos = self.pos[0] - self.speed,self.pos[1]

    def update(self, mapRect):
        self.rect = mapRect.move(self.pos)
        self.rect.width = 64
        self.rect.height = 64


class Frog(pygame.sprite.Sprite):
    def __init__(self, pos=(128,180)):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(350, 200, 10, 20)
        self.image = pygame.Surface((10, 20)).convert()
        self.image.fill((20, 150, 20))
        pygame.draw.line(self.image, (0, 0, 0), (0, 3), (3, 3), 2)
        pygame.draw.line(self.image, (0, 0, 0), (6, 3), (9, 3), 2)
        self.pos = pos
        self.UPs = random.randint(0,400)

    def update(self, mapRect):
        self.rect = mapRect.move(self.pos)
        self.UPs += 1
        if self.UPs > 400:
            self.UPs = random.randint(0,100)
            self.randomMove()

    def randomMove(self):
        self.pos = self.pos[0] + random.randint(-45,45),self.pos[1] + random.randint(-45,45)

class Cricket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16)).convert_alpha()
        self.image = self.load('cricket_smoll.png')
        self.rect = self.image.get_rect()
        # self.imageList = []
        # self.imageList.append(self.load('tree.png'))
        # self.imageList.append(self.load('grass2.png'))
        self.counter = 0
        self.pos = (x, y)
        self.UPs = random.randint(0, 200)

    def update(self, mapRect):
        self.rect = mapRect.move(self.pos)
        self.UPs += 1
        if self.UPs > 200:
            self.UPs = random.randint(0, 100)
            self.randomMove()

    def randomMove(self):
        self.pos = self.pos[0] + random.randint(-45, 45), self.pos[1] + random.randint(-45, 45)

    def load(self, name):
        fullname = os.path.join('data', name)
        try:
            self.image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        return self.image.convert_alpha()

class Squirrel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((24, 24)).convert_alpha()
        self.image = self.load('squirrel.png')
        self.rect = self.image.get_rect()
        # self.imageList = []
        # self.imageList.append(self.load('tree.png'))
        # self.imageList.append(self.load('grass2.png'))
        self.counter = 0
        self.pos = (x, y)
        self.UPs = random.randint(0, 200)

    def update(self, mapRect):
        self.rect = mapRect.move(self.pos)
        self.UPs += 1
        if self.UPs > 200:
            self.UPs = random.randint(0, 100)
            self.randomMove()

    def randomMove(self):
        self.pos = self.pos[0] + random.randint(-45, 45), self.pos[1] + random.randint(-45, 45)

    def load(self, name):
        fullname = os.path.join('data', name)
        try:
            self.image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        return self.image.convert_alpha()

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((24, 24)).convert_alpha()
        self.image = self.load('fish.png')
        self.rect = self.image.get_rect()
        # self.imageList = []
        # self.imageList.append(self.load('tree.png'))
        # self.imageList.append(self.load('grass2.png'))
        self.counter = 0
        self.pos = (x, y)
        self.UPs = random.randint(0, 40)

    def update(self, mapRect):
        self.rect = mapRect.move(self.pos)
        self.UPs += 1
        if self.UPs > 40:
            self.UPs = random.randint(0, 10)
            self.randomMove()

    def randomMove(self):
        self.pos = self.pos[0] + random.randint(-9, 9), self.pos[1] + random.randint(-9, 9)

    def load(self, name):
        fullname = os.path.join('data', name)
        try:
            self.image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        return self.image.convert_alpha()