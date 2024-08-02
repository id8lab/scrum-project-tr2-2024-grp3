import pygame
class audio_library():
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(frequency=44100, size = -16 , channels = 2 , allowedchanges=0)

        # Declaring Dir
        self.audio_path = {'background' : 'assets\\audio\\background\\' ,'effects' : 'assets\\audio\\effects\\'}

        # Declaring Defaults
        self.audio_bg_game_intro = pygame.mixer.Sound(self.audio_path['background']+'game_intro.wav')
        self.audio_bg_game_loop1 = pygame.mixer.Sound(self.audio_path['background']+'game_loop_1.wav')
        self.audio_bg_game_bridge = pygame.mixer.Sound(self.audio_path['background']+'game_bridge.wav')
        self.audio_bg_game_loop2 = pygame.mixer.Sound(self.audio_path['background']+'game_loop_2.wav')
        self.audio_bg_game_outro = pygame.mixer.Sound(self.audio_path['background']+'game_outro.wav')
        
        self.audio_bg_menu = pygame.mixer.Sound(self.audio_path['background']+'menu_theme.mp3')
        
        self.audio_p1_shoot = pygame.mixer.Sound(self.audio_path['effects']+'player_shoot_1.mp3')
        self.audio_p2_shoot = pygame.mixer.Sound(self.audio_path['effects']+'player_shoot_2.mp3')
        
        self.audio_p1_death = pygame.mixer.Sound(self.audio_path['effects']+'player_death_1.mp3')
        self.audio_p2_death = pygame.mixer.Sound(self.audio_path['effects']+'player_death_2.mp3')
        
        self.audio_jelly_death = pygame.mixer.Sound(self.audio_path['effects']+'jelly_death.mp3')
        
        self.audio_bg_game_intro.set_volume(.1) 
        self.audio_bg_game_loop1.set_volume(.1) 
        self.audio_bg_game_bridge.set_volume(.1) 
        self.audio_bg_game_loop2.set_volume(.1) 
        self.audio_bg_game_outro.set_volume(.1) 
        
        self.audio_bg_menu.set_volume(.1)
        
        self.audio_p1_shoot.set_volume(.3)
        self.audio_p2_shoot.set_volume(.65)
        
        self.audio_p1_death.set_volume(.65)
        self.audio_p2_death.set_volume(.65)
        
        self.audio_jelly_death.set_volume(.65)

    def background_music(self,screen,track):
        if screen == 'game':
            if track == 'intro':
                audio = self.audio_bg_game_intro
            if track == 'loop_1':
                audio = self.audio_bg_game_loop1
            if track == 'bridge':
                audio = self.audio_bg_game_bridge
            if track == 'loop_2':
                audio = self.audio_bg_game_loop2
            if track == 'outro':
                audio = self.audio_bg_game_outro
        if screen == 'menu':
            audio = self.audio_bg_menu
        return audio
            
    def audio_shoot(self,entity):
        if entity == 'player_1':
            audio = self.audio_p1_shoot
        if entity == 'player_2':
            audio = self.audio_p2_shoot
        return audio 
        
    def audio_death(self,entity):
        if entity == 'player_1':
            audio = self.audio_p1_death
        if entity == 'player_2':
            audio = self.audio_p2_death
        if entity == 'jellyfish':
            audio = self.audio_jelly_death
        return audio
        
        
        

        
        
