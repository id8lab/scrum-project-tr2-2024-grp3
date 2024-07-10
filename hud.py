import pygame

class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)  # Set the font and size

    def render(self, screen, score, p1_health, p2_health):
        # Render the score
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Render Player 1 health
        p1_health_text = self.font.render(f"P1 Health: {p1_health}", True, (255, 255, 255))
        screen.blit(p1_health_text, (10, 50))

        # Render Player 2 health
        p2_health_text = self.font.render(f"P2 Health: {p2_health}", True, (255, 255, 255))
        screen.blit(p2_health_text, (10, 90))
