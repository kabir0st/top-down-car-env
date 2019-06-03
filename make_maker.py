import pygame 
import numpy as np 
import os 
from pygame.locals import * 
class Game(object):
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car")
        width = 1336 
        height = 768 
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        state = 0
        self.map_coordinates = []
        start = []
        end = []
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        
        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print('Mouse at : ',event.pos)
                    if state == 0:
                        start = event.pos
                        state = 1
                    elif state == 1:
                        end = event.pos
                        state = 2
            if state == 2:
                print("saving starting point ",start," and end point ",end)
                self.map_coordinates.append((start,end))
                print(self.map_coordinates)
                state = 0
            self.update()

    def update(self):
        self.screen.fill((0,0,0))
        for coordinates in self.map_coordinates:
            start = coordinates[0]
            end = coordinates[1]
            pygame.draw.line(self.screen, (255,0,0),start,end,5)
        pygame.display.flip()
        


if __name__ == "__main__":
    game = Game()
    game.run()
