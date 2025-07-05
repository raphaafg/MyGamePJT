import random
from pygame import Vector2
import pygame
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Boost(Entity):
    def __init__(self, name:str, position:tuple, ):
        super().__init__(name, position)
       

    def move(self):        
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT: 
            if random.random() < 0.50: # 50% chance to respawn the civilian
                self.rect.bottom = -200
                #print(f'Enemy {self.name} respawned ')
            else:
                #print(f'Enemy {self.name} destroyed)')
                pass
