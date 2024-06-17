# need to move sprite via keypress
# https://stackoverflow.com/questions/39070388/how-can-i-move-a-sprite-using-the-keyboard-with-pythons-pygame
# automate obtaining sprites > +- 0 to get local
import pygame
from pygame.locals import *
from sheet_to_sprite import spritesheet
from pygame_starter import Game

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_sprite
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vx = 0
        self.vy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.vx = -5
        elif key[pygame.K_RIGHT]:
            self.vx = 5
        if key[pygame.K_UP]:
            self.vy = -5
        elif key[pygame.K_DOWN]:
            self.vy = 5
        self.rect.x += self.vx
        self.rect.y += self.vy

    
        
class MyGame(Game):
    def __init__(self):
        super().__init__()
        # defines
        global win

        self.p2_animation_frame = 1
        win = pygame.display.set_mode((1450,750))

        # functions
        self.clock = pygame.time.Clock()
        
        # directories
        p1_idle = spritesheet("assets/p1_idle.png")
        p2_idle = spritesheet("assets/p2_idle.png")
        p2_forward = spritesheet("assets/p2_move_highlighted.png")

        # load background
        self.background = pygame.image.load("assets/bg.jpg").convert()
        self.bg_width = self.background.get_width()
        self.bg_height = self.background.get_height()

        # defining spritesheets
        global p1_idle_sprites , p2_idle_sprites , p2_forward_sprites
        """ Player 1 idle """ 
        self.p1_idle_sprite = p1_idle.image_at((0,0,39,57))
        p1_idle_sprites = []
        p1_idle_sprites = p1_idle.images_at(((0,0,39,57),(40,0,39,57)))

        """ Player 2 idle """
        p2_idle_sprites = []
        p2_idle_sprites = p2_forward.images_at(((0,0,39,57),(40,0,39,57),(0,58,39,57),(40,58,39,57)))

        """ Player 2 forward """
        p2_forward_sprites = []
        p2_forward_sprites = p2_forward.images_at(((0,0,39,57),(39,0,39,57),(78,0,39,57),(0,57,39,57),(0,114,39,57)))
        
        # Initialize background positions
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height
        self.bg_scroll_speed = 5  # Adjust scroll speed as needed

    """
    action 1 - idle
    action 2 - forward
    action 3 - left
    action 4 - right

    """
    def updateGameWindow(self):
        print(self.p2_animation_frame)
        try:
            if self.p2_animation_frame + 1 >= 5:
                self.p2_animation_frame = 1
        except NameError:
            self.p2_animation_frame = 0

        p2 = p2_forward_sprites
        print(p2)
        p2_sprite = pygame.transform.scale(p2[self.p2_animation_frame],(45.5,66.5))
        win.blit(p2_sprite,(0,0))
        self.p2_animation_frame += 1

        pygame.display.update
        
    def game(self):
        self.clock.tick(32)
            
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
        
        
##        # player 1_idle
##        self.p1 = self.p1_idle_sprites[0]
##        self.p1 = pygame.transform.scale(self.p1,(52,76))
##        win.blit(
##            self.p1,
##            (
##                self.screen_size[0]  - self.p1.get_size()[0],
##                self.screen_size[1]  - self.p1.get_size()[1],
##            ),
##        )

        # Update sprites
        self.updateGameWindow()
               


##        sprites = pygame.sprite.Group()
##        player = Player(red1)
##        sprtites.add(player)
##
##        
##        sprites.update()
##        sprites.update()
##        window_name.fill((200, 200, 200))
##        sprites.draw(window_name)
##        pygame.display.flip()
      


if __name__ == "__main__":
    game = MyGame()
    game.run()
