import pygame
from engine import Engine


class Camera:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    @staticmethod
    def pointRelativePosition(cls, point1, point2):
        res = []
        if point1[0] < point2[0]:
            res += ["xl", "xle"]
        elif point1[0] == point2[0]:
            res += ["xle", "xe", "xge"]
        elif point1[0] == point2[0]:
            res += ["xg", "xge"]
        if point1[1] < point2[1]:
            res += ["yl", "yle"]
        elif point1[1] == point2[1]:
            res += ["yle", "ye", "yge"]
        elif point1[1] == point2[1]:
            res += ["yg", "yge"]
        return res

    def isVisible(self, obj):
        if Camera.pointRelativePosition(obj.mostLUPoint(), (0, 0), ["xle", "yle"])

    def sieve(self, scene):
        i = 0
        while i < len(scene):
            if not self.isVisible(scene[i]):
                scene.pop(i)
        return scene


class Displayer:
    def __init__(self, name="МОЯ ИГРА", width=800, height=600):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.engine = Engine(width, height)
        self.camera = Camera()
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
            print(len(self._scene)
            for obj in self._scene:
                obj.draw(self.window)
            pygame.display.update()
            self.clock.tick(fps)
        pygame.quit()

