import pygame
import glob
import platform

DIR_CHAR = '/' if platform.system() == 'Darwin' else '\\'

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
        for sound_file in glob.glob(f".{DIR_CHAR}sounds{DIR_CHAR}*.mp3"):
            sound = pygame.mixer.Sound(sound_file)
            sound.set_volume(0.1)
            self.sounds[sound_file] = sound


    def play_sound(self, sound):
        if sound == "game-soundtrack.mp3":
            self.sounds[f'.{DIR_CHAR}sounds{DIR_CHAR}{sound}.mp3'].play(-1)
        else:
            self.sounds[f'.{DIR_CHAR}sounds{DIR_CHAR}{sound}.mp3'].play()