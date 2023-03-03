import pygame
import random


class Rectangle:
    def __init__(self, x, y, speed, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 50
        self.height = 50

    def move(self):
        self.x += self.speed
        self.y += self.speed

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))



class Engine:
    def __init__(self):
        self.rectangles = []
        for i in range(10):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            speed = random.randint(1, 5)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.rectangles.append(Rectangle(x, y, speed, color))

    def update(self):
        for rectangle in self.rectangles:
            rectangle.move()

    def getObjectsForDisplay(self):
        return self.rectangles

