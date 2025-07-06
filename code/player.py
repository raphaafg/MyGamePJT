#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.const import ENTITY_HEALTH, ENTITY_SHOT_DELAY, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_BOOST, PLAYER_KEY_UP, WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity
from code.playerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_limit = 0
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Set the shot delay for the player
        self.shot_sound = pygame.mixer.Sound('./assets/' + name + '.wav') # Load the shot sound for the player
        self.shot_sound.set_volume(0.3)  # Set the volume for the shot sound

        #BOOST4
        self.boost_invincible_timer = 0
        self.boost_speed_extra = 0
        self.boost_nitro_img = pygame.image.load('./assets/nitro.png').convert_alpha()
        
        

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name] + self.boost_speed_extra
        #if I set ELIF here, the player will not be able to move diagonally, because it is if or another if. That way it is if and another if.
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: 
            self.rect.centery += ENTITY_SPEED[self.name] + self.boost_speed_extra
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 100:
            self.rect.centerx -= ENTITY_SPEED[self.name] + self.boost_speed_extra
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH-100:
            self.rect.centerx += ENTITY_SPEED[self.name] + self.boost_speed_extra
        

        if self.boost_invincible_timer > 0:
            nitro_rect = self.boost_nitro_img.get_rect(midtop=(self.rect.centerx, self.rect.bottom))
            
            
        if self.boost_invincible_timer > 0:
            self.boost_invincible_timer -= 1
            if self.boost_invincible_timer == 0:
                self.boost_speed_extra = 0  # volta à velocidade normal


        pass 

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            if self.shot_limit > 0:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                pressed_key = pygame.key.get_pressed()
                if pressed_key[PLAYER_KEY_BOOST[self.name]]:
                    self.shot_limit -= 1  # usa um tiro
                    self.shot_sound.play()
                    return PlayerShot(name=f"{self.name}Shot", position=(self.rect.centerx, self.rect.centery))
            else:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]
                pressed_key = pygame.key.get_pressed()
                if pressed_key[PLAYER_KEY_BOOST[self.name]]:
                    no_ammo_sound = pygame.mixer.Sound('./assets/Sound_noammo.wav')
                    no_ammo_sound.set_volume(0.5)
                    no_ammo_sound.play()

    def hp(self):
        self.health = ENTITY_HEALTH[self.name]
        
    