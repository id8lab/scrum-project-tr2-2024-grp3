from SpriteLibrary import sprite_library
from Players import Player
from AudioLibrary import audio_library
from Enemies import enemy
from pygame.locals import *
import pygame
from pygame_starter import Game
from hud import HUD  # Import the HUD class
from random import randint


#ADD effects , done player shooting effect & loop1 + intro

print('hi')
""" Setting Window's Size """
global win
win = pygame.display.set_mode((1450,750))
sl = sprite_library()
al = audio_library()

p1 = Player(1)
p2 = Player(2)


# testing random spawn
ex = randint(0,1357)
ey = randint(0,300)


class Galaga(Game,audio_library):
    def __init__(self):
        super().__init__()
        global win
        win = pygame.display.set_mode((1450,750))
        #pygame.mixer.pre_init(frequency=24455, size = -12 , channels = 2 , allowedchanges=0)

        self.clock = pygame.time.Clock()
        self.global_tick = 0
        self.p1_cd = 0
        self.p2_cd = 0

        # Player's Variables
        self.life_coords = sl.Hud_Life_Coord()
        
        # Load Background
        self.background = pygame.image.load("assets/bg.jpg").convert()
        self.bg_width = self.background.get_width()
        self.bg_height = self.background.get_height()
        
        # Initialize background positions
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height
        self.bg_scroll_speed = 5  # Adjust scroll speed as needed
        
        # Initialize vars
        self.p1_coords = p1.GetCoords()
        p1_movement = False
        self.p2_coords = p2.GetCoords()
        self.p1_player_hitbox = p1.PlayerHitbox(self.p1_coords[0],self.p1_coords[1])
        self.p2_player_hitbox = p2.PlayerHitbox(self.p2_coords[0],self.p2_coords[1])
        
        self.p1_projectile = p1.GetProjectile()
        self.p2_projectile = p2.GetProjectile()
        self.player_projectiles = [self.p1_projectile,self.p2_projectile]
        
        self.p1_projectile_hitbox = p1.ProjectileHitbox(self.p1_projectile[0],self.p1_projectile[1])
        self.p2_projectile_hitbox = p2.ProjectileHitbox(self.p2_projectile[0],self.p2_projectile[1])

        self.total_enemies = []
        self.enemy_hit_status = False

         # Initialize HUD
        self.hud = HUD()
        self.score = 0  # Example score
        self.p1_life = p1.Life()  # Example Player 1 life
        self.p2_life = p2.Life()  # Example Player 2 life
        
        self.total_enemies = []

        # Initialize Groups
        self.current_enemies = pygame.sprite.Group()

        self.players = pygame.sprite.Group()
        self.players.add(p1)
        self.players.add(p2)

        # Initialize Audio
        self.audio_bg_intro = al.background_music('game','intro')
        self.audio_bg_loop1 = al.background_music('game','loop_1')
        self.audio_bg_bridge = al.background_music('game','bridge')
        self.audio_bg_loop2 = al.background_music('game','loop_2')
        self.audio_bg_outro = al.background_music('game','outro')
        
        self.audio_player_shoot_1 = al.audio_shoot('player_1')
        self.audio_player_shoot_2 = al.audio_shoot('player_2')

        self.audio_bg_intro.play()
        
    def background_music(self):
        print(pygame.mixer.Sound.get_length(self.audio_bg_intro))
        self.audio_bg_loop1.play(-1)
        
    def test(self,surface):
        sprites = self.sprites()
        for sprite in sprites:
            sprite.image
        
        return sprite.image
    
