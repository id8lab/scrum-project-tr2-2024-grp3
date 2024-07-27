from SpriteLibrary import sprite_library
import pygame
from pygame.locals import *
from sheet_to_sprite import spritesheet
from pygame_starter import Game

class PWR_UP(sprite_library):
    def __init__(self):
        super().__init__()
        self.index = 4
        
        # Obtaining predefined params
        self.sprite = self.sprite_dir_sheet_lib[self.index]
        self.sheet = self.sprite_dir_full_lib[self.index]
        self.frames = self.sprite_animation_frame_lib[self.index]
        self.sprite_size = self.df_sprite_size_selib[self.index]
        self.sprite_max_frame = self.sprite_total_frame_lib[self.index]
        sprite_coord = self.sprite_coord_lib[self.index]
        self.entity_x = sprite_coord[0]
        self.entity_y = sprite_coord[1]
        
        # Key Frames _________
        self.pwr_up_lib = {}
        
        shield = 0
        damage = 1
        speed = 2
        life = 3
        ammo = 4
        
        self.pwr_up_lib.update({'shield':shield , 'damage':damage , 'speed':speed , 'life':life , 'ammo':ammo})