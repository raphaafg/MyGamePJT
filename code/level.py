#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
import pygame
from code.background import Background
from code.const import COLOR_BLUESKY, COLOR_FLAME, COLOR_TURBOBLUE, COLOR_TURBOGREEN, COLOR_FLAME, COLOR_WHITE, ENEMY_SPAWN, ENTITY_SPEED, EVENT_CIV_SPAWN, EVENT_TIMEOUT, MENU_OPTION, PROGRESSO_CHEGADA, PROGRESSO_LARGADA, TIME_CIVILIAN_SPAWN, TIME_ENEMY_SPAWN, TIMEOUT_STAGE, TIMEOUT_STEP, WIN_HEIGHT, WIN_POSX_RUA1, WIN_POSX_RUA2, WIN_POSX_RUA3
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window: pygame.Surface, name: str, game_mode: str, player_score:list[int]):
        self.timeout = TIMEOUT_STAGE #ms = 95seconds
        self.total_time = TIMEOUT_STAGE

        self.window = window
        self.name = name
        self.game_mode = game_mode #game mode selected in the menu (menu_option)

        ##---------DEFINIÇÃO DAS FERRAMENTAS PARA PROGRESSO E BARRAS---------##
        self.distance       = PROGRESSO_LARGADA
        self.distance_goal  = PROGRESSO_CHEGADA
         # 3) configurações das duas barras
        self.dist_bar_rect = pygame.Rect(30,  200, 50, 500)
        self.dist_bar_col  = COLOR_TURBOGREEN # cor da distância
        self.bar_border    = COLOR_WHITE      # cor da borda das duas


        LEVEL_MAP = {
            'MAP01': 'Map01',
            'MAP02': 'Map02'
        }
        entity_factory_key = LEVEL_MAP.get(self.name)
        if entity_factory_key is None:
            raise ValueError(f'nenhum lvl configurado para {self.name}')
        
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(entity_factory_key))  # Get the entities MAP1 1 or 2

        #adding player and keepinh score
        p1 = EntityFactory.get_entity('Player1')
        p1.score = player_score[0]
        self.player = p1
        self.entity_list.append(p1)
        if self.game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            p2 = EntityFactory.get_entity('Player2')
            p2.score = player_score[1]
            self.entity_list.append(p2)

        #adding CIVILIAN
        pygame.time.set_timer(EVENT_CIV_SPAWN, TIME_CIVILIAN_SPAWN)

        #adding ENEMY
        pygame.time.set_timer(ENEMY_SPAWN, TIME_ENEMY_SPAWN)  # Set a timer to spawn enemies every 2 seconds


        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) #100ms

    def run(self, player_score:list[int]):
        pygame.mixer.music.load('./assets/Sound_Race1.mp3')  # Load the background music for level 1
        pygame.mixer.music.set_volume(1.5)
        pygame.mixer.music.play(loops=-1)
        clock = pygame.time.Clock()  # Create a clock to control FPS
           
        ##---------MAIN GAME LOOP---------##
        while True:
            clock.tick(60)
            self.window.fill((0,0,0)) #reset screen

            for ent in self.entity_list:

                if isinstance(ent, Background):
                    old_top = ent.rect.top
                    ent.move()
                    if ent.rect.top >= WIN_HEIGHT-ENTITY_SPEED[self.name]:
                        self.distance += 1
                        print(f'distancia percorrida = {self.distance}')


                elif isinstance(ent, Enemy):
                    ent.move(entity_list=self.entity_list)
                else:
                    ent.move()

                self.window.blit(source=ent.surf, dest=ent.rect)  # Draw each entity on the window

                if isinstance(ent,(Player, Enemy)):
                    shoot = ent.shoot()  # If the entity is a player or enemy, check if it can shoot
                    if shoot is not None:
                        self.entity_list.append(shoot) # Add the shot to the entity list if it exists
                
                ##---------SHOW HEALTH OF PLAYERS---------##
                if ent.name == 'PlayerA0':
                    self.level_text( 14, f'Player 1 -    Health: {ent.health}    Score: {ent.score}', COLOR_BLUESKY,(10, 20))             
                if ent.name == 'PlayerB0':
                    self.level_text( 14, f'Player 2 -    Health: {ent.health}    Score: {ent.score}', COLOR_FLAME,(10, 35))




                ##---------CREATING BAR PROGRESS---------##
                
                #desenha a barrinha de distância
                h_dist = self.distance * self.dist_bar_rect.height // self.distance_goal
                bar = self.dist_bar_rect
                fill = pygame.Rect(bar.x,bar.y + (bar.height - h_dist),bar.width,h_dist)
                pygame.draw.rect(self.window, self.bar_border, bar, 4)
                pygame.draw.rect(self.window, self.dist_bar_col, fill)

                #checa vitória ou derrota
                if self.distance >= self.distance_goal:
                    return True   # chegou na linha de chegada antes do tempo: GANHOU
                if self.timeout <= 0:
                    return False  # acabou o tempo antes da chegada: PERDEU


                

            ##---------CHECK FOR ALL EVENTS---------##
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Exit the game if the window is closed 



                ##---------SPAWN OF ENEMIES---------##
                if event.type == ENEMY_SPAWN:
                    px = self.player.rect.centerx
                    enemy = EntityFactory.get_entity('Enemy1',(px,-200))
                    self.entity_list.append(enemy)
                    #choice = random.choice(['Enemy1', 'Enemy2'])  # Randomly choose an enemy type to spawn
                    #self.entity_list.append(EntityFactory.get_entity(choice))  #add a random enemy to the entity list
                
                ##---------SPAWN CIVILIANS---------##    
                if event.type == EVENT_CIV_SPAWN:
                    x1 = random.randint(WIN_POSX_RUA1, WIN_POSX_RUA2)
                    x2 = random.randint(WIN_POSX_RUA2, WIN_POSX_RUA3)
                    x = random.choice([x1, x2])
                    #print(f'SPAWN AT {x}')
                    y = -200   # começa fora de tela, acima
                    civ = EntityFactory.get_entity('Civilians', position=(x, y))
                    self.entity_list.append(civ)  

                ##---------TIMEOUT EVENT---------##
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:  # If the timeout reaches zero, end the level
                        for ent in self.entity_list:
                            if ent.name == 'PlayerA0':
                                ent.score += ent.health  # Add the remaining health to the score
                                player_score[0] = ent.score
                            if ent.name == 'PlayerB0':
                                ent.score += ent.health  # Add the remaining health to the score
                                player_score[1] = ent.score
                        return True  # Return True to indicate the level is finished
                    
            

                ##---------CHECK PLAYER ALIVE---------##
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    print('GAME OVER')
                    return False       


                


           
            
            
            #printed text on the screen
            self.level_text( 14, f'{self.name} - Timeout: {self.timeout / 1000:.0f}s', COLOR_TURBOBLUE,(10, 5)) #show the level name and timeout
            self.level_text( 14, f'FPS: {clock.get_fps():.0f}', COLOR_TURBOBLUE,(10, WIN_HEIGHT - 30)) #show the current FPS
            self.level_text( 14, f'Entidades: {len(self.entity_list)}', COLOR_TURBOBLUE,(10, WIN_HEIGHT - 45)) #show number of entities




            pygame.display.flip()


            #---------COLLISION AND HEALTH CHECK---------##
            EntityMediator.verify_collision(entity_list=self.entity_list)  # Check for collisions between entities
            EntityMediator.verify_health(entity_list=self.entity_list)
        

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        Font = pygame.font.SysFont(name="bauhaus93", size=text_size) #cria a fonte
        Surface = Font.render(text, True, text_color).convert_alpha() #renderiza o texto com a fonte, antialiasing e cor
        Rect = Surface.get_rect(topleft = text_pos) #centra o retangulo do texto na posicao especificada
        self.window.blit(source=Surface, dest=Rect) #blit padrao, ou seja, desenha o texto na janela
