import pygame 
import json
import os 
from pygame.locals import *


FPS = 60

class Game(object):
    
    def __init__(self):
        pygame.init()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        car_image_temp = pygame.image.load(image_path)
        self.car_image = pygame.transform.scale(car_image_temp, (40,40))
        pygame.display.set_caption("Car")
        width = 1336 
        height = 768 
        self.screen = pygame.display.set_mode((width, height))
        self.FPSCLOCK = pygame.time.Clock()
        self.exit = False

    def run(self):
        self.current_line_start = 0
        self.current_line_end = 0
        self.car_spawn_point = (0,0)
        car = False
        new_line = True
        mouse_pos = (0,0)
        self.map_coordinates = []

        while not self.exit:
            self.screen.fill((50,50,50))
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.exit = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.exit = True
                    if event.key == K_s:
                        self.exit = True
                    if not new_line:
                        if event.key == K_n:
                                print("Creating new sequences of lines.")
                                new_line = True

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not car:
                        self.car_spawn_point = event.pos
                        print("Spawn point",event.pos)
                        car = True
                        print(car)
                    else:
                        if new_line:
                            self.current_line_start = event.pos
                            print(self.current_line_start, event.pos)
                            new_line = False
                        elif not new_line:
                            self.current_line_end = event.pos
                            self.map_coordinates.append((self.current_line_start,self.current_line_end))
                            self.current_line_start = event.pos
                    
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
            if not car:
                self.screen.blit(self.car_image,mouse_pos)
            else:
                self.screen.blit(self.car_image,self.car_spawn_point)
                if not new_line:    
                    pygame.draw.line(self.screen, (0,00,00), self.current_line_start, mouse_pos, 2)

            #updating
            for coordinates in self.map_coordinates:
                start = coordinates[0]
                end = coordinates[1]
                pygame.draw.line(self.screen, (250,150,50),start,end,4)
            # print(self.FPSCLOCK.get_fps())
            pygame.display.flip()
            self.FPSCLOCK.tick(FPS)
        

    def save(self,map_name):
        print(self.map_coordinates)
        print()
        save_json = {'map':self.map_coordinates, 'spawn_point': self.car_spawn_point}
        print(save_json)
        map_name = "maps/"+map_name+".json"
        try:
            with open(map_name,'w') as json_file:
                json.dump(save_json,json_file)
            print("Map saved")
        except:
            print("Error occured while saving map.")
            

if __name__ == "__main__":
    print("         How to Use ")
    print(" - Draw map by clicking and creating lines.")
    print(" - Press 'n' to set new sequence of lines.")
    print(" - press 'c' to define starting point for the car.")
    print(" - Press 's' to save the created map.")
    print(" - Press 'r' to clear the canvas and start drawing again.")
    # ans = "y"
    # while ans.lower != "y":
    game = Game()
    game.run()
    pygame.quit()
    map_name = input("\nSave Map as  : ")
    game.save(map_name)
    # ans = input("Draw another map ? (y/n) ")

    
