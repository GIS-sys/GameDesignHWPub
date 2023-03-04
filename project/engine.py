import pygame
import random
from gameobjects.blocks import ColorBlock, BrickTextureBlock, SteelTextureBlock


class Engine:
    def __init__(self):
        self.iter = 0
        self.objects = [ColorBlock(color=(255,0,0), width=10, height=10, speed=(3, 3)),
                        BrickTextureBlock(speed=(3, 3), width=30, height=30, z=2),
                        BrickTextureBlock(speed=(3, 3), width=30, height=30, z=2, x=30),
                        SteelTextureBlock(speed=(3, 3), width=20, height=20)]

    def update(self):
        self.iter += 1
        for obj in self.objects:
            obj.x += obj.speed[0]
            obj.y += obj.speed[1]

    def getObjectsForDisplay(self):
        self.objects.sort(key=lambda obj: -obj.z)
        return self.objects