##    def hitchecker(self):
##        for player_temp in self.players.sprites():
##            projectile_hb = player_temp.hitbox()
##            for enemy_temp in self.current_enemies.sprites():
##                enemy_hb = enemy_temp.hitbox()
##                
##                if pygame.Rect.colliderect(enemy_hb,projectile_hb):
##                    enemy_temp.hit()
    def game(self):
        bg_flag = pygame.mixer.get_busy()
        if bg_flag == False:
            self.background_music()
        self.clock.tick(250)
        self.global_tick = pygame.time.get_ticks()

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
        """Player 1 movement"""
        # movement flag
        if keypress[K_LEFT] or keypress[K_RIGHT] or keypress[K_UP]or keypress[K_DOWN]:
            p1_MoveFlag = True
        else:
            p1_MoveFlag = False
            
        if keypress[K_LEFT]:
            if (self.p1_coords[0] - 11) >= 0 :
                self.p1_coords[0] = self.p1_coords[0] - 11
            
            
        if keypress[K_RIGHT]:
            if (self.p1_coords[0] + 11) <= 1450-39:
                self.p1_coords[0] = self.p1_coords[0] + 11
            
            
        if keypress[K_UP]:
            if (self.p1_coords[1] - 7) >= 0:
                self.p1_coords[1] = self.p1_coords[1] - 7
            
            
        if keypress[K_DOWN]:
            if (self.p1_coords[1] + 7) <= 750-57:
                self.p1_coords[1] = self.p1_coords[1] + 7
            
        # firing mechanism
        p1_FireFlag = False
        if self.p1_cd == 10:
            if (keypress[K_RSHIFT] > 0 ):
                p1_FireFlag = True
                self.audio_player_shoot_1.play()
                sprite = p1.Fire(self.p1_coords)
                if self.player_projectiles[0][1] < 0:
                    self.player_projectiles[0][0] = self.p1_coords[0]
                    self.player_projectiles[0][1] = self.p1_coords[1] + 10
                else :
                    self.player_projectiles[0][1] = self.player_projectiles[0][1] - 100
             
                
                self.p1_cd = 0
##                win.blit(sprite,(self.player_projectiles[0][0],self.player_projectiles[0][1]))
##                pygame.display.update
                
            
        elif self.player_projectiles[0][1] > 0:
            p1_FireFlag = True
            sprite = p1.Fire(self.p1_coords)
            if self.player_projectiles[0][1] < 0:
                self.player_projectiles[0][0] = self.p1_coords[0]
                self.player_projectiles[0][1] = self.p1_coords[1] + 10
            else :
                self.player_projectiles[0][1] = self.player_projectiles[0][1] - 100
         
            
            self.p1_cd = 0
##            win.blit(sprite,(self.player_projectiles[0],self.player_projectiles[0][1]))
##            pygame.display.update
        else:
            self.p1_cd += 1

        try:
            win.blit(sprite,(self.player_projectiles[0][0],self.player_projectiles[0][1]))
            pygame.display.update    
        except UnboundLocalError:
            1+1
            

        """ Player 2 movement"""
        if keypress[K_a] or keypress[K_d] or keypress[K_w]or keypress[K_s]:
            p2_MoveFlag = True
        else:
            p2_MoveFlag = False
            
        if keypress[K_a]:
            if (self.p2_coords[0] - 11) >= 0 :
                self.p2_coords[0] = self.p2_coords[0] - 11
            
        if keypress[K_d]:
            if (self.p2_coords[0] + 11) <= 1450-39:
                self.p2_coords[0] = self.p2_coords[0] + 11
            
        if keypress[K_w]:
            if (self.p2_coords[1] - 7) >= 0:
                self.p2_coords[1] = self.p2_coords[1] - 7
            
        if keypress[K_s]:
            if (self.p2_coords[1] + 7) <= 750-57:
                self.p2_coords[1] = self.p2_coords[1] + 7

        p2_FireFlag = False    
        if self.p2_cd == 10:
            if (keypress[K_q] > 0 ):
                p2_FireFlag = True
                self.audio_player_shoot_2.play()
                sprite = p2.Fire(self.p2_coords)
                if self.player_projectiles[1][1] < 0:
                    self.player_projectiles[1][0] = self.p2_coords[0]
                    self.player_projectiles[1][1] = self.p2_coords[1] + 10
                else :
                    self.player_projectiles[1][1] = self.player_projectiles[1][1] - 100
             
                
                self.p2_cd = 0

            
        elif self.player_projectiles[1][1] > 0:
            p2_FireFlag = True
            sprite = p2.Fire(self.p2_coords)
            if self.player_projectiles[1][1] < 0:
                self.player_projectiles[1][0] = self.p2_coords[0]
                self.player_projectiles[1][1] = self.p2_coords[1] + 10
            else :
                self.player_projectiles[1][1] = self.player_projectiles[1][1] - 100
         
            
            self.p2_cd = 0
        else:
            p2_FireFlag = False
            self.p2_cd += 1
            
        """ Special Keys """
        # Simulate health gain/loss
        if keypress[K_j]:
            if self.p1_life - 1 >= 0:
                self.p1_life -= 1
        if keypress[K_l]:
            self.p1_life += 1

        # Spawn enemies
