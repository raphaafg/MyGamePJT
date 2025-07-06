import pygame
from code.boost import Boost
from code.civilians import Civilians
from code.const import HIT_COOLDOWN, WIN_HEIGHT, WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.player import Player
from code.playerShot import PlayerShot


class EntityMediator: #design pattern factory doesnt need a init
    
    _hit_cooldown = HIT_COOLDOWN
    _entity_list_global = []


    @staticmethod 
    #method to verify if the entity is out of the screen, if so, it will set the health to 0
    def __verify_collision_window(ent: Entity): #private method that just works inside this class
        if isinstance(ent, Enemy):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.bottom <= 0:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0
        if isinstance (ent, Civilians):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0
        if isinstance (ent, Boost):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0
            
    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        
        # Check if the entities are of types that can interact with each other
        valid_interaction = False #flag to check if the collision is valid
       
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True    
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Civilians):
            valid_interaction = True    
        elif isinstance(ent1, Civilians) and isinstance(ent2, PlayerShot):
            valid_interaction = True
                
        elif isinstance(ent1, Player) and isinstance(ent2, Civilians):
            EntityMediator._hit_cooldown -= 1
            if EntityMediator._hit_cooldown == 0:
                valid_interaction = True
                EntityMediator._hit_cooldown = HIT_COOLDOWN       
        elif isinstance(ent1, Civilians) and isinstance(ent2, Player):
            EntityMediator._hit_cooldown -= 1
            if EntityMediator._hit_cooldown == 0:
                valid_interaction = True
                EntityMediator._hit_cooldown = HIT_COOLDOWN
                
        ##----checkando boosts----##
        elif isinstance(ent1, Player) and isinstance(ent2, Boost):
            valid_interaction = True    
        elif isinstance(ent1, Boost) and isinstance(ent2, Player):
            valid_interaction = True
        

        
        # Check if the entities are colliding
        if valid_interaction: #== True:
            if (ent1.rect.right >= ent2.rect.left and 
                ent1.rect.left <= ent2.rect.right and 
                ent1.rect.bottom >= ent2.rect.top and 
                ent1.rect.top <= ent2.rect.bottom):
                # If they are colliding, reduce their health by their respective damage
                # verifica escudo (boost_invincible_timer) antes de aplicar dano
                if not (isinstance(ent1, Player) and ent1.boost_invincible_timer > 0):
                    ent1.health -= ent2.damage
                if not (isinstance(ent2, Player) and ent2.boost_invincible_timer > 0):
                    ent2.health -= ent1.damage

                
                # set the last damage source for both entities
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

                EntityMediator.boost(ent1, ent2)



                


                


    @staticmethod
    def __give_score(entidade: Entity, entity_list: list[Entity]):
        if entidade.last_dmg == 'PlayerA0Shot':
            for ent in entity_list:
                if ent.name == 'PlayerA0':
                    ent.score += entidade.score
        elif entidade.last_dmg == 'PlayerB0Shot':
            for ent in entity_list:
                if ent.name == 'PlayerB0':
                    ent.score += entidade.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        EntityMediator._entity_list_global = entity_list
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)): #using i+1 to avoid checking the same pair twice (reduce redundant checks)
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    #method to verify the health of the entities, if the health is 0 or less, it will remove the entity from the list (destroy the entity)
    def verify_health(entity_list: list[Entity]):
        hit_sound = pygame.mixer.Sound('./assets/Sound_hit.wav') # Load the shot sound for the player
        hit_sound.set_volume(0.3)


        for ent in entity_list:
            if isinstance(ent, (Player, Enemy, Civilians)): #define a tuple of types to check if the entity is a Player or an Enemy to make a sound
                if ent.health <= 0:
                    hit_sound.play()
                    if isinstance(ent, (Enemy, Civilians)):
                        EntityMediator.__give_score(ent, entity_list)
                    if isinstance(ent,Enemy):
                        ent.siren_channel.stop()
                    entity_list.remove(ent)
            elif ent.health <= 0:
                entity_list.remove(ent)

    
    @staticmethod
    def boost(ent1,ent2):
        #HP
        if isinstance(ent1, Player) and isinstance(ent2, Boost) and ent2.name == 'boost3':
            ent1.hp()  # aplica o efeito
            pygame.mixer.Sound('./assets/SELECT.wav').play()
            ent2.health = 0  # remove o boost da tela
            ent1.score += 17
            return  # já tratou, não precisa aplicar dano
        elif isinstance(ent2, Player) and isinstance(ent1, Boost) and ent1.name == 'boost3':
            ent2.hp()  # aplica o efeito
            pygame.mixer.Sound('./assets/SELECT.wav').play()
            ent1.health = 0  # remove o boost da tela
            ent2.score += 17
            return  # já tratou, não precisa aplicar dano
        
        #BOMB
        if isinstance(ent1, Player) and isinstance(ent2, Boost) and ent2.name == 'boost0':
            for ent in EntityMediator._entity_list_global:
                if isinstance(ent, (Enemy, Civilians)):
                    ent.health = 0
                sound_bomb = pygame.mixer.Sound('./assets/Sound_bomb.wav')
                sound_bomb.set_volume(0.5)
                sound_bomb.play()
                ent2.health = 0
                ent1.score += 3
            return
        elif isinstance(ent2, Player) and isinstance(ent1, Boost) and ent1.name == 'boost0':
            for ent in EntityMediator._entity_list_global:
                if isinstance(ent, (Enemy, Civilians)):
                    ent.health = 0
            sound_bomb = pygame.mixer.Sound('./assets/Sound_bomb.wav')
            sound_bomb.set_volume(0.5)
            sound_bomb.play()
            ent1.health = 0
            ent2.score += 3
            return
        
        #SHOT
        if isinstance(ent1, Player) and isinstance(ent2, Boost) and ent2.name == 'boost2':
            ent1.shot_limit = 3  # + 3 tiros
            pygame.mixer.Sound('./assets/SELECT.wav').play()
            ent2.health = 0
            return
        elif isinstance(ent2, Player) and isinstance(ent1, Boost) and ent1.name == 'boost2':
            ent2.shot_limit = 4
            pygame.mixer.Sound('./assets/SELECT.wav').play()
            ent1.health = 0
            return
        
        #SHIELD + NITRO
        if isinstance(ent1, Player) and isinstance(ent2, Boost) and ent2.name == 'boost4':
            ent1.boost_invincible_timer = 60 * 5  # 5 segundos (60 FPS x 5)
            ent1.boost_speed_extra = 2
            pygame.mixer.Sound('./assets/SELECT.wav').play()
            ent2.health = 0
            ent1.score += 11
            return

        elif isinstance(ent2, Player) and isinstance(ent1, Boost) and ent1.name == 'boost4':
            ent2.boost_invincible_timer = 60 * 5
            ent2.boost_speed_extra = 2
            pygame.mixer.Sound('./assets/SELECT.wav').play()
            ent1.health = 0
            ent2.score += 11
            return
        
        #XP
        if isinstance(ent1, Player) and isinstance(ent2, Boost) and ent2.name == 'boost1':
            pygame.mixer.Sound('./assets/Sound_xp.wav').play()
            ent1.score += 200
            ent2.health = 0
            return
        elif isinstance(ent2, Player) and isinstance(ent1, Boost) and ent1.name == 'boost1':
            pygame.mixer.Sound('./assets/Sound_xp.wav').play()
            ent2.score += 200
            ent1.health = 0
            return