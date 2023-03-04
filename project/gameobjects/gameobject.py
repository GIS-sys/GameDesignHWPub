from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, x=0, y=0, z=1, weight=1, speed=(0, 0), *args, **kwargs):
        self.x = x
        self.y = y
        self.z = z
        self.weight = weight
        self.speed = speed

    @abstractmethod
    def draw(self, window):
        pass

