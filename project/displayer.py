import pygame
from engine import Engine


class Camera:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def isVisible(self, obj):
        x0, y0, x1, y1 = obj.boundRect()
        if x1 < 0 or x0 > self.screen_width:
            return False
        if y1 < 0 or y0 > self.screen_height:
            return False
        return True

    def sieve(self, scene):
        i = 0
        while i < len(scene):
            if not self.isVisible(scene[i]):
                scene.pop(i)
            else:
                i += 1
        return scene


class Displayer:
    def __init__(self, name="МОЯ ИГРА", width=800, height=600):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.engine = Engine(width, height)
        self.camera = Camera(width, height)
        self.running = False

    def run(self, fps=60):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.window.fill((255, 255, 255))
            self.engine.update()
            self._scene = self.engine.getObjectsForDisplay()
            self._scene = self.camera.sieve(self._scene)
            for obj in self._scene:
                obj.draw(self.window)
            pygame.display.update()
            self.clock.tick(fps)
        pygame.quit()

