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
        self.p1 = "assets/players/p1.png"
        self.p2 = "assets/players/p2.png"
        
        self.enemy_jelly = "assets/enemies/jellyfish.png"
        self.enemy_ship = "assets/enemies/ship.png"
        
        self.pwr_up = "assets/pwr_up.png"
        self.projectile = "assets/projectile.png"
        
        self.hud_life = "assets/hud/lifeBar.png"
        # Loading directories [full img]
        """ Players """
        p1_sheet = pygame.image.load("assets/players/p1.png")
        p2_sheet = pygame.image.load("assets/players/p2.png")
        players = (p1_sheet,p2_sheet)
        
        enemy_jelly_sheet = pygame.image.load("assets/enemies/jellyfish.png")
        enemy_ship_sheet = pygame.image.load("assets/enemies/ship.png")
        enemies = (enemy_jelly_sheet,enemy_ship_sheet)
        
        pwr_up_sheet = pygame.image.load("assets/pwr_up.png")
        projectile_sheet = pygame.image.load("assets/projectile.png")
        hud_life_sheet = pygame.image.load("assets/hud/lifeBar.png")
        misc = (pwr_up_sheet,projectile_sheet,hud_life_sheet)
        
        self.sprite_dir_full_lib = (players,enemies,misc)
        
        # Loading directories [spritesheet]
        global p1,p2,p1_projectile,enemy_jelly,enemy_ship,pwr_up,hud_life
        
        p1 = sprite_library.Sprite(self,'p1',self.p1)
        p2 = sprite_library.Sprite(self,'p2',self.p2)
        players = (p1,p2)
        
        
        enemy_jelly = sprite_library.Sprite(self,'enemy_jelly',self.enemy_jelly)
        enemy_ship = sprite_library.Sprite(self,'enemy_ship',self.enemy_ship)
        enemies = (enemy_jelly,enemy_ship)
        
        pwr_up = sprite_library.Sprite(self,'pwr_up',self.pwr_up)
        hud_life = sprite_library.Sprite(self,'hud_life',self.hud_life)
        projectile = sprite_library.Sprite(self,'projectile',self.projectile)
        misc = (pwr_up,hud_life,projectile)
        
        
        self.sprite_dir_sheet_lib = (players,enemies,misc)
                
        # Defines
        """ Setting Starting Animation Frame """
        p1_animation_frame , p2_animation_frame ,  = 0 , 0 
        players = [p1_animation_frame,p2_animation_frame]
        
        enemy_jelly_animation_frame = 0
        enemy_ship_animation_frame = 0
        enemies = [enemy_jelly_animation_frame,enemy_ship_animation_frame]
        
        pwr_up_animation_frame = 0
        projectile_animation_frame = 0
        hud_life_animation_frame = 0
        misc = [pwr_up_animation_frame,projectile_animation_frame,hud_life_animation_frame]
        
        self.sprite_animation_frame_lib = [players,enemies,misc]
        

        """ For Automatic Sprite Loader """
        coords = []
        self.coord_x , self.coord_y = 0 , 0
        rowcounter = 1


        # Sprites Config
        """ Default Sprite Size """
        df_p1_sprite_size = [39 , 57]  
        df_p2_sprite_size = [39 , 57] 
        players = (df_p1_sprite_size,df_p2_sprite_size)
            
        
        df_enemy_jelly_sprite_size = [93,138]
        df_enemy_ship_sprite_size = [125,149]
        enemies = (df_enemy_jelly_sprite_size,df_enemy_ship_sprite_size)
        
        df_pwr_up_sprite_size = [75,76]
        df_hud_life_sprite_size = [15,45]
        df_projectile_sprite_size = [39,57]
        misc = (df_pwr_up_sprite_size,df_hud_life_sprite_size,df_projectile_sprite_size)
        
        self.df_sprite_size_lib = (players,enemies,misc)

        
            
        """ Width of SpriteSheet """
        p1_img_x = self.sprite_dir_full_lib[0][0].get_height()
        p2_img_x = self.sprite_dir_full_lib[0][1].get_height()
        players = (p1_img_x,p2_img_x)
        
        enemy_jelly_img_x = self.sprite_dir_full_lib[1][0].get_height()
        enemy_ship_img_x = self.sprite_dir_full_lib[1][1].get_height()
        enemies = (enemy_jelly_img_x,enemy_ship_img_x)
        
        pwr_up_img_x = self.sprite_dir_full_lib[2][0].get_height()
        hud_life_img_x = self.sprite_dir_full_lib[2][1].get_height()
        projectile_img_x = self.sprite_dir_full_lib[2][2].get_height()
        misc = (pwr_up_img_x,hud_life_img_x,projectile_img_x)

        self.sprite_height_lib = (players,enemies,misc)

        """ Sprites Per Sheet """
        df_p1_num = 18 
        df_p2_num = 18
        players = (df_p1_num,df_p2_num)
        
        df_enemy_jelly_num = 2
        df_enemy_ship_num = 9
        enemies = (df_enemy_jelly_num,df_enemy_ship_num)
        
        df_pwr_up_num = 5
        df_hud_life_num = 4
        df_projectile_num = 4
        misc = (df_pwr_up_num,df_hud_life_num,df_projectile_num)

        self.sprite_total_frame_lib = (players,enemies,misc)

        """ Initilisation Coordinates """
        p1_coord = [695,500]
        p2_coord = [725,500]
        players = [p1_coord,p2_coord]
        
        enemy_jelly_coord = [700,10]
        enemy_ship_coord = [350,30]
        enemies = [enemy_jelly_coord,enemy_ship_coord]
        
        pwr_up_coord = [1450,-15]
        hud_life_coord = [[15,690],[1420,690],[25,15],[35,15]]
        projectile_coord = [[0 , -50],[0,-50]]
        misc = [pwr_up_coord,hud_life_coord,projectile_coord]
        
        self.sprite_coord_lib = [players,enemies,misc]

        """ SpriteSheet Indexes """        
        I_p1 = 'p1_sprites'
        I_p2 = 'p2_sprites' 
        
        I_en_j = 'enemy_jelly_sprites'
        I_en_s = 'enemy_ship_sprites'
        
        I_pwr = 'pwr_up_sprites'
        I_hud_life = 'hud_life_sprites'
        I_pro = 'projectile_sprites'

        # Automatic SpriteLoader
        self.p1_sprites = p1.images_at(self.AutoSprite(I_p1))
        self.p2_sprites = p2.images_at(self.AutoSprite(I_p2))
        
        self.enemy_jelly_sprites = enemy_jelly.images_at(self.AutoSprite(I_en_j))
        self.enemy_ship_sprites = enemy_jelly.images_at(self.AutoSprite(I_en_s))
        
        self.hud_life_sprites = hud_life.images_at(self.AutoSprite(I_hud_life))
        self.projectile_sprites = projectile.images_at(self.AutoSprite(I_pro))
        
    def Hud_Life_Coord(self):
        return self.sprite_coord_lib[2][1]
    
    def Sprite(self,container,target):
        globals()[container] = []
        globals()[container] = spritesheet(target)
        return globals()[container]
    
    def GetEnemySprite(self):
        return self.enemy_jelly_sprites,self.enemy_ship_sprites
    
    def AutoSprite(self,target):
        # Reset sprite coords for each executions 
        self.coord_x = 0
        self.coord_y = 0

        # setting params based on provided target
        if target == 'p1_sprites':
            type_index = 0
            sprite_index = 0
            
        elif target == 'p2_sprites':
            type_index = 0
            sprite_index = 1
            
            
        elif target == 'enemy_jelly_sprites':
            type_index = 1
            sprite_index = 0
            
        elif target == 'enemy_ship_sprites':
            type_index = 1
            sprite_index = 1
            
            
        elif target == 'pwr_up_sprites':
            type_index = 2
            sprite_index = 0
        
        elif target == 'hud_life_sprites':
            type_index = 2
            sprite_index = 1
            
        elif target == 'projectile_sprites':  
            type_index = 2        
            sprite_index = 2    
            
        sheet_size = self.sprite_height_lib[type_index][sprite_index]
        sprite_count = self.sprite_total_frame_lib[type_index][sprite_index]
        sprite_size = self.df_sprite_size_lib[type_index][sprite_index]

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

 