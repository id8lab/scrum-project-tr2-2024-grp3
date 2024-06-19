# need to move sprite via keypress
# https://stackoverflow.com/questions/39070388/how-can-i-move-a-sprite-using-the-keyboard-with-pythons-pygame

import pygame
from pygame.locals import *
from sheet_to_sprite import spritesheet
from pygame_starter import Game
    
        
class MyGame(Game):
    def __init__(self):
        super().__init__()
        # directories
        p1_idle = spritesheet("assets/p1_idle.png")
        p2_idle = spritesheet("assets/p2_idle.png")
        p2_forward = spritesheet("assets/p2_move_highlighted.png")

        test = pygame.image.load("assets/p2_move_highlighted.png")
        
        # defines
        global win , p1_idle_sprites , p2_idle_sprites , p2_forward_sprites , p1_idle_x
        self.p2_animation_frame = 1
        win = pygame.display.set_mode((1450,750))

        coords = []
        self.coord_x , self.coord_y = 0,0
        img_x , img_y = 0,0
        rowct = 1
        
        # sprite defines
        self.df_sprite_size = [39 , 57] #default size of sprites
        
        self.img_x = test.get_width()
        self.img_y = test.get_height()

        """sprites per sheets"""
        df_p1_idle_num = 2 
        df_p2_idle_num = 2

        df_p1_fwd_num = 5
        self.df_p2_fwd_num = 5

        """ sprites characteristics """
        self.p2_x , self.p2_y = 725,500
        # Animation indexs
        p1_i = 'p1_idle_sprites'
        p1_a = 'p1_atk_sprites'
        p1_fw = 'p2_fwd_sprites'

        p2_i = 'p2_idle_sprites'
        p2_a = 'p2_atk_sprites'
        p2_fw = 'p2_fwd_sprites'
        
        # functions
        self.clock = pygame.time.Clock()
        
        # load background
        self.background = pygame.image.load("assets/bg.jpg").convert()
        self.bg_width = self.background.get_width()
        self.bg_height = self.background.get_height()

        # defining spritesheets
        """ usage :
        [individual sprites] = [sheet directory].images_at(self.automaticSprites([animation_index]))"""
        self.p2_fwd_sprites = p2_forward.images_at(self.automaticSprites(p2_fw))
        self.p1_idle_sprites = p1_idle.images_at(self.automaticSprites(p1_i))
        
        # Initialize background positions
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height
        self.bg_scroll_speed = 5  # Adjust scroll speed as needed

    def automaticSprites(self,target):
        name = target+'_coords'
        globals()[name] = []
        globals()[name].append(( self.coord_x , self.coord_y , self.df_sprite_size[0] , self.df_sprite_size[1] )) # append 0,0

        while len(globals()[name]) <= self.df_p2_fwd_num-1: # incremental
            """ x increment """
            if (self.coord_x+ self.df_sprite_size[0] < self.img_x):
                self.coord_x = self.coord_x + self.df_sprite_size[0]
            else :
                self.coord_x = 0
                """ y incremental """
                self.coord_y = self.coord_y + self.df_sprite_size[1]
                
            globals()[name].append(( self.coord_x , self.coord_y  , self.df_sprite_size[0] , self.df_sprite_size[1] ))
        return  globals()[name]
            
    def updateGameWindow(self,pl_x,pl_y):
        curr_x = pl_x
        curr_y = pl_y
        
        try:
            if self.p2_animation_frame + 1 >= 5:
                self.p2_animation_frame = 1
        except NameError:
            self.p2_animation_frame = 0

        p2 = self.p2_fwd_sprites
        
        p2_sprite = pygame.transform.scale(p2[self.p2_animation_frame],(45.5,66.5))
        win.blit(p2_sprite,(curr_x,curr_y))
        self.p2_animation_frame += 1

        pygame.display.update
        
    def game(self):
        self.clock.tick(64)
            
        """ Back Ground """
        # Update background positions
        self.bg_y1 += self.bg_scroll_speed
        self.bg_y2 += self.bg_scroll_speed

        # Reset background positions to create a loop effect
        if self.bg_y1 >= self.bg_height:
            self.bg_y1 = -self.bg_height
        if self.bg_y2 >= self.bg_height:
            self.bg_y2 = -self.bg_height

        # Draw the background images
        self.screen.blit(self.background, (0, self.bg_y1))
        self.screen.blit(self.background, (0, self.bg_y2))
        
        pygame.key.set_repeat(100,200)
        keypress = pygame.key.get_pressed()
        if keypress[K_LEFT]:
            self.p2_x -= 10
        if keypress[K_RIGHT]:
            self.p2_x += 10
        if keypress[K_UP]:
            self.p2_y -= 5
        if keypress[K_DOWN]:
            self.p2_y += 5

        # Update sprites
        self.updateGameWindow(self.p2_x , self.p2_y)
      


if __name__ == "__main__":
    game = MyGame()
    game.run()
