#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.const import ENTITY_SHOT_DELAY, ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.enemyShot import EnemyShot
from code.entity import Entity
import random



class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.spawn_time_ms = pygame.time.get_ticks() # Get the current time in milliseconds from spawn
        self.shot_sound = pygame.mixer.Sound('./assets/' + name + '.wav') # Load the shot sound for the player
        self.shot_sound.set_volume(0.3)  # Set the volume for the shot sound



    def move(self, ): 
# Move the enemy to the left but, set the enemy not destroyed by shot to the right side of the screen again closer to the player related to the time elapsed since spawn
        
        self.rect.centery += ENTITY_SPEED[self.name]                
        if self.rect.top <= 0: #if the top side of a image gets 0, set the left side to the final right again
            if random.random() < 0.5: #50% chance to respawn the enemy
                self.rect.bottom = WIN_HEIGHT
                ##print(f'Enemy {self.name} respawned at {self.rect.left} after {elapsed_s:.2f}s')
            else:
                ##print(f'Enemy {self.name} destroyed)')
                pass 

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            self.shot_sound.play()
            return EnemyShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))
