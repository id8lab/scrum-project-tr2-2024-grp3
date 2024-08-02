from random import randint,uniform
from SpriteLibrary import sprite_library
from AudioLibrary import audio_library
import pygame
import time

al = audio_library()
class enemy(sprite_library , pygame.sprite.Sprite):
    def __init__(self,entity_x,entity_y,enemy_type):
        super().__init__()
        
        # General Enemies Default
        self.entity_x = entity_x
        self.entity_y = entity_y
        self.enemy_type = enemy_type
        self.counter = 1
        self.entity_id = self.counter
        
        # Jellyfish Default
        if enemy_type == 'jellyfish':
            self.image = self.enemy_jelly_sprites[0]
            self.rect  = [entity_x,entity_y]
            
            self.health = 1
            self.entity_hitbox = (self.entity_x , self.entity_y, 93 , 138)
            self.scalar = 10
            self.cntr = randint(0,49)
            
            # Audio defaults
            self.audio_death = al.audio_death(enemy_type)
            
            # Creating X-axis patrol direction and scalar
            if entity_x <= 632:                 # entity on left
                self.patrol_direction = 'right'
                patrol_x = randint(150 , 725)
                while (patrol_x + entity_x) > (1450 - self.df_sprite_size_lib[1][0][0]):
                    patrol_x = randint(150 , 725)
                
                
            elif entity_x >= 725:               # entity on right
                self.patrol_direction = 'left'
                patrol_x = randint(150, 632)
                while (entity_x - patrol_x) < (0 - self.df_sprite_size_lib[1][0][0]):
                    patrol_x = randint(150 , 725)
                
            else:
                self.patrol_direction = 'none'
                patrol_x = entity_x
            self.distance_to_endpt = patrol_x
            
            self.patrol_route = {'x path':[entity_x,patrol_x] , 'y anchored':entity_y }
        
        # Ship defaults
        if enemy_type == 'ship':
            self.image = self.enemy_ship_sprites[0]
            self.rect  = [entity_x,entity_y]
            
            self.health = 1
            self.entity_hitbox = (self.entity_x , self.entity_y, 93 , 138)
            self.scalar = 10
            self.cntr = randint(0,49)
            
            # Audio defaults
            self.audio_death = al.audio_death(enemy_type)
    
    def update(self,win,player_projectiles):
        self.patrol()
        self.hitbox()
        hit_status = self.hitcheck(player_projectiles)
        
        if self.enemy_type == 'jellyfish':
            win.blit(self.enemy_jelly_sprites[0] , (self.entity_x,self.entity_y))
            pygame.draw.rect(win, (255,0,0), self.entity_hitbox,2)
            
        if self.enemy_type == 'ship':
            win.blit(self.enemy_jelly_sprites[0] , (self.entity_x,self.entity_y))
            pygame.draw.rect(win, (255,0,0), self.entity_hitbox,2)
        
        return hit_status
        
    def hitcheck(self,projectile_players):        
        for projectile_hitbox in projectile_players:
            if pygame.Rect.colliderect(self.entity_hitbox,projectile_hitbox):
                if self.health <= 0:
                    #print('kill')
                    self.audio_death.play()
                    self.kill()
                    
                else:
                    self.health -= 1
                    print('ouch')

    def hit(self):
        if self.health <= 0:
            self.kill()
            
        else:
            self.health -= 1
                    
    def hitbox(self):
        if self.enemy_type == 'jellyfish':
            self.entity_hitbox = pygame.Rect(self.entity_x , self.entity_y, self.df_sprite_size_lib[1][0][0] , self.df_sprite_size_lib[1][0][1])
        if self.enemy_type == 'ship':
            self.entity_hitbox = pygame.Rect(self.entity_x , self.entity_y, self.df_sprite_size_lib[1][1][0] , self.df_sprite_size_lib[1][1][1])
        return self.entity_hitbox
     
    def patrol(self):
        if self.enemy_type == 'jellyfish':
            # creating y axis movement
            if self.cntr <= 25:
                self.entity_y += 1
            elif (self.cntr > 25) and (self.cntr <= 50):
                self.entity_y -= 1    
            else :
                self.cntr  = 0
                
            self.cntr += 1

            if self.patrol_direction == 'left':
                
                # If entity have yet to reach end point , else take same path back
                if self.distance_to_endpt - self.scalar >= 0:  
                    self.entity_x -= self.scalar
                    self.distance_to_endpt -= self.scalar 
                else:
                    
                    self.patrol_direction = 'right'
                    self.distance_to_endpt = self.patrol_route['x path'][1] + self.scalar
                    self.entity_x += self.scalar
                    
            
            elif self.patrol_direction == 'right':
                
                # If entity have yet to reach end point , else take same path back
                if self.distance_to_endpt - self.scalar >= 0:  
                    self.entity_x += self.scalar
                    self.distance_to_endpt -= self.scalar 
                else:
                    
                    self.patrol_direction = 'left'
                    self.distance_to_endpt = self.patrol_route['x path'][1] + self.scalar
                    self.entity_x -= self.scalar 
                           
            else :
                1+1
                
        if self.enemy_type == 'ship':
            self.entity_x
        