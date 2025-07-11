#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from pygame import Vector2
import pygame
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Civilians(Entity):
    def __init__(self, name:str, position:tuple, ):
        super().__init__(name, position)
        
       

    def move(self):        
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT: 
            if random.random() < 0.5: # 50% chance to respawn the civilian
                resp_civ = random.randint(-800,-200)
                self.rect.bottom = resp_civ
                #print(f'civ {self.name} respawned at {resp_civ}')
            else:
                #print(f'civ {self.name} destroyed)')
                pass
      