import pygame
from abc import ABC, abstractmethod
from gameobjects.gameobject import GameObject


class Block(GameObject, ABC):
    def __init__(self, width=1, height=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height

    @abstractmethod
    def draw(self, window):
        pass

    def boundRect(self):
        return [self.x, self.y, self.x + self.width, self.y + self.height]


class ColorBlock(Block):
    def __init__(self, alpha=255, color=(0, 0, 0), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.alpha = alpha
        self.color = color
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.set_alpha(alpha)
        self.surf.fill(color)

    def draw(self, window):
        window.blit(self.surf, (self.x, self.y))


class TextureBlock(Block):
    texture_model: int

    def draw(self, window):
        window.blit(pygame.transform.scale(self.texture_model, (self.width, self.height)), (self.x, self.y))


class BrickTextureBlock(TextureBlock):
    texture_model = pygame.image.load("assets/img/brick_square_tile.png")


class SteelTextureBlock(TextureBlock):
    texture_model = pygame.image.load("assets/img/steel_square_tile.png")

