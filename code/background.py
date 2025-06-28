#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import Vector2
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Background(Entity):
    def __init__(self, name:str, position:tuple, ):
        super().__init__(name, position)
       

    def move(self):        
        self.rect.centery += ENTITY_SPEED[self.name] #using the const to set the speed for each background image, moving it to down (-)
        #it is necessary to set self.name because it is a dict and the key is the name to reach the value (speed) of the dict ENTITY_SPEED
                
        if self.rect.top >= WIN_HEIGHT: 
            self.rect.bottom = 0
            PROGRESSO_COUNT +=1
      