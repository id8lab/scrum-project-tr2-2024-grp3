from SpriteLibrary import sprite_library
import pygame
from pygame.locals import *
from sheet_to_sprite import spritesheet
from pygame_starter import Game

class Player(sprite_library,pygame.sprite.Sprite):
    def __init__(self,player_number):
        super().__init__()
        """ Audio """
        audio_path = 'assets\\audio\\'
        #pygame.init()
        #pygame.mixer.pre_init(frequency=24455, size = -12 , channels = 2 , allowedchanges=0)

        self.player_number = player_number
        self.key_frames = {}
        """ Player specfic defines """
        if self.player_number == 1:
            #self.audio_shoot = pygame.mixer.Sound(audio_path+'player_shoot_1.mp3')
            #self.audio_death = pygame.mixer.Sound(audio_path+'player_death_1.mp3')
            
            self.sprite_index = 0
            self.type_index = 0
            
            self.proj_sprite_index = 2
            self.proj_type_index = 2
            
            rest_num , rest_l  = 5,5
            fire_num , fire_l  = 1,6
            shield_num , shield_l  = 4,10
            dead_num , dead_l   = 8,18 
              
        if self.player_number == 2:
            #self.audio_shoot = pygame.mixer.Sound(audio_path+'player_shoot_2.mp3')
            #self.audio_death = pygame.mixer.Sound(audio_path+'player_death_2.mp3')
            
            self.sprite_index = 1
            self.type_index = 0
            
            self.proj_sprite_index = 2
            self.proj_type_index = 2
            
            rest_num , rest_l  = 5,5
            fire_num , fire_l  = 1,6
            shield_num , shield_l  = 4,10
            dead_num , dead_l   = 8,18 
            
            
            
        rest_s = rest_l-rest_num
        fire_s = fire_l-fire_num
        shield_s = shield_l-shield_num
        dead_s = dead_l-dead_num
        self.key_frames.update({'rest start':rest_s ,'rest end':rest_l-1 , 'fire start':fire_s , 'fire end':fire_l-1 , 'shield start':shield_s,'shield end': shield_l-1 , 'dead start':dead_s , 'dead end': dead_l-1 })
        
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
        
        # Player specfic variables
        self.life = 3
        self.player_hitbox = (self.entity_x , self.entity_y, 45.5 , 66.5)
        self.projectile_hitbox = (self.projectile_x+17 , self.projectile_y, 5,57)
        
    def Life(self):
        return self.life
   
    def audio(self,action):
        if action == 'fire':
            return self.audio_shoot
        
    def Fire(self,coords):
        if self.player_number == 1:
            
            sprite = self.projectile_sprites[0]
        if self.player_number == 2:
            sprite = self.projectile_sprites[1]
        return sprite 
    
    def PlayerHitbox(self,entity_x,entity_y):
        self.player_hitbox = (entity_x , entity_y, 45.5 , 66.5)
        return self.player_hitbox
        
    def ProjectileHitbox(self,entity_x,entity_y):
        self.projectile_hitbox = pygame.Rect(entity_x+16 , entity_y+3, 8 , 50.5)
        return self.projectile_hitbox
        
    def hitbox(self):
        self.projectile_hb = pygame.Rect(self.projectile_x+17 , self.projectile_y, 5,57)
        return self.projectile_hb
        
    def Projectile_hit(self,hb):
        if pygame.Rect.colliderect():
            1+1
            
    def GetCoords(self):
        coords = [self.entity_x,self.entity_y]
        return coords
        
    def GetProjectile(self):
        coords = [self.projectile_x,self.projectile_y]
        return coords
        
    def Update(self):
        # Handling initilization
        try:
            if self.frames + 1 >= self.key_frames['rest end']:
                self.frames = 0
        except NameError:
            self.frames = 0

        # Scaling up sprite
        if self.player_number == 1:
            sprite = pygame.transform.scale(self.p1_sprites[self.frames],(45.5,66.5))
        if self.player_number == 2:
            sprite = pygame.transform.scale(self.p2_sprites[self.frames],(45.5,66.5))
        #win.blit(p1_sprite,(self.entity_x,self.entity_y))
        self.frames += 1

        # Update libraries
        self.sprite_animation_frame_lib[self.type_index][self.sprite_index] = self.frames
        self.sprite_coord_lib[self.type_index][self.sprite_index] = [self.entity_x,self.entity_y]
        
        
        test = self.sprite_coord_lib[self.type_index][self.sprite_index]
        
        return sprite 
        
    def LifeUpdate(self,increments):
        # checking current life
        current = self.life
        final = current + increments
        
        if self.player_number == 1:
            life_sprite = self.hud_life_sprites[0]
        if self.player_number == 2:
            life_sprite = self.hud_life_sprites[1]
        #life_sprite = pygame.transform.scale(life_sprite,(45.5,66.5))            
        
        self.life = final
        
        return life_sprite




