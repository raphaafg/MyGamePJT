import pygame

#C
COLOR_JET = (187, 50, 214)         # Roxo neon vibrante — ideal para títulos ou menus
COLOR_BLUESKY = (167, 236, 255)       # Azul céu claro — ótimo para texto leve sobre fundo escuro
COLOR_TURBOBLUE = (80, 50, 255)       # Azul profundo — para menus ou destaques
COLOR_FLAME = (255, 94, 0)            # Laranja fogo — para avisos, boosts ou contagem regressiva
COLOR_TURBOGREEN = (0, 255, 153)      # Verde neon — bom para feedback positivo ou velocidade
COLOR_WHITE = (245, 245, 245)    # Branco acinzentado — texto neutro sobre fundo escuro
COLOR_WARNINGYELLOW = (255, 209, 0)   # Amarelo alerta — ótimo para pontuação ou destaque

#F
FONT_TITLE_SIZE = 60  #Font size for the menu title
FONT_OPTION_SIZE = 18  #Font size for the menu options
FONT_HUD_SIZE = 20 #Font size for HUD

#H
HIT_COOLDOWN = 40 #Cool down for hits between entities (cars)

#M
MENU_OPTION = ( 'NEW GAME - 1P > ARCADE',
                'NEW GAME - 2P > COOPERATIVE',
                'NEW GAME - 2P > COMPETITIVE',
                'SCORE',
                'CONTROLS',
                'EXIT')

#P
PLAYER_KEY_UP = {'Player1_DLC': pygame.K_UP, 'Player2_DLC': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1_DLC': pygame.K_DOWN, 'Player2_DLC': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1_DLC': pygame.K_LEFT, 'Player2_DLC': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1_DLC': pygame.K_RIGHT, 'Player2_DLC': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1_DLC': pygame.K_SPACE, 'Player2_DLC': pygame.K_LSHIFT}
PLAYER_KEY_POWERUP = {'Player1_DLC': pygame.K_RCTRL, 'Player2_DLC': pygame.K_LCTRL}  

PROGRESSO_CHEGADA = 300 #Numero de Bg que devem ser decontados par ao final do jogo
PROGRESSO_LARGADA = 0 #Numero de inicio do contador

#T
TIME_SPAWN = 1300 #1.8s
TIMEOUT_STEP = 100  #0.1s
TIMEPUT_STAGE = 25000  #25s

#W
WIN_WIDTH = 700
WIN_HEIGHT = 900

WIN_SCORE_POS = { 'Title': (WIN_WIDTH/2, 50),
                 'EnterName': (WIN_WIDTH/2, 90),
                 'Label': (WIN_WIDTH/2, 100),
                 'Name': (WIN_WIDTH/2, 110),
                 0: (WIN_WIDTH/2, 130), #0 a 9 referente ao index do lista ordenada
                 1: (WIN_WIDTH/2, 150),
                 2: (WIN_WIDTH/2, 170),
                 3: (WIN_WIDTH/2, 190),
                 4: (WIN_WIDTH/2, 210),
                 5: (WIN_WIDTH/2, 230),
                 6: (WIN_WIDTH/2, 250),
                 7: (WIN_WIDTH/2, 270),
                 8: (WIN_WIDTH/2, 290),
                 9: (WIN_WIDTH/2, 310),            

}