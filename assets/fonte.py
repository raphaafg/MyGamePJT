# font.py
import pygame
import sys

# Inicialização
pygame.init()
largura, altura = 700, 1000
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Visualizador de Fontes - Jogo de Corrida")

# Lista de fontes a testar (certifique-se que estão instaladas no seu sistema)
fontes = [
    "Orbitron", "Audiowide", "Russo One", "Exo", "Bebas Neue", "Ethnocentric",
    "Agency FB", "Square721 BT", "Microgramma", "Digital-7",
    "Bank Gothic", "Eurostile", "OCR A Extended", "DS-Digital", "Impact"
]

# Cor e tamanho
cor_texto = (255, 255, 255)
fundo = (30, 30, 30)
tamanho_fonte = 22
espaco_linha = 60
margem = 20

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    tela.fill(fundo)

    y = margem
    for nome_fonte in fontes:
        try:
            fonte = pygame.font.SysFont(nome_fonte, tamanho_fonte)
        except:
            fonte = pygame.font.Font(None, tamanho_fonte)

        texto = fonte.render(f"{nome_fonte}", True, cor_texto)
        tela.blit(texto, (margem, y))
        y += espaco_linha

    pygame.display.flip()
    clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
