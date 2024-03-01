import pygame,random
from core import Engine
from constants import *
class Snake:
    def __init__(self,engine:Engine):
        self.engine = engine
        self.length = 1
        self.positions = [((engine.width // 2), (engine.height // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.border = False

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        if self.engine.border:
            if cur[0]+20 >= self.engine.width or  cur[1]+20 >= self.engine.height or cur[0]-20 >= self.engine.width or  cur[1]-20 >= self.engine.height:
                self.reset()
                return
        x, y = self.direction
        new = (((cur[0] + (x*self.engine.gridSize)) % self.engine.width), (cur[1] + (y*self.engine.gridSize)) % self.engine.height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((self.engine.width // 2), (self.engine.height // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], self.engine.gridSize,self.engine.gridSize))

class Food:
    def __init__(self,engine:Engine):
        self.engine = engine
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (self.engine.width//self.engine.gridSize)-1) * self.engine.gridSize,
                         random.randint(0, (self.engine.height//self.engine.gridSize)-1) * self.engine.gridSize)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], self.engine.gridSize,self.engine.gridSize))