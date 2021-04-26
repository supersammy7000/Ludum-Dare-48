#!/usr/bin/python

import os, sys
import pygame
from pygame.locals import *
import Character
import Biome
import random


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((960, 720))
    pygame.display.set_caption('Forest Adventure')
    clock = pygame.time.Clock()

    # Background image
    map, mapRect = load_image("map.png")
    background = pygame.Surface(screen.get_size()).convert()
    background.fill((30, 70, 30))
    mapSprite = pygame.sprite.Sprite()
    mapSprite.image = map
    mapSprite.rect = mapRect
    mapSprite.rect.move_ip(-2400,-1800)


    #constants
    plains = (232,231,186)
    trees = (50,90,31)
    forest = (24, 50, 12)
    blue = (23, 21, 98) # not used change black(amazon) to this color


    # Sprite Group
    allSprites = pygame.sprite.Group()
    grassland = pygame.sprite.Group()
    treeland = pygame.sprite.Group()
    forestland = pygame.sprite.Group()
    amazonland = pygame.sprite.Group()

    #Frogs
    #froggy = Character.Frog()

    #allSprites.add(froggy)


    #Field sprites
    for i in range(2000):
        pos = (random.randint(0,4799),random.randint(0,3599))
        color = mapSprite.image.get_at(pos)
        if color == plains:
            if i % 2 == 0:
                grassland.add(Biome.Grass(pos[0]-32,pos[1]-32))
            else:
                grassland.add(Character.Cricket(pos[0]-8,pos[1]-8))
        elif color == trees:
            if i % 4 != 0:
                treeland.add(Biome.Tree(pos[0]-32,pos[1]-96))
            else:
                treeland.add(Character.Squirrel(pos[0]-12,pos[1]-12))
        elif color == forest:
            forestland.add(Character.Frog(pos))
        elif color == blue:
            if i % 2 == 0:
                amazonland.add(Character.Fish(pos[0]-12,pos[1]-12))
            else:
                amazonland.add(Biome.Rock(pos[0]-8,pos[1]-8))

    # Character
    char = Character.Main(2400,1800)
    allSprites.add(char)
    char.speed = 5

    #keyboard setup
    wasd = [False]*4


    # Event loop
    UPs = 0
    while 1:
        UPs += 1
        if UPs > 60:
            UPs = 0
        # Game logic
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    char.move(0)
                    mapSprite.rect.move_ip(0,char.speed)
                    wasd[0] = True
                if event.key == K_RIGHT or event.key == K_d:
                    char.move(1)
                    mapSprite.rect.move_ip(-char.speed,0)
                    wasd[1] = True
                if event.key == K_DOWN or event.key == K_s:
                    char.move(2)
                    mapSprite.rect.move_ip(0,-char.speed)
                    wasd[2] = True
                if event.key == K_LEFT or event.key == K_a:
                    char.move(3)
                    mapSprite.rect.move_ip(char.speed,0)
                    wasd[3] = True
                if event.key == K_f: #debug key
                    #froggy.randomMove()
                    pass
                if event.key == K_ESCAPE:
                    return
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_w:
                    wasd[0] = False
                if event.key == K_RIGHT or event.key == K_d:
                    wasd[1] = False
                if event.key == K_DOWN or event.key == K_s:
                    wasd[2] = False
                if event.key == K_LEFT or event.key == K_a:
                    wasd[3] = False

        if UPs % 2 == 0:
            if wasd[0]:
                char.move(0)
                mapSprite.rect.move_ip(0,char.speed)
            if wasd[1]:
                char.move(1)
                mapSprite.rect.move_ip(-char.speed, 0)
            if wasd[2]:
                char.move(2)
                mapSprite.rect.move_ip(0, -char.speed)
            if wasd[3]:
                char.move(3)
                mapSprite.rect.move_ip(char.speed, 0)




        # Sprite Update
        allSprites.update(mapSprite.rect)




        # Draw calls
        screen.fill((0,0,0))
        pygame.sprite.RenderPlain(mapSprite).draw(screen) #Render background
        print(char.pos, char.rect.center)
        try:
            if mapSprite.image.get_at((char.pos[0]+32,char.pos[1]+32)) == trees and screen.get_rect().width == 960:
                screen = pygame.display.set_mode((800, 600))
                mapSprite.rect.move_ip(-80,-60)
                char.speed = 4
            elif mapSprite.image.get_at((char.pos[0]+32,char.pos[1]+32)) == plains and screen.get_rect().width == 800:
                screen = pygame.display.set_mode((960, 720))
                mapSprite.rect.move_ip(80,60)
                char.speed = 5

            elif mapSprite.image.get_at((char.pos[0] + 32, char.pos[1] + 32)) == forest and screen.get_rect().width == 800:
                screen = pygame.display.set_mode((600, 400))
                mapSprite.rect.move_ip(-100,-100)
                char.speed = 2
            elif mapSprite.image.get_at((char.pos[0] + 32, char.pos[1] + 32)) == trees and screen.get_rect().width == 600:
                screen = pygame.display.set_mode((800, 600))
                mapSprite.rect.move_ip(100,100)
                char.speed = 4


            elif mapSprite.image.get_at((char.pos[0] + 32, char.pos[1] + 32)) == blue and screen.get_rect().width == 600:
                screen = pygame.display.set_mode((400, 300))
                mapSprite.rect.move_ip(-100, -50)
                char.speed = 1
            elif mapSprite.image.get_at((char.pos[0] + 32, char.pos[1] + 32)) == forest and screen.get_rect().width == 400:
                screen = pygame.display.set_mode((600, 400))
                mapSprite.rect.move_ip(100, 50)
                char.speed = 2



        except:
            print("Negitive position off map")
        allSprites.draw(screen) #Render all sprites(character, frogs, grass)
        if screen.get_rect().width == 960:
            grassland.update(mapSprite.rect)
            grassland.draw(screen)
        elif screen.get_rect().width == 800:
            treeland.update(mapSprite.rect)
            treeland.draw(screen)
        elif screen.get_rect().width == 600:
            forestland.update(mapSprite.rect)
            forestland.draw(screen)
        elif screen.get_rect().width == 400:
            amazonland.update(mapSprite.rect)
            amazonland.draw(screen)
        pygame.display.flip() #display on screen
        clock.tick(60) #game tick


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


if __name__ == '__main__': main()
