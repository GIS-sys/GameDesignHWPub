import pygame


class Displayer:
    def __init__(self, engine, name="МОЯ ИГРА", width=800, height=600):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.engine = engine
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
            for obj in self._scene:
                obj.draw(self.window)
            pygame.display.update()
            self.clock.tick(fps)
        pygame.quit()

