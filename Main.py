from SpriteLibrary import sprite_library,Player_1
from pygame.locals import *
import pygame
from pygame_starter import Game

print('hi')
""" Setting Window's Size """
global win
win = pygame.display.set_mode((1450,750))
#sprite_library()
p1 = Player_1()


class Galaga(Game):
    def __init__(self):
        super().__init__()
        
        global win
        win = pygame.display.set_mode((1450,750))

        self.clock = pygame.time.Clock()
        
        # Load Background
        self.background = pygame.image.load("assets/bg.jpg").convert()
        self.bg_width = self.background.get_width()
        self.bg_height = self.background.get_height()
        # Initialize background positions
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height
        self.bg_scroll_speed = 5  # Adjust scroll speed as needed

        self.p1_coords = p1.GetCoords()

    def game(self):
        #self.clock.tick(128)
            
        # Back Ground 
        ''' Update background position'''
        self.bg_y1 += self.bg_scroll_speed
        self.bg_y2 += self.bg_scroll_speed

        ''' Reset background positions to create a loop effect '''
        if self.bg_y1 >= self.bg_height:
            self.bg_y1 = -self.bg_height
        if self.bg_y2 >= self.bg_height:
            self.bg_y2 = -self.bg_height

        ''' Draw the background images '''
        self.screen.blit(self.background, (0, self.bg_y1))
        self.screen.blit(self.background, (0, self.bg_y2))


        # Acquire keypress
        pygame.key.set_repeat(100,200)
        keypress = pygame.key.get_pressed()
        """Player 2 movement"""
        if keypress[K_LEFT]:
            self.p1_coords[0] = self.p1_coords[0] - 11
            print(self.p1_coords)
        if keypress[K_RIGHT]:
            self.p1_coords[0] = self.p1_coords[0] + 11
            print(self.p1_coords)
        if keypress[K_UP]:
            self.p1_coords[1] = self.p1_coords[1] - 7
            print(self.p1_coords)
        if keypress[K_DOWN]:
            self.p1_coords[1] = self.p1_coords[1] + 7
            print(self.p1_coords)
        if keypress[K_RSHIFT]:
            sprite = p1.Fire()
            win.blit(sprite,(self.p1_coords[0],self.p1_coords[1]))
            pygame.display.update
            self.clock.tick(1208)
            

        """ Player 1 movement"""
        if keypress[K_a]:
            self.p1_x -= 10
        if keypress[K_d]:
            self.p1_x += 10
        if keypress[K_w]:
            self.p1_y -= 6
        if keypress[K_s]:
            self.p1_y += 6


        # Update sprites
        print(self.p1_coords)
        sprite = p1.Update(self.p1_coords)
        win.blit(sprite,(self.p1_coords[0],self.p1_coords[1]))
        pygame.display.update

        
##        self.updateP2(self.p2_x , self.p2_y)
##        self.updateJelly(self.emy_jelly_x , self.emy_jelly_y)

if __name__ == "__main__":
    game = Galaga()
    game.run()
