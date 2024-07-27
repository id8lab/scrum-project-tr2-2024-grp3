from random import randint,uniform
from SpriteLibrary import sprite_library
import pygame
import time

class enemy(sprite_library,pygame.sprite.Sprite):
    def __init__(self,entity_x,entity_y,enemy_type):
        super().__init__()
        # self.total_enemies = []
        # self.current_enemies = pygame.sprite.Group()       
        
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
            
            
            
            self.entity_hitbox = (self.entity_x , self.entity_y, 93 , 138)
            self.scalar = 10
            self.cntr = randint(0,49)
            # Creating X-axis patrol direction and scalar
            if entity_x <= 632:                 # entity on left
                self.patrol_direction = 'right'
                patrol_x = randint(150 , 725)
                
                
            elif entity_x >= 725:               # entity on right
                self.patrol_direction = 'left'
                patrol_x = randint(150, 632)
                
            else:
                self.patrol_direction = 'none'
                patrol_x = entity_x
        
        self.distance_to_endpt = patrol_x
        
        # If patrol route too small , make stationary
        if ( abs(patrol_x-entity_x) <=  200) :
            patrol_x = entity_x
            self.patrol_direction = 'none'
                
           
            
        self.patrol_route = {'x path':[entity_x,patrol_x] , 'y anchored':entity_y }        
        
        print('patrol :',patrol_x,'entity :',entity_x)
        print('vector :',self.patrol_direction)
        print('distance :',self.distance_to_endpt)
    
    def update(self,win,player_projectiles):
        self.patrol()
        self.hitbox()
        self.hittemp(player_projectiles)
        
        if self.enemy_type == 'jellyfish':
            win.blit(self.enemy_jelly_sprites[0] , (self.entity_x,self.entity_y))
            pygame.draw.rect(win, (255,0,0), self.entity_hitbox,2)
        
    def hittemp(self,projectile_players):        
        for projectile_hitbox in projectile_players:
            if pygame.Rect.colliderect(self.entity_hitbox,projectile_hitbox):
                self.kill()
          

        
    def hitbox(self):
        if self.enemy_type == 'jellyfish':
            self.entity_hitbox = pygame.Rect(self.entity_x , self.entity_y, 93 , 138)
            return self.entity_hitbox
    
    def hit(self):
        print('killed')
        self.entity_x , self.entity_x = -100,-100
        self.patrol_direction = 'none'
        self.kill()
        
    # def draw(self,win):
        # self.patrol()
        # self.hitbox()
        
        # if self.enemy_type == 'jellyfish':
            
            # win.blit(self.enemy_jelly_sprites[0] , (self.entity_x,self.entity_y))
            # pygame.draw.rect(win, (255,0,0), self.entity_hitbox,2)
     
    def patrol(self):
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
            if self.distance_to_endpt + self.scalar >= 0:  
                self.entity_x += self.scalar
                self.distance_to_endpt -= self.scalar 
            else:
                self.patrol_direction = 'left'
                self.distance_to_endpt = self.patrol_route['x path'][1] - self.scalar
                self.entity_x -= self.scalar        
        else :
            1+1

        