#https://github.com/EcoSimulator/EcoSim/blob/d973d8344c23158c6c76d2a7b26a83d429106b85/Sprites/Sprite.py#L33


 #Can only parse string thru, get around : parse string , each class type handle rest (i.e: spritesheet())
import pygame
from pygame.locals import *
from sheet_to_sprite import spritesheet
from pygame_starter import Game

class sprite_library(pygame.sprite.Sprite,object):
    def __init__(self):
        super().__init__()
        
        # Loading directories [spritesheet]
        """ Players """
        self.p1 = "assets/p1.png"
        self.p2 = "assets/p2.png"
        self.p1_projectile = "assets/projectile.png"
        self.enemy_jelly = "assets/jellyfish.png"
        self.pwr_up = "assets/pwr_up.png"
       
       
        # Loading directories [full img]
        """ Players """
        p1_sheet = pygame.image.load("assets/p1.png")
        p2_sheet = pygame.image.load("assets/p2.png")
        p1_projectile_sheet = pygame.image.load("assets/projectile.png")
        enemy_jelly_sheet = pygame.image.load("assets/jellyfish.png")
        pwr_up_sheet = pygame.image.load("assets/pwr_up.png")
        
        self.sprite_dir_full_lib = [p1_sheet,p2_sheet,p1_projectile_sheet,enemy_jelly_sheet,pwr_up_sheet]
        
        # Loading directories [spritesheet]
        global p1,p2,p1_projectile,enemy_jelly
        p1 = sprite_library.Sprite(self,'p1',self.p1)
        p2 = sprite_library.Sprite(self,'p2',self.p2)
        p1_projectile = sprite_library.Sprite(self,'p1_projectile',self.p1_projectile)
        enemy_jelly = sprite_library.Sprite(self,'enemy_jelly',self.enemy_jelly)
        pwr_up = sprite_library.Sprite(self,'pwr_up',self.pwr_up)
        
        self.sprite_dir_sheet_lib = [p1,p2,p1_projectile,enemy_jelly,pwr_up]
                
        # Defines
        """ Setting Starting Animation Frame """
        p1_animation_frame , p2_animation_frame , p1_projectile_animation_frame = 0 , 0 , 0
        
        enemy_jelly_animation_frame = 0
        pwr_up_animation_frame = 0
        
        self.sprite_animation_frame_lib = [p1_animation_frame , p2_animation_frame , p1_projectile_animation_frame,enemy_jelly_animation_frame,pwr_up_animation_frame]
        

        """ For Automatic Sprite Loader """
        coords = []
        self.coord_x , self.coord_y = 0 , 0
        rowcounter = 1


        # Sprites Config
        """ Default Sprite Size """
        df_p1_sprite_size = [39 , 57]  
        df_p2_sprite_size = [39 , 57]        
        df_p1_projectile_sprite_size = [39,57]
        df_enemy_jelly_sprite_size = [93,138]
        df_pwr_up_sprite_size = [75,76]
        
        self.df_sprite_size_lib = [df_p1_sprite_size,df_p2_sprite_size,df_p1_projectile_sprite_size,df_enemy_jelly_sprite_size,df_pwr_up_sprite_size]


            # Refactoring out - complied into def
        """ Width of SpriteSheet """
        p1_img_x = self.sprite_dir_full_lib[0].get_height()
        p2_img_x = self.sprite_dir_full_lib[1].get_height()
        p1_projectile_img_x = self.sprite_dir_full_lib[2].get_height()
        enemy_jelly_img_x = self.sprite_dir_full_lib[3].get_height()
        pwr_up_img_x = self.sprite_dir_full_lib[4].get_height()

        self.sprite_height_lib = [p1_img_x,p2_img_x,p1_projectile_img_x,enemy_jelly_img_x,pwr_up_img_x]

        """ Sprites Per Sheet """
        df_p1_num = 18 
        df_p2_num = 5
        df_p1_projectile_num = 1
        df_enemy_jelly_num = 1
        df_pwr_up_num = 1

        self.sprite_total_frame_lib = [df_p1_num,df_p2_num,df_p1_projectile_num,df_enemy_jelly_num,df_pwr_up_num]

        """ Initilisation Coordinates """
        p1_coord = [695,500]
        p2_coord = [725,500]
        p1_projectile_coord = [p1_coord[0] , p1_coord[1] + 20]
        enemy_jelly_coord = [700,10]
        pwr_up_coord = [0,0]
        
        self.sprite_coord_lib = [p1_coord,p2_coord,p1_projectile_coord,enemy_jelly_coord,pwr_up_coord]


        """ SpriteSheet Indexes """        
        I_p1 = 'p1_sprites'
        I_p2 = 'p2_sprites'
        I_p1_pro = 'p1_projectile_sprites'
        I_en_j = 'enemy_jelly_sprites'
        I_pwr = 'pwr_up_sprites'


        # Automatic SpriteLoader
        self.p1_sprites = p1.images_at(self.AutoSprite(I_p1))
        self.p2_sprites = p2.images_at(self.AutoSprite(I_p2))

        self.p1_projectile_sprites = p1_projectile.images_at(self.AutoSprite(I_p1_pro))
        
        self.enemy_jelly_sprites = enemy_jelly.images_at(self.AutoSprite(I_en_j))

        print(self.p1_sprites)

    def Sprite(self,container,target):
        globals()[container] = []
        globals()[container] = spritesheet(target)
        return globals()[container]
        
    def AutoSprite(self,target):
        # Reset sprite coords for each executions 
        self.coord_x = 0
        self.coord_y = 0

        # setting params based on provided target
        if target == 'p1_sprites':
            sprite_index = 0
            
        elif target == 'p2_sprites':
            sprite_index = 1
        
        elif target == 'p1_projectile_sprites':   
            sprite_index = 2
            
        elif target == 'enemy_jelly_sprites':
            sprite_index = 3
            
        elif target == 'pwr_up_sprites':
            sprite_index = 4
            
            
        sheet_size = self.sprite_height_lib[sprite_index]
        sprite_count = self.sprite_total_frame_lib[sprite_index]
        sprite_size = self.df_sprite_size_lib[sprite_index]

        # Creating list and appending initial coords of sprites
        name = target + '_coords'
        globals()[name] = []
        globals()[name].append(( self.coord_x , self.coord_y , sprite_size[0] , sprite_size[1] )) # append 0,0 of sheet

        
        while len(globals()[name]) <= sprite_count-1: # incremental
            """ x increment """
            if (self.coord_x+ sprite_size[0] < sheet_size):
                self.coord_x = self.coord_x + sprite_size[0]
            else :
                self.coord_x = 0
                """ y incremental """
                self.coord_y = self.coord_y + sprite_size[1]
                
            globals()[name].append(( self.coord_x , self.coord_y  , sprite_size[0] , sprite_size[1] ))
        return  globals()[name]

    
class Player_1(sprite_library):
    def __init__(self):
        super().__init__()
        self.index = 0
       
        print('player 1 :',p1)
        # obtain predefined params
        self.sprite = self.sprite_dir_sheet_lib[self.index]
        self.sheet = self.sprite_dir_full_lib[self.index]
        self.frames = self.sprite_animation_frame_lib[self.index]
        self.sprite_size = self.df_sprite_size_lib[self.index]
        self.sprite_max_frame = self.sprite_total_frame_lib[self.index]
        sprite_coord = self.sprite_coord_lib[self.index]
        self.entity_x = sprite_coord[0]
        
        self.entity_y = sprite_coord[1]
        
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
        
       
    def Fire(self):
        print('pew')
        p1_sprite = pygame.transform.scale(self.p1_sprites[self.key_frames['fire start']],(45.5,66.5))
        self.sprite_animation_frame_lib[self.index] = self.key_frames['fire start']
        
        return p1_sprite
        
    def GetCoords(self):
        coords = [self.entity_x,self.entity_y]
        print('coord:' , coords)
        return coords
        
    def Update(self,coords):
        # Handling initilization
        print(self.frames,len(self.p1_sprites))
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
        

        


        

        
