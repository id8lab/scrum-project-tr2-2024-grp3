from SpriteLibrary import sprite_library
import pygame
from pygame.locals import *
from sheet_to_sprite import spritesheet
from pygame_starter import Game

class Player_1(sprite_library):
    def __init__(self):
        super().__init__()
        self.index = 0
       
        # obtain predefined params
        self.sprite = self.sprite_dir_sheet_lib[self.index]
        self.sheet = self.sprite_dir_full_lib[self.index]
        self.frames = self.sprite_animation_frame_lib[self.index]
        self.sprite_size = self.df_sprite_size_lib[self.index]
        self.sprite_max_frame = self.sprite_total_frame_lib[self.index]
        sprite_coord = self.sprite_coord_lib[self.index]
        self.entity_x = sprite_coord[0]
        self.entity_y = sprite_coord[1]

        self.projectile_sprite = self.sprite_dir_sheet_lib[2]
        self.projectile_sheet = self.sprite_dir_full_lib[2]
        self.projectile_frames = self.sprite_animation_frame_lib[2]
        self.projectile_size = self.df_sprite_size_lib[2]
        self.projectile_max_frame = self.sprite_total_frame_lib[2]
        
        projectile_coord = [self.entity_x , self.entity_y+10]
        self.projectile_x = projectile_coord[0]
        self.projectile_y = projectile_coord[1]

        
        # Key Frames  ___________
        self.key_frames = {}
        #                 number of frames , last frame 
        rest_num , rest_l  = 5,5
        fire_num , fire_l  = 1,6
        shield_num , shield_l  = 4,10
        dead_num , dead_l   = 8,18 
        
        rest_s = rest_l-rest_num
        fire_s = fire_l-fire_num
        shield_s = shield_l-shield_num
        dead_s = dead_l-dead_num
        
        
        self.key_frames.update({'rest start':rest_s ,'rest end':rest_l-1 , 'fire start':fire_s , 'fire end':fire_l-1 , 'shield start':shield_s,'shield end': shield_l-1 , 'dead start':dead_s , 'dead end': dead_l-1 })
        

    def Fire(self,coords):
        sprite = self.projectile_sprites[0]
        return sprite 
        
    def GetCoords(self):
        coords = [self.entity_x,self.entity_y]
        print('e coord:' , coords)
        return coords
        
    def GetProjectile(self):
        coords = [self.projectile_x,self.projectile_y]
        print('p coord:' , coords)
        return coords
        
    def Update(self):
        # Handling initilization

        try:
            if self.frames + 1 >= self.key_frames['rest end']:
                self.frames = 0
        except NameError:
            self.frames = 0

        # Scaling up sprite
        
        p1_sprite = pygame.transform.scale(self.p1_sprites[self.frames],(45.5,66.5))
        #win.blit(p1_sprite,(self.entity_x,self.entity_y))
        self.frames += 1

        # Update libraries
        self.sprite_animation_frame_lib[self.index] = self.frames
        self.sprite_coord_lib[self.index] = [self.entity_x,self.entity_y]
        
        return p1_sprite
        #pygame.display.update
        

class Player_2(sprite_library):
    def __init__(self):
        super().__init__()
        self.index = 1
      
        # obtain predefined params
        self.sprite = self.sprite_dir_sheet_lib[self.index]
        self.sheet = self.sprite_dir_full_lib[self.index]
        self.frames = self.sprite_animation_frame_lib[self.index]
        self.sprite_size = self.df_sprite_size_lib[self.index]
        self.sprite_max_frame = self.sprite_total_frame_lib[self.index]
        sprite_coord = self.sprite_coord_lib[self.index]
        self.entity_x = sprite_coord[0]

        self.entity_y = sprite_coord[1]
        
        self.projectile_sprite = self.sprite_dir_sheet_lib[2]
        self.projectile_sheet = self.sprite_dir_full_lib[2]
        self.projectile_frames = self.sprite_animation_frame_lib[2]
        self.projectile_size = self.df_sprite_size_lib[2]
        self.projectile_max_frame = self.sprite_total_frame_lib[2]
        
        projectile_coord = [self.entity_x , self.entity_y+10]
        self.projectile_x = projectile_coord[0]
        self.projectile_y = projectile_coord[1]

        
        # Key Frames  ___________
        self.key_frames = {}
        #                 number of frames , last frame 
        rest_num , rest_l  = 5,5
        fire_num , fire_l  = 1,6
        shield_num , shield_l  = 5,11
        dead_num , dead_l   = 7,18 
        
        rest_s = rest_l-rest_num
        fire_s = fire_l-fire_num
        shield_s = shield_l-shield_num
        dead_s = dead_l-dead_num
        
        
        self.key_frames.update({'rest start':rest_s ,'rest end':rest_l-1 , 'fire start':fire_s , 'fire end':fire_l-1 , 'shield start':shield_s,'shield end': shield_l-1 , 'dead start':dead_s , 'dead end': dead_l-1 })
        
    def Fire(self,coords):
        sprite = self.projectile_sprites[1]
        return sprite 

        
    def GetCoords(self):
        coords = [self.entity_x,self.entity_y]
        return coords

    def GetProjectile(self):
        coords = [self.projectile_x,self.projectile_y]
        print('p coord:' , coords)
        return coords  
        
    def Update(self):
        # Handling initilization

        try:
            if self.frames + 1 >= self.key_frames['rest end']:
                self.frames = 0
        except NameError:
            self.frames = 0

        # Scaling up sprite
        
        p2_sprite = pygame.transform.scale(self.p2_sprites[self.frames],(45.5,66.5))
        #win.blit(p1_sprite,(self.entity_x,self.entity_y))
        self.frames += 1

        # Update libraries
        self.sprite_animation_frame_lib[self.index] = self.frames
        self.sprite_coord_lib[self.index] = [self.entity_x,self.entity_y]
        
        
        
        return p2_sprite
        #pygame.display.update        
