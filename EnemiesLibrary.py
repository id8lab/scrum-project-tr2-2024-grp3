from SpriteLibrary import sprite_library
import pygame
from pygame.locals import *
from sheet_to_sprite import spritesheet
from pygame_starter import Game

class Jellyfish(sprite_library):
    def __init__(self):
        super().__init__()
        self.sprite_index = 0
        self.type_index = 1
        
        self.proj_sprite_index = 2
        self.proj_type_index = 2
       
        # obtain predefined params
        self.sprite = self.sprite_dir_sheet_lib[self.type_index][self.sprite_index]
        self.sheet = self.sprite_dir_full_lib[self.type_index][self.sprite_index]
        self.frames = self.sprite_animation_frame_lib[self.type_index][self.sprite_index]
        self.sprite_size = self.df_sprite_size_lib[self.type_index][self.sprite_index]
        self.sprite_max_frame = self.sprite_total_frame_lib[self.type_index][self.sprite_index]
        sprite_coord = self.sprite_coord_lib[self.type_index][self.sprite_index]
        self.entity_x = sprite_coord[0]
        self.entity_y = sprite_coord[1]
        
        
        self.projectile_sprite = self.sprite_dir_sheet_lib[self.proj_type_index][self.proj_sprite_index]
        self.projectile_sheet = self.sprite_dir_full_lib[self.proj_type_index][self.proj_sprite_index]
        self.projectile_frames = self.sprite_animation_frame_lib[self.proj_type_index][self.proj_sprite_index]
        self.projectile_size = self.df_sprite_size_lib[self.proj_type_index][self.proj_sprite_index]
        self.projectile_max_frame = self.sprite_total_frame_lib[self.proj_type_index][self.proj_sprite_index]
        
        projectile_coord = [self.entity_x , self.entity_y+10]
        self.projectile_x = projectile_coord[0]
        self.projectile_y = projectile_coord[1]
        
        # Key Frames  ___________
        self.key_frames = {}
        #                 number of frames , last frame 
        idle  = 1 
        obstacle  = 1
        
        idle_last = 0 + idle
        idle = 0
        obstacle_last = idle_last + obstacle
        
        self.key_frames.update({'idle':idle,'obstacle':obstacle})
        
        # Enemies specfic variables
        self.health = 10
        self.enemy_hitbox = (self.entity_x , self.entity_y, 182 , 266)
    
    def Main_Hitbox(self,entity_x,entity_y):
        self.enemy_hitbox = (entity_x , entity_y, 182 , 266)
        return self.enemy_hitbox
        
    def Health(self):
        return self.health
       
    def Fire(self,coords):
        sprite = self.projectile_sprites[3]
        return sprite 
        
    def GetCoords(self):
        coords = [self.entity_x,self.entity_y]
        return coords
        
    def GetProjectile(self):
        coords = [self.projectile_x,self.projectile_y]
        return coords
        
    def Update(self):
        # Handling initilization
        try:
            if self.frames + 1 >= self.key_frames['idle']:
                self.frames = 0
        except NameError:
            self.frames = 0

        # Scaling up sprite
        jelly_sprite = pygame.transform.scale(self.enemy_jelly_sprites[self.frames],(182,266))
        #win.blit(p1_sprite,(self.entity_x,self.entity_y))
        self.frames += 1

        # Update libraries
        self.sprite_animation_frame_lib[self.type_index][self.sprite_index] = self.frames
        self.sprite_coord_lib[self.type_index][self.sprite_index] = [self.entity_x,self.entity_y]
        self.hitbox = (self.entity_x , self.entity_y, 182 , 266)
        
        
        return jelly_sprite
        
    def Hitbox(self):
        return self.hitbox
    
    def HealthUpdate(self,damage):
        # checking current life
        current = self.health
        final = current - damage 
        
        if final <= 0:
            print('dead')
            status = 'Dead'
            
        else:
            self.life = final
            status = 'Alive'
        
        return status
