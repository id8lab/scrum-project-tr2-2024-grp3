import pygame

class spritesheet(object):
    # Try obtain player sprites + failsafe
    def __init__(self,spritesheet):
        try:
            self.sprite_sheet = pygame.image.load(spritesheet).convert_alpha()
        except (pygame.error, message):
            print ('Player spritesheet not found')
            print ('Spritesheet should be located within :',spritesheet)
            raise SystemExit

    # Load a image
    def image_at(self, rectangle, colorkey = (0,0,0)):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sprite_sheet, (0,0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load group of images
    def images_at(self, rects, colorkey=(0,0,0)):
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load strip of images
    def load_strip(self,rect, image_count, colorkey=(0,0,0)):
        tups = [(rect[0] + rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
        return self.images_at(tups,colorkey)
    
