#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import Vector2
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Civilians(Entity):
    def __init__(self, name:str, position:tuple, ):
        super().__init__(name, position)
       

    def move(self):        
        self.rect.centery += ENTITY_SPEED[self.name] 
      