

#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from pygame.font import Font # Import the Font class from the pygame.font module
from pygame import Rect
from pygame import Surface 

from code.const import COLOR_WARNINGYELLOW, WIN_WIDTH, WIN_HEIGHT
from code.const import COLOR_FLAME, COLOR_TURBOBLUE, COLOR_TURBOGREEN 
from code.const import FONT_TITLE_SIZE, FONT_OPTION_SIZE
from code.const import MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        #para inserir a imagem do menu: carregue a imagem, desenha o retangulo e coloca a imagem no retangulo
        self.surf = pygame.image.load('./assets/menuBg.png').convert_alpha() #load the background image
        self.rect = self.surf.get_rect(left=0, top=0)  #get the rectangle of the image setting the position (0,0 is default)
        self.clock = pygame.time.Clock()

        self.blip_sound = pygame.mixer.Sound('./assets/BLIP.wav')
        self.blip_sound.set_volume(0.5)    
        self.select_sound = pygame.mixer.Sound('./assets/SELECT.wav')

    #criacao de um metodo para desenhar o texto no menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        Font = pygame.font.SysFont(name="OCR A Extended", size=text_size) #cria a fonte
        Surface = Font.render(text, True, text_color).convert_alpha() #renderiza o texto com a fonte, antialiasing e cor
        Rect = Surface.get_rect(center=text_center_pos) #centra o retangulo do texto na posicao especificada
        self.window.blit(source=Surface, dest=Rect) #blit padrao, ou seja, desenha o texto na janela


    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./assets/Sound_Menu1.wav') # Load the background music for the menu
        pygame.mixer_music.play(loops=-1) # Play the background music in a loop (-1 means loop indefinitely)
        pygame.mixer_music.set_volume(0.08) 
        while True:

            ##--------------DRAW---IMAGES--------------##
            self.window.blit(source=self.surf, dest=self.rect)  #draw the image on the window - source is the image, dest is the rectangle where the image will be drawn
            self.menu_text(FONT_TITLE_SIZE, "RUNAWAY", COLOR_FLAME, text_center_pos=((WIN_WIDTH/2), 120) )
            self.menu_text(FONT_TITLE_SIZE, "HEAT", COLOR_FLAME, text_center_pos=((WIN_WIDTH/2), 200) )
            

            self.menu_text(10, "Created by Raphael Fagundes", COLOR_TURBOGREEN, text_center_pos=(74, 985) )

            for i in range(len(MENU_OPTION)):
                if i== menu_option: #if the current option is the selected one
                    self.menu_text(FONT_OPTION_SIZE, MENU_OPTION[i], COLOR_TURBOGREEN, text_center_pos=((WIN_WIDTH/2), (WIN_HEIGHT/2) + (i * 30)))
                else:
                    self.menu_text(FONT_OPTION_SIZE, MENU_OPTION[i], COLOR_WARNINGYELLOW, text_center_pos=((WIN_WIDTH/2), (WIN_HEIGHT/2) + (i * 30)))
                    # Draw each menu option with a vertical offset                                                                  ^^^^^^^^       
            
            pygame.display.flip()  #update the display to show the image
            self.clock.tick(60) # Limit the frame rate to 60 FPS
           


            ##--------------Check for all events--------------##
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #if the event is a quit event, exit the loop == close the window
                    quit() #End PYGAME

                if event.type == pygame.KEYDOWN: #check event for pressing a key
                    if event.key == pygame.K_DOWN: #if the key pressed is the down arrow key
                        self.blip_sound.play()
                        if menu_option < len(MENU_OPTION) - 1: #it is necessary to check the length to no surpass the number of options
                            menu_option += 1 #add 1 to the menu option (counter to navigate through the menu)
                        else:
                            menu_option = 0 #if the menu option is greater than the number of options, reset it to 0
                    if event.key == pygame.K_UP:#same but for the up arrow key
                        self.blip_sound.play()
                        if menu_option > 0:
                            menu_option -= 1 
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #event for pressing the enter key
                        self.select_sound.play()
                        return MENU_OPTION[menu_option] #return the selected option




            



