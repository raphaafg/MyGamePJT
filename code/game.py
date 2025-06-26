import pygame

from code.const import WIN_HEIGHT, WIN_WIDTH
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init() # Initialize the pygame library
        pygame.mixer.init() # Initialize the mixer module for sound playback
        self.window = pygame.display.set_mode (size=(WIN_WIDTH,WIN_HEIGHT)) # Create a window

    def run(self):
        menu = Menu(self.window)
        while True:
            menu_return = menu.run()
        pass
    