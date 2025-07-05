#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from code.background import Background
from code.boost import Boost
from code.civilians import Civilians
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.enemy import Enemy
from code.player import Player


class EntityFactory: #design pattern factory doesnt need a init
    

    @staticmethod 
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            #lvl1 factory
            case 'Map01':
                list_bg = []
                for i in range (2): # 4 backgrounds images for level 1
                    list_bg.append(Background(f'Map1{i}', (0,0)))
                    list_bg.append(Background(f'Map1{i}', (0,WIN_HEIGHT)))
                return list_bg
            
            #lvl2 factory
            case 'Map02':    
                list_bg = []
                for i in range (2): # 3 backgrounds images for level 2
                    list_bg.append(Background(f'Map2{i}', (0,0)))
                    list_bg.append(Background(f'Map2{i}', (0,WIN_HEIGHT)))
                return list_bg
            
            #Player1 factory
            case 'Player1':
                return Player('PlayerA0', ((WIN_WIDTH/2-90) , (650)))
            #Player2 factory    
            case 'Player2':
                return Player('PlayerB0', ((WIN_WIDTH/2+70) , (650)))
            
            #Enemy1 factory
            case 'Enemy1':
                px, _ = position
                return Enemy('Enemy1', (px, 0))
            #Enemy2 factory
            # case 'Enemy2':
            #     return Enemy('Enemy2', (WIN_WIDTH + 15, random.randint(50, WIN_HEIGHT - 50)))

            case 'Civilians':
                i = random.randint(1,6)
                sprite_name = f'CIVILIAN{i}'
                return Civilians(sprite_name,position)
            
            case 'Boost':
                i = random.randint(1,5)
                sprite_name = f'boost{i}'
                return Boost (sprite_name,position)


            
            
            