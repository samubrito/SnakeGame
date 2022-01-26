from cgitb import text
import pygame
from pygame.locals import *
from sys import exit
from random import randint
import neat

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('BoxCat_Games_-_CPU_Talk.mp3')
pygame.mixer.music.play(-1)
colisao = pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
x_cobra = int(largura/2)
y_cobra = int(altura/2)
x_maca = randint(50,640)
y_maca = randint(40,480)
velocidade = 5
x_controle = velocidade
y_controle = 0
lista_cobra = []
comprimento_inicial = 5
morreu = False
pontos = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont('arial',40,True,True)

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))

def reiniciar_jogo():
    global x_cobra,y_cobra,x_maca,y_maca,comprimento_inicial,morreu,lista_cobra,lista_cabeca,pontos
    pontos = 0
    lista_cabeca = []
    lista_cobra = []
    comprimento_inicial=5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    x_maca = randint(50,640)
    y_maca = randint(40,480)
    morreu = False

while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    texto = fonte.render(f'Pontos: {pontos}',True,(0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,20,20))

    if cobra.colliderect(maca):
        x_maca = randint(50,640)
        y_maca = randint(40,480)
        comprimento_inicial+=3
        pontos +=1
        colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra)>comprimento_inicial:
        del lista_cobra[0]
    
    if lista_cobra.count(lista_cabeca)>1:
        fonte2 = pygame.font.SysFont('arial',20,True,True)
        mensagem = 'Game over! Pressione R para reiniciar'
        texto = fonte2.render(mensagem,True,(0,0,0))
        ret_texto = texto.get_rect()
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura/2,altura/2)
            tela.blit(texto,ret_texto)
            pygame.display.update()

    if x_cobra>largura:
        x_cobra=0
    if x_cobra<0:
        x_cobra=largura
    if y_cobra>altura:
        y_cobra=0
    if y_cobra<0:
        y_cobra=altura
    aumenta_cobra(lista_cobra)

    tela.blit(texto,(400,30))
    pygame.display.update()