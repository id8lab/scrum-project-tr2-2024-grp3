import pygame
from SpriteLibrary import sprite_library

class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)  # Set the font and size

    def render(self, screen, score, p1_life, p2_life,life_sprite,life_coord):
        # Render the score
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Render Player 1 life
        p1_life_text = self.font.render(f"P1 life: {p1_life}", True, (255, 255, 255))
        screen.blit(p1_life_text, (10, 50))

        # Render Player 2 life
        p2_life_text = self.font.render(f"P2 life: {p2_life}", True, (255, 255, 255))
        screen.blit(p2_life_text, (10, 90))
        
        # Rendering Player 1 life
        p1_life_coord = life_coord[0]
        for iterations in range (p1_life):
            screen.blit(life_sprite[0],(p1_life_coord[0],p1_life_coord[1]))
            p1_life_coord[0] += 15
        p1_life_coord[0] = 15
        
        # Rendering Player 2 life
        p2_life_coord = life_coord[1]
        for iterations in range (p2_life):
            screen.blit(life_sprite[1],(p2_life_coord[0],p2_life_coord[1]))
            p2_life_coord[0] -= 15
        p2_life_coord[0] = 1420
        
