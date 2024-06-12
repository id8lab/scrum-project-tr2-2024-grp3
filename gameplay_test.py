import pygame
from pygame_starter import Game

class MyGame(Game):
    def __init__(self):
        super().__init__()
        # Load the background image
        self.background = pygame.image.load("assets/bg_h.png").convert()
        # Load the player sprite image
        self.img = pygame.image.load("assets/player_sprites.png").convert_alpha()

    def game(self):
        # Draw the background image
        self.screen.blit(self.background, (0, 0))
        # Draw the player sprite in the middle of the screen
        self.screen.blit(
            self.img,
            (
                self.screen_size[0] / 2 - self.img.get_size()[0] / 2,
                self.screen_size[1] / 2 - self.img.get_size()[1] / 2,
            ),
        )

if __name__ == "__main__":
    game = MyGame()
    game.run()


##class Block(pygame.sprite.Sprite):
##
##    # Constructor. Pass in the color of the block,
##    # and its x and y position
##    def __init__(self, color, width, height):
##       # Call the parent class (Sprite) constructor
##       pygame.sprite.Sprite.__init__(self)
##
##       # Create an image of the block, and fill it with a color.
##       # This could also be an image loaded from the disk.
##       self.image = pygame.Surface([width, height])
##       self.image.fill(color)
##
##       # Fetch the rectangle object that has the dimensions of the image
##       # Update the position of this object by setting the values of rect.x and rect.y
##       self.rect = self.image.get_rect()
