#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.const import ENTITY_SHOT_DELAY, ENTITY_SPEED, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_UP, WIN_HEIGHT, WIN_WIDTH
from code.enemyShot import EnemyShot
from code.entity import Entity
import random

from code.player import Player



class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.spawn_time_ms = pygame.time.get_ticks() # Get the current time in milliseconds from spawn
        self.shot_sound = pygame.mixer.Sound('./assets/' + name + '.wav') # Load the shot sound for the player
        self.shot_sound.set_volume(0.3)  # Set the volume for the shot sound


        # SIRENE
        self.siren_channel = pygame.mixer.Channel(5)  # usa canal específico para sirene
        self.siren_sound = pygame.mixer.Sound('./assets/Sound_siren.wav')
        self.siren_sound.set_volume(0.5)
        self.siren_channel.play(self.siren_sound, loops=-1)  # loop infinito



    def move(self, ): 
        self.rect.centery += ENTITY_SPEED[self.name]                
        

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            self.shot_sound.play()
            return EnemyShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))
        
    def move(self, entity_list=None):
        # 1) sempre desce
        self.rect.centery += ENTITY_SPEED[self.name]

        # 2) procura o player1 na lista, se existir
        if entity_list is not None:
            p1 = next((e for e in entity_list if isinstance(e, Player)), None)
            if p1:
                # ajusta X para “seguir” o p1
                if self.rect.centerx < p1.rect.centerx:
                    self.rect.centerx += ENTITY_SPEED[self.name]
                elif self.rect.centerx > p1.rect.centerx:
                    self.rect.centerx -= ENTITY_SPEED[self.name]
