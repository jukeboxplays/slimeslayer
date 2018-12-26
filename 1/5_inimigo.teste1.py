

# -*- coding: utf-8 -*-

import platform

import pickle

import socket

host = ""
port = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

import random

import pygame

from pygame.locals import*

import time



pygame.init()

ponto_jogador = int(0)
ponto_oponente = int(0)


clock = pygame.time.Clock()

width = 800
height = 600

tela = pygame.display.set_mode((width,height))

pygame.display.set_caption("Slime Slayer")

fundo = pygame.image.load("PAPEL QUADRICULADO.jpg")

mfonte = pygame.font.SysFont("monospace", 35)
mfonte2 = pygame.font.SysFont("monospace", 15)

class Archer (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImageArcher = pygame.image.load('idle.png')
##cria uma classe e importa imagem

        self.rect = self.ImageArcher.get_rect ()
        self.rect.centerx = width/2
        self.rect.centery = height/2
##posiciona imagem
        self.velocidade = 7
##variaveis relacionadas somente ao personagem

    def mov (self):
        if self.rect.left <= -20:
            self.rect.left = -20

        if self.rect.right > 820:
            self.rect.right = 820

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom > 600:
            self.rect.bottom = 600
##verifica posi??o do personagem


    def tiro_up (self):
        flecha_up = FlechaUp(self.rect.centerx, self.rect.top)
        flechas.add(flecha_up)

    def tiro_down (self):
        flecha_down = FlechaDown(self.rect.centerx, self.rect.bottom)
        flechas.add(flecha_down)

    def tiro_right (self):
        flecha_right = FlechaRight(self.rect.right, self.rect.centery)
        flechas.add(flecha_right)

    def tiro_left (self):
        flecha_left = FlechaLeft(self.rect.left, self.rect.centery)
        flechas.add(flecha_left)

# os quatro métodos "tiro" acima fazem com q o player possa atirar as flechas. Existe uma função para cada direção em que a flecha será atirada.
# cada um deles cria um objeto de flecha e o adiciona em um grupo de objeto de flechas (chamado "flechas")

    """def disparo (self, x, y):
        MyArrow = Arrow (x, y)
        self.quiver.append(MyArrow)"""

    def place (self, surface):
        surface.blit (self.ImageArcher, self.rect)
##carimba o personagem na posi??o determinada anteriormente

class Inimigo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("inimigo.png").convert(), [100,50])
		self.image.set_colorkey(self.image.get_at((0,0)))
# carrega imagem do inimigo e tira o fundo colorido
		self.rect = self.image.get_rect()
# captura o retangulo do inimigo
		self.take = random.randint(1,4)
# cria uma variavel take e sorteia um valor de 1 a 4 para colocar nela
		if self.take == 1:
			self.rect.x = -6
			self.rect.y = random.randrange(0,height-self.rect.height)
# se take for 1, o personagem vai spawnar do canto esquerdo da tela

		elif self.take == 2:
			self.rect.x = random.randrange(0,width-self.rect.width)
			self.rect.y = -6
# se take for 2, o personagem vai spawnar do canto superior da tela

		elif self.take == 3:
			self.rect.x = width+6
			self.rect.y = random.randrange(0,height-self.rect.height)
# se take for 3, o personagem vai spawnar do canto direito da tela
		
		elif self.take == 4:
			self.rect.x = random.randrange(0,width-self.rect.width)
			self.rect.y = height+6
# se take for 4, o personagem vai spawnar do canto inferior da tela

	def update(self, px, py):
		if self.rect.centerx < px:
			self.rect.centerx += 1

		elif self.rect.centerx > px:
			self.rect.centerx -= 1

		if self.rect.centery > py:
			self.rect.y -= 1

		elif self.rect.centery < py:
			self.rect.centery += 1

# todo inimigo criado irá simplesmente caminhar em linha reta em relação à sua posição inicial, por exemplo: se ele surgiu do canto superior ele vai caminhar em linha reta até o canto inferior e vice-versa. Se ele surgir do canto esquerdo, ele irá em linha reta pro canto direito e vice-versa. O método self.kill() deleta a variável que receber essa classe do código, para não ficar caminhando pelo infinito sem ser deletada da memória do pc.
			

