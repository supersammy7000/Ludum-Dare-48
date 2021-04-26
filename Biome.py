import os, sys
import random

import pygame.sprite


class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64)).convert_alpha()
        self.rect = self.image.get_rect()
        self.imageList = []
        self.imageList.append(self.load('grass1.png'))
        self.imageList.append(self.load('grass2.png'))
        self.counter = 0
        self.pos = (x,y)
        self.UPs = random.randint(0,80)

    def change(self):
        self.counter += 1
        self.image = self.imageList[self.counter % 2]

    def update(self, mapRect):
        self.rect = mapRect.move(self.pos)
        self.UPs += 1
        if self.UPs > 80:
            self.UPs = 0
            self.change()



    def load(self, name):
        fullname = os.path.join('data', name)
        try:
            self.image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        return self.image.convert_alpha()

class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,128)).convert_alpha()
        self.image = self.load('tree.png')
        self.rect = self.image.get_rect()
        #self.imageList = []
        #self.imageList.append(self.load('tree.png'))
        #self.imageList.append(self.load('grass2.png'))
        self.counter = 0
        self.pos = (x,y)
        self.UPs = random.randint(0,80)

    def change(self):
        self.counter += 1
        self.image = self.imageList[self.counter % 2]

    def update(self, mapRect):
        self.rect = mapRect.move(self.pos)
        self.UPs += 1
        #if self.UPs > 80:
            #self.UPs = 0
            #self.change()
    def load(self, name):
        fullname = os.path.join('data', name)
        try:
            self.image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        return self.image.convert_alpha()

class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,16)).convert_alpha()
        self.image = self.load('rock.png')
        self.rect = self.image.get_rect()
        #self.imageList = []
        #self.imageList.append(self.load('tree.png'))
        #self.imageList.append(self.load('grass2.png'))
        self.counter = 0
        self.pos = (x,y)
        self.UPs = random.randint(0,80)

    def change(self):
        self.counter += 1
        self.image = self.imageList[self.counter % 2]

    def update(self, mapRect):
        self.rect = mapRect.move(self.pos)
        self.UPs += 1
        #if self.UPs > 80:
            #self.UPs = 0
            #self.change()
    def load(self, name):
        fullname = os.path.join('data', name)
        try:
            self.image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        return self.image.convert_alpha()