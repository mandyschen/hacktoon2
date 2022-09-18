import pygame
import glob


class GameGUI:

    def __init__(self):
        self.clock = pygame.time.Clock()

    def start(self):
        pygame.font.init()
        pygame.mixer.init()
        pygame.display.init()
        self.load_sounds()

    def load_sounds(self):
        self.sounds = {}
        for sound_file in glob.glob(f"./sounds/*.mp3"):
            sound = pygame.mixer.Sound(sound_file)
            self.sounds[sound_file] = sound


    def play_sound(self, sound):
        self.sounds[f'./sounds/{sound}.mp3'].play(-1)