# Abaixo: classe da flecha que é atirada pra cima
class FlechaUp(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("ARROWUP.png").convert()
		self.image.set_colorkey(self.image.get_at((0,0)))
		self.rect = self.image.get_rect()
		self.rect.bottom = y # a parte de baixo vertical (y) da flecha dessa classe vai equivaler à parte de cima vertical do jogador, conforme o método tiro_up da classe Archer
		self.rect.centerx = x # o centro x (horizontal) dessa flecha é o mesmo centro horizontal do jogador
		self.velocidade = 7

	def update(self):
		# Vai pra cima:
		self.rect.y -= self.velocidade
		# Se sair da tela desaparece:
		if self.rect.bottom < 0:
			self.kill()	

# classe da flecha que vai pra baixo
class FlechaDown(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("ARROWDOWN.png").convert()
		self.image.set_colorkey(self.image.get_at((0,0)))
		self.rect = self.image.get_rect()
		self.rect.top = y # a parte de cima vertical (y) da flecha dessa classe vai equivaler à parte de baixo vertical do jogador, conforme o método tiro_down da classe Archer
		self.rect.centerx = x # o centro x (horizontal) dessa flecha é o mesmo centro horizontal do jogador
		self.velocidade = 7

	def update(self):
		# Vai pra baixo:
		self.rect.y += self.velocidade
		# Se sair da tela desaparece:
		if self.rect.top > height:
			self.kill()


class FlechaRight(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("ARROWRIGHT.png").convert()
		self.image.set_colorkey(self.image.get_at((0,0)))
		self.rect = self.image.get_rect()
		self.rect.left = x  # a parte esquerda horizontal (x) da flecha dessa classe vai equivaler à parte direita horizontal do jogador, conforme o método tiro_right da classe Archer
		self.rect.centery = y # o centro y (vertical) dessa flecha é o mesmo centro horizontal do jogador
		self.velocidade = 7

	def update(self):
		# Vai pra direita
		self.rect.x += self.velocidade
		# Se sair da tela desaparece:
		if self.rect.left > width:
			self.kill()

class FlechaLeft(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("ARROWLEFT.png").convert()
		self.image.set_colorkey(self.image.get_at((0,0)))
		self.rect = self.image.get_rect()
		self.rect.right = x # a parte direita horizontal (x) da flecha dessa classe vai equivaler à parte esquerda horizontal do jogador, conforme o método tiro_left da classe Archer
		self.rect.centery = y # o centro y (vertical) dessa flecha é o mesmo centro horizontal do jogador
		self.velocidade = 7

	def update(self):
		# Vai pra esquerda
		self.rect.x -= self.velocidade
		# Se sair da tela desaparece:
		if self.rect.right < 0:
			self.kill()

		
		
		

# Variável ligada ao loop infinito (ele vai rodar enquanto ela for True e para quando ela for False)
rodando = True

# Grupo com os sprites dos inimigos
inimigos = pygame.sprite.Group()
# Grupo com os sprites das flechas
flechas = pygame.sprite.Group()

# variável a ser usada como medida de tempo para a geração de inimigos no loop infinito
count = 0

time_count = 0

# objeto player q recebe a classe Archer
player = Archer()
# loop infinito 
while rodando:
	clock.tick(60)
	print time_count
	time_count += 1
	if time_count == 5000:
		rodando = False
	# comando que não deixa o player sair da tela do jogo
	player.mov()
	# a cada iteração do loop infinito, o valor de count sobe +1
	count += 1
	# se count atingir o valor especificado no if abaixo, é criada uma variável inim que recebe a classe inimigo, ou seja, o objeto do inimigo. Além disso, ela é adicionada ao grupo de sprites dos inimigos
	if count == 100:
		# você(s) pode(m) brincar com o valor do if acima! Quanto maior o valor acima, maior o intervalo de tempo entre a criação de um inimigo e a criação de outro. 
		inim = Inimigo()
		inimigos.add(inim)
		# count é zerada, e assim q ela atingir o valor especificado no if acima, outro inimigo será criado, e todo o processo desse if se repete
		count = 0
		# "stop" conta quanto tempo o código levou para atingir esse ponto
	
	k = pygame.key.get_pressed() # variavel a ser usada no input de teclas mais adiante

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			rodando = False # se apertar o X da janela desativa o programa. (O rodando sendo False quebra o loop infinito)

		if e.type == pygame.KEYUP:
			if e.key == pygame.K_w:
				player.tiro_up() # se apertar W atira a flecha de cima
				#print e

			if e.key == pygame.K_s:
				player.tiro_down() # se apertar S atira a flecha de baixo
				#print e

			if e.key == pygame.K_d:
				player.tiro_right() # se apertar D atira a flecha direita
				#print e

			if e.key == pygame.K_a:
				player.tiro_left() # se apertar A atira a flecha esquerda
				#print e

	if k[K_LEFT]:
		player.rect.left -= player.velocidade # enquanto apertar a seta esquerda o personagem vai pra esquerda

	if k[K_RIGHT]:
		player.rect.right += player.velocidade # enquanto apertar a seta direita o personagem vai pra direita

	if k[K_UP]:
		player.rect.top -= player.velocidade # enquanto apertar a seta cima o personagem vai pra cima

	if k[K_DOWN]:
		player.rect.bottom += player.velocidade # enquanto apertar a seta baixo o personagem vai pra baixo
		

	if bool(inimigos) == False:
		pass
	else:
		inimigos.update(player.rect.centerx, player.rect.centery) # se existir elemento(s) no grupo de sprites dos inimigos, executa o método "update" dele(s)

	# Conferir se algum elemento do grupo flechas atinge algum elemento do grupo dos inimigos. Se acontecer, os dois elementos são apagados do jogo
	hits = pygame.sprite.groupcollide(inimigos, flechas, True, True)
	if hits:
		ponto_jogador += 1

	# Conferir se o arqueiro colide com algum monstro
	hits = pygame.sprite.spritecollide(player, inimigos, True)
	if hits:
		ponto_jogador -= 3
		#rodando = False # se colidir, o programa para. Em outras palavaras: o jogador perdeu (O rodando sendo False quebra o loop infinito)

	tela.blit(fundo,[0,0])
	if bool(inimigos) == False:
		pass
	else:
		inimigos.draw(tela) # se existir elemento(s) no grupo de sprites dos inimigos, da um blit nele(s)

	player.place(tela)
	if bool(flechas) == False:
		pass
	else:
		flechas.update() # se existir elemento(s) no grupo de sprites das flechas, executa o método "update" dele(s)

	if bool(flechas) == False:
		pass
	else:
		flechas.draw(tela) # se existir elemento(s) no grupo de sprites das flechas, da um blit nele(s)

	#label = mfonte.render("TEMPO: "+str(tempo_jogo), 1, (255,0,255))
	label2 = mfonte2.render("SEUS PONTOS: "+str(ponto_jogador), 1, (255,0,255))
	label3 = mfonte2.render("PONTOS DO OPONENTE: "+str(ponto_oponente), 1, (255,0,255))

	#tela.blit(label, [290,10])
	tela.blit(label2, [10,10])
	tela.blit(label3, [580,10])

	pygame.display.update() # atualiza toda a tela do pygame
	s.sendto(pickle.dumps(ponto_jogador), ("",5002))
	s.sendto(pickle.dumps(rodando), ("",5002))

	if rodando == True:
		ponto_oponente, addr = s.recvfrom(65535)
		ponto_oponente = pickle.loads(ponto_oponente)
		#rodando = False
		#print "Jogador: "+str(ponto_jogador)+" : "+str(ponto_oponente)+" :Oponente"

		playing, addr = s.recvfrom(65535)
		rodando = pickle.loads(playing)

	else:
		break
	

pygame.quit() # com o loop infinito quebrado, só resta ao código finalizar o pygame

