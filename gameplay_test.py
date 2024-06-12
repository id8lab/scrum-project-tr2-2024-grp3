import pygame
from sheet_to_sprite import spritesheet
from pygame_starter import Game
    
class MyGame(Game):
    def __init__(self):
        super().__init__()
        # directories
        sheet2sprite = spritesheet("assets/player_sprite.png")

        # load background
        self.background = pygame.image.load("assets/bg.jpg").convert()
        self.bg_width = self.background.get_width()
        self.bg_height = self.background.get_height()

        # defining spritesheets
        self.image = sheet2sprite.image_at((0,0,39,57))
        images = []
        self.images = sheet2sprite.images_at(((0,0,39,57),(40,0,39,57),(0,58,39,57),(40,58,39,57)))
        # , colorkey=(255,255,255)

        # Initialize background positions
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height
        self.bg_scroll_speed = 5  # Adjust scroll speed as needed
        
    def game(self):
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
        
        
        # red highlight
        red1 = self.images[1]    
        self.screen.blit(
            red1,
            (
                self.screen_size[0]  - red1.get_size()[0],
                self.screen_size[1]  - red1.get_size()[1],
            ),
        )
        # red none
        red0 = self.images[0]
        self.screen.blit(
            self.images[0],
            (
                self.screen_size[0] / 2 - red0.get_size()[0],
                self.screen_size[1] / 2 - red0.get_size()[1],
            ),
        )
        # blue none
        blue0 = self.images[2]
        self.screen.blit(
            self.images[2],
            (
                self.screen_size[0]  - blue0.get_size()[0],
                self.screen_size[1]/2  - blue0.get_size()[1],
            ),
        )

        #blue highlight
        blue1 = self.images[3]
        self.screen.blit(
            self.images[3],
            (
                self.screen_size[0] / 2 - blue1.get_size()[0],
                self.screen_size[1]  - blue1.get_size()[1],
            ),
        )


if __name__ == "__main__":
    game = MyGame()
    game.run()