##        if keypress[K_p]:
##            # Test if bullet hits enemy
##            for player_temp in self.players.sprites():
##                projectile_hb = ProjectileHitbox()
##                for enemy_temp in self.current_enemies.sprites():
##                    enemy_hb = enemy_temp.hitbox()
##                    if pygame.Rect.colliderect(enemy_hb,projectile_hb):
##                        enemy_temp.hit()
                
        if keypress[K_k]:
            enemy_type = randint(1,1)
            if enemy_type == 1:
                enemy_type = 'jellyfish'
                
            elif enemy_type == 2:
                enemy_type = 'flier'
                enemy_type = 'jellyfish'
                
            elif enemy_type == 3:
                enemy_type = 'ship'
                
            
            
            
            count=str(len(self.total_enemies) + 1)
            name = enemy_type + count
            self.total_enemies.append(name)
        
            ex = randint(0,1357)
            ey = randint(0,300)
            print(ex, '-',ey)

            if enemy_type == 'jellyfish':
                globals()[name] = enemy(ex,ey,enemy_type)
                self.current_enemies.add(globals()[name])
                
                #self.current_enemies.draw(win)
            
            print(enemy_type)
            print(self.current_enemies)
            
    

        try:
            win.blit(sprite,(self.player_projectiles[1][0],self.player_projectiles[1][1]))
            pygame.display.update
        except UnboundLocalError:
            1 + 1
            
        # Update sprites
        p1_sprite = p1.Update()
        p2_sprite = p2.Update()

        # Player Related Flags
        if p1_MoveFlag:     #Update hitbox if movement flag tripped
            self.p1_player_hitbox = p1.PlayerHitbox(self.p1_coords[0],self.p1_coords[1])
        if p1_FireFlag:
            self.p1_projectile_hitbox = p1.ProjectileHitbox(self.player_projectiles[0][0],self.player_projectiles[0][1])
            
        if p2_MoveFlag:     #Update hitbox if movement flag tripped
            self.p2_player_hitbox = p2.PlayerHitbox(self.p2_coords[0],self.p2_coords[1])
        if p2_FireFlag:                                                                                             #Player's projectile hitbox dont stick to sprite
            self.p2_projectile_hitbox = p2.ProjectileHitbox(self.player_projectiles[1][0],self.player_projectiles[1][1])
            
        self.player_projectiles_hb = [self.p1_projectile_hitbox,self.p2_projectile_hitbox]
        
        # Detecting collisions
##        for projectile_hitbox in self.projectile_players_hb:
##            if pygame.Rect.colliderect(self.entity_hitbox,projectile_hitbox):
##                if self.health <= 0:
##                    self.kill()
##                else:
##                    self.health -= 1
##                    print('ouch')
                    
            
        pygame.draw.rect(win, (255,0,0), self.p1_player_hitbox,2)
        pygame.draw.rect(win, (255,0,0), self.p1_projectile_hitbox,2)
        
        pygame.draw.rect(win, (255,0,0), self.p2_player_hitbox,2)
        pygame.draw.rect(win, (255,0,0), self.p2_projectile_hitbox,2)
        
        self.current_enemies.update(win,self.player_projectiles_hb)

##        self.hitchecker()
        
        #self.current_enemies.draw(win)
        #jelly1.draw(win)
        
        win.blit(p1_sprite,(self.p1_coords[0],self.p1_coords[1]))
        win.blit(p2_sprite,(self.p2_coords[0],self.p2_coords[1]))

        p1_life_sprite = p1.LifeUpdate(0)
        p2_life_sprite = p2.LifeUpdate(0)

        Hud_Life_Sprite =[p1_life_sprite , p2_life_sprite]

        # Render HUD
        self.hud.render(win, self.score, self.p1_life, self.p2_life,Hud_Life_Sprite,self.life_coords)

        pygame.display.update()


if __name__ == "__main__":
    game = Galaga()
    game.run()
