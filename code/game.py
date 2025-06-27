import pygame


from code.control import Control
from code.score import Score
from code.const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init() # Initialize the pygame library
        pygame.mixer.init() # Initialize the mixer module for sound playback
        self.window = pygame.display.set_mode (size=(WIN_WIDTH,WIN_HEIGHT)) # Create a window

    def run(self):
        menu = Menu(self.window)
        while True:
            score = Score(self.window)
            control = Control(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()
        
        ##----- selecting menu option -----##
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: #if player selects to play 1p. 2p coop or 2p vs, starts the level 1
                player_score = [0, 0] #[score player 1, score player 2]
                level = Level(self.window, 'Level 1', menu_return, player_score) #create a new Level object with the window and level name
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level 2', menu_return, player_score) #create a new Level object with the window and level name (the second level)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)


            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                control.run()
            elif menu_return == MENU_OPTION[5]:
                pygame.quit() #quit the game closing the window
                quit()
            else:
                pygame.quit() #quit the game closing the window
                quit()

    