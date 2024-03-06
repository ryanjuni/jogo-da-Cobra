import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
X_cobra = int(largura / 2)
Y_cobra = int(altura / 2)
X_maca = randint(40, 600)
Y_maca = randint(50, 430)
Pontos = 0
Velocidade = 10
X_controle = Velocidade
Y_controle = 0

fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Joguinho da Cobra')
relogio = pygame.time.Clock()

musica_de_fundo = pygame.mixer.music.load('stranger-things-124008.mp3')
pygame.mixer.music.play(-1)

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
X_cobra = int(largura / 2)
Y_cobra = int(altura / 2)
X_maca = randint(40, 600)
Y_maca = randint(50, 430)
Pontos = 0
Velocidade = 10
X_controle = Velocidade
Y_controle = 0

fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Joguinho da Cobra')
relogio = pygame.time.Clock()

musica_de_fundo = pygame.mixer.music.load('stranger-things-124008.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
pygame.mixer.music.set_volume (0.05)

lista_cobra = []
comprimento_cobra = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global Pontos, comprimento_cobra, X_cobra, Y_cobra, lista_cobra, morreu
    Pontos = 0
    comprimento_cobra = 5
    X_cobra = int(largura / 2)
    Y_cobra = int(altura / 2)
    lista_cobra = []
    morreu = False

def desenha_texto(texto, x, y):
    texto_formatado = fonte.render(texto, True, (255, 255, 255))
    tela.blit(texto_formatado, (x, y))

while True:
    relogio.tick(10)
    tela.fill((0, 0, 0))  # Preenche a tela com preto

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_r and morreu:
                reiniciar_jogo()
    if len(lista_cobra) > comprimento_cobra:
        del lista_cobra[0]

    keys = pygame.key.get_pressed()
    if keys[K_a]:
        if X_controle == Velocidade:
            pass
        else:
            X_controle = -Velocidade
            Y_controle = 0
    if keys[K_d]:
        if X_controle == -Velocidade:
            pass
        else:
            X_controle = Velocidade
            Y_controle = 0
    if keys[K_w]:
        if Y_controle == Velocidade:
            pass
        else:
            Y_controle = -Velocidade
            X_controle = 0
    if keys[K_s]:
        if Y_controle == -Velocidade:
            pass
        else:
            Y_controle = Velocidade
            X_controle = 0

    X_cobra += X_controle
    Y_cobra += Y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (X_cobra, Y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (X_maca, Y_maca, 20, 20))

    if cobra.colliderect(maca):
        X_maca = randint(40, 600)
        Y_maca = randint(50, 430)
        Pontos += 1
        barulho_colisao.play()
        comprimento_cobra += 1

    cabeca_cobra = [X_cobra, Y_cobra]
    lista_cobra.append(cabeca_cobra)

    if lista_cobra.count(cabeca_cobra) > 1:
        ret_Texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
                   

            tela.fill((0, 0, 0))  
            mensagem = 'Game Over! Pressione R para recomeçar.'
            fonte2 = pygame.font.SysFont('arial',20,True,True)
            texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
         
            ret_texto_center = texto_formatado.get_rect(center=(largura // 2, altura // 2))
            tela.blit(texto_formatado,ret_texto_center)
            
            pygame.display.update()

    else:
        aumenta_cobra(lista_cobra)
        mensagem = f'Pontos: {Pontos}'
        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
        tela.blit(texto_formatado, (400, 30))
        pygame.display.update()

        
    if  X_cobra > largura: 
            X_cobra = 0 
    if X_cobra < 0:
           X_cobra = largura
    if  Y_cobra < 0 : 
            Y_cobra = altura  
    if  Y_cobra > altura:
            Y_cobra = 0 

lista_cobra = []
comprimento_cobra = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global Pontos, comprimento_cobra, X_cobra, Y_cobra, lista_cobra, morreu
    Pontos = 0
    comprimento_cobra = 5
    X_cobra = int(largura / 2)
    Y_cobra = int(altura / 2)
    lista_cobra = []
    morreu = False

def desenha_texto(texto, x, y):
    texto_formatado = fonte.render(texto, True, (255, 255, 255))
    tela.blit(texto_formatado, (x, y))

while True:
    relogio.tick(10)
    tela.fill((0, 0, 0))  # Preenche a tela com preto

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_r and morreu:
                reiniciar_jogo()
    if len(lista_cobra) > comprimento_cobra:
        del lista_cobra[0]

    keys = pygame.key.get_pressed()
    if keys[K_a]:
        if X_controle == Velocidade:
            pass
        else:
            X_controle = -Velocidade
            Y_controle = 0
    if keys[K_d]:
        if X_controle == -Velocidade:
            pass
        else:
            X_controle = Velocidade
            Y_controle = 0
    if keys[K_w]:
        if Y_controle == Velocidade:
            pass
        else:
            Y_controle = -Velocidade
            X_controle = 0
    if keys[K_s]:
        if Y_controle == -Velocidade:
            pass
        else:
            Y_controle = Velocidade
            X_controle = 0

    X_cobra += X_controle
    Y_cobra += Y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (X_cobra, Y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (X_maca, Y_maca, 20, 20))

    if cobra.colliderect(maca):
        X_maca = randint(40, 600)
        Y_maca = randint(50, 430)
        Pontos += 1
        barulho_colisao.play()
        comprimento_cobra += 1

    cabeca_cobra = [X_cobra, Y_cobra]
    lista_cobra.append(cabeca_cobra)

    if lista_cobra.count(cabeca_cobra) > 1:
        ret_Texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
                   

            tela.fill((0, 0, 0))  
            mensagem = 'Game Over! Pressione R para recomeçar.'
            fonte2 = pygame.font.SysFont('arial',20,True,True)
            texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
         
            ret_texto_center = texto_formatado.get_rect(center=(largura // 2, altura // 2))
            tela.blit(texto_formatado,ret_texto_center)
            
            pygame.display.update()

    else:
        aumenta_cobra(lista_cobra)
        mensagem = f'Pontos: {Pontos}'
        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
        tela.blit(texto_formatado, (400, 30))
        pygame.display.update()

        
    if  X_cobra > largura: 
            X_cobra = 0 
    if X_cobra < 0:
           X_cobra = largura
    if  Y_cobra < 0 : 
            Y_cobra = altura  
    if  Y_cobra > altura:
            Y_cobra = 0  
