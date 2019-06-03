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
        self.current_line_start = 0.0
        self.current_line_end = 0.0
        new_line = True
        self.map_coordinates = []

        while not self.exit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.exit = True
                        print(new_line)
                    if not new_line:
                        if event.key == K_n:
                                print("Creating new sequences of lines.")
                                new_line = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if new_line:
                        self.current_line_start = event.pos
                        print(self.current_line_start, event.pos)
                        new_line = False
                    else:
                        self.current_line_end = event.pos
                        self.map_coordinates.append((self.current_line_start,self.current_line_end))
                        self.current_line_start = event.pos
                if not new_line: 
                    if event.type == pygame.MOUSEMOTION:
                        pygame.draw.line(self.screen, (100,100,100), self.current_line_start, event.pos, 3)
            self.update()



        # while not self.exit:

        #     for event in pygame.event.get():
        #         if not new_line:
        #             pygame.draw.line(self.screen, (100,100,100),self.current_line_start,event.pos,3)
        #         if event.type == pygame.QUIT:
        #             self.exit = True
        #         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #             print('Mouse at : ',event.pos)
        #             if state == 0:
        #                 start = event.pos
        #                 state = 1
        #             elif state == 1:
        #                 end = event.pos
        #                 state = 2
        #         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        #             try:
        #                 x = self.map_coordinates.pop()
        #                 print(x," point removed.")
        #             except:
        #                 print("Array is empty.")
                    
        #     if state == 2:
        #         print("saving starting point ",start," and end point ",end)
        #         self.map_coordinates.append((start,end))
        #         print(self.map_coordinates)
        #         state = 0
        #     self.update()

    def update(self):
        self.screen.fill((0,0,0))
        for coordinates in self.map_coordinates:
            start = coordinates[0]
            end = coordinates[1]
            pygame.draw.line(self.screen, (255,0,0),start,end,3)
        pygame.display.flip()
        


if __name__ == "__main__":
    game = Game()
    game.run()
