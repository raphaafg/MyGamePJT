import pygame

#C
COLOR_JET = (187, 50, 214)         # Roxo neon vibrante — ideal para títulos ou menus
COLOR_BLUESKY = (167, 236, 255)       # Azul céu claro — ótimo para texto leve sobre fundo escuro
COLOR_TURBOBLUE = (80, 50, 255)       # Azul profundo — para menus ou destaques
COLOR_FLAME = (255, 94, 0)            # Laranja fogo — para avisos, boosts ou contagem regressiva
COLOR_TURBOGREEN = (0, 255, 153)      # Verde neon — bom para feedback positivo ou velocidade
COLOR_WHITE = (245, 245, 245)    # Branco acinzentado — texto neutro sobre fundo escuro
COLOR_WARNINGYELLOW = (255, 209, 0)   # Amarelo alerta — ótimo para pontuação ou destaque

#E
ENEMY_SPAWN = pygame.USEREVENT + 1 
EVENT_TIMEOUT = pygame.USEREVENT + 2
EVENT_CIV_SPAWN = pygame.USEREVENT + 3


ENTITY_SPEED = {
    'Map10': 5,
    'Map20': 6,
    'Map11': 10,
    'Map21': 8,
    'PlayerA0':5,
    'PlayerB0':5,
    'Enemy1': 1,
    'Enemy2': 1,
    'PlayerA0Shot': 7,
    'PlayerB0Shot': 5,
    'Enemy1Shot': 3,
    'Enemy2Shot': 3,
    'CIVILIAN1': 5, 
    'CIVILIAN2': 6, 
    'CIVILIAN3': 7, 
    'CIVILIAN4': 7, 
    'CIVILIAN5': 7, 
    'CIVILIAN6': 7, 
}

ENTITY_HEALTH = {
    'Map10': 999,
    'Map20': 999,
    'Map11': 999,
    'Map21': 999,
    'PlayerA0': 300,
    'PlayerA0Shot': 1,
    'PlayerB0': 300,
    'PlayerB0Shot': 1,
    'Enemy1': 40,
    'Enemy2': 65,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'CIVILIAN1': 999, 
    'CIVILIAN2': 999, 
    'CIVILIAN3': 999, 
    'CIVILIAN4': 999, 
    'CIVILIAN5': 999, 
    'CIVILIAN6': 999, 
}

ENTITY_SHOT_DELAY = {
    'PlayerA0': 20,
    'PlayerB0': 30,
    'Enemy1': 6000,
    'Enemy2': 1500,
}

ENTITY_DAMAGE = {
    'Map10': 0,
    'Map20': 0,
    'Map11': 0,
    'Map21': 0,
    'PlayerA0': 5,
    'PlayerB0': 5,
    'Enemy1': 999,
    'Enemy2': 999,
    'PlayerA0Shot': 20,
    'PlayerB0Shot': 25,
    'Enemy1Shot': 20,
    'Enemy2Shot': 30,
    'CIVILIAN1': 15, 
    'CIVILIAN2': 15, 
    'CIVILIAN3': 15, 
    'CIVILIAN4': 15, 
    'CIVILIAN5': 15, 
    'CIVILIAN6': 15, 
}

ENTITY_SCORE = {
    'Map10': 0,
    'Map20': 0,
    'Map11': 0,
    'Map21': 0,
    'PlayerA0': 0,
    'PlayerB0': 0,
    'Enemy1': 100,
    'Enemy2': 150,
    'PlayerA0Shot': 0,
    'PlayerB0Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'CIVILIAN1': 0, 
    'CIVILIAN2': 0, 
    'CIVILIAN3': 0, 
    'CIVILIAN4': 0, 
    'CIVILIAN5': 0, 
    'CIVILIAN6': 0, 
}

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
PLAYER_KEY_UP = {'PlayerA0': pygame.K_UP, 'PlayerB0': pygame.K_w}
PLAYER_KEY_DOWN = {'PlayerA0': pygame.K_DOWN, 'PlayerB0': pygame.K_s}
PLAYER_KEY_LEFT = {'PlayerA0': pygame.K_LEFT, 'PlayerB0': pygame.K_a,'Enemy1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'PlayerA0': pygame.K_RIGHT, 'PlayerB0': pygame.K_d, 'Enemy1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'PlayerA0': pygame.K_SPACE, 'PlayerB0': pygame.K_LSHIFT}
PLAYER_KEY_CANCEL = {'PlayerA0': pygame.K_RCTRL, 'PlayerB0': pygame.K_LCTRL}  

PROGRESSO_CHEGADA = 300 #Numero de Bg que devem ser decontados par ao final do jogo
PROGRESSO_LARGADA = 0 #Numero de inicio do contador
PROGRESSO_COUNT = 0



#T
TIME_ENEMY_SPAWN = 10500 
TIMEOUT_STEP = 100  #0.1s
TIMEOUT_STAGE = 90000  #90s
TIME_CIVILIAN_SPAWN = 6500

#W
WIN_WIDTH = 700
WIN_HEIGHT = 1000

WIN_SCORE_POS = { 'Title': (WIN_WIDTH/2, 100),
                 'EnterName': (WIN_WIDTH/2, 140),
                 'Label': (WIN_WIDTH/2, 170),
                 'Name': (WIN_WIDTH/2, 190),
                 0: (WIN_WIDTH/2, 210), #0 a 9 referente ao index do lista ordenada
                 1: (WIN_WIDTH/2, 230),
                 2: (WIN_WIDTH/2, 250),
                 3: (WIN_WIDTH/2, 270),
                 4: (WIN_WIDTH/2, 290),
                 5: (WIN_WIDTH/2, 310),
                 6: (WIN_WIDTH/2, 330),
                 7: (WIN_WIDTH/2, 350),
                 8: (WIN_WIDTH/2, 370),
                 9: (WIN_WIDTH/2, 390),
                 10: (WIN_WIDTH/2, 410),
                 11: (WIN_WIDTH/2, 430),
                 12: (WIN_WIDTH/2, 450),
                 13: (WIN_WIDTH/2, 470),
                 14: (WIN_WIDTH/2, 490),
                 15: (WIN_WIDTH/2, 510)           

}

WIN_POSX_RUA1 = ((WIN_WIDTH/2) + 100)
WIN_POSX_RUA2 = ((WIN_WIDTH/2) - 120)
