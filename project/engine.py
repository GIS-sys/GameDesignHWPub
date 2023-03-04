import pygame
import random
from gameobjects.blocks import ColorBlock, BrickTextureBlock, SteelTextureBlock


class Engine:
    def __init__(self, screen_width, screen_height):
        self.iter = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = BrickTextureBlock(speed=(3, 3), width=screen_width, height=screen_height, z=2, x=30)
        self.objects = [ColorBlock(color=(255,0,0), alpha=128, width=50, height=50, speed=(3, 3), z=-1),
                        BrickTextureBlock(speed=(3, 3), width=30, height=30, z=2),
                        BrickTextureBlock(speed=(3, 3), width=30, height=30, z=2, x=30),
                        SteelTextureBlock(speed=(3, 3), width=20, height=20)]

    def loadLevel(self, path):
        pass

    def update(self):
        self.iter += 1
        for obj in self.objects:
            obj.x += obj.speed[0]
            obj.y += obj.speed[1]

    def getObjectsForDisplay(self):
        self.objects.sort(key=lambda obj: -obj.z)
        return [self.background, *self.objects]

