# -*- coding: utf-8 -*-

import random

import pygame

from zlib_process import zlib_compress, zlib_decompress

# Com base nas funções zlib_compress e zlib_decompress do algoritmo zlib_process (que usa a biblioteca zlib do Python), é possível a compressão da imagem de fundo do jogo



import pickle

import socket

pygame.init()

width = 800
height = 600

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

fundo = pygame.image.load("fundo.jpeg")


clock = pygame.time.Clock()

# CARREGAMENTO DE IMAGENS

rb0 = pygame.image.load("run_baixo0.png")

# frente do slime
sf0 = pygame.image.load("slime_frente0.png")
sf1 = pygame.image.load("slime_frente1.png")
sf2 = pygame.image.load("slime_frente2.png")
sf3 = pygame.image.load("slime_frente3.png")
sf4 = pygame.image.load("slime_frente4.png")
sf5 = pygame.image.load("slime_frente5.png")
sf6 = pygame.image.load("slime_frente6.png")
sf7 = pygame.image.load("slime_frente7.png")
sf8 = pygame.image.load("slime_frente8.png")
sf9 = pygame.image.load("slime_frente9.png")
sf10 = pygame.image.load("slime_frente10.png")

# costas do slime
sc0 = pygame.image.load("slime_costas0.png")
sc1 = pygame.image.load("slime_costas1.png")
sc2 = pygame.image.load("slime_costas2.png")
sc3 = pygame.image.load("slime_costas3.png")
sc4 = pygame.image.load("slime_costas4.png")
sc5 = pygame.image.load("slime_costas5.png")
sc6 = pygame.image.load("slime_costas6.png")
sc7 = pygame.image.load("slime_costas7.png")
sc8 = pygame.image.load("slime_costas8.png")
sc9 = pygame.image.load("slime_costas9.png")
sc10 = pygame.image.load("slime_costas10.png")

# correr pra baixo
rb0 = pygame.image.load("run_baixo0.png")
rb1 = pygame.image.load("run_baixo1.png")
rb2 = pygame.image.load("run_baixo2.png")
rb3 = pygame.image.load("run_baixo3.png")
rb4 = pygame.image.load("run_baixo4.png")
rb5 = pygame.image.load("run_baixo5.png")
rb6 = pygame.image.load("run_baixo6.png")
rb7 = pygame.image.load("run_baixo7.png")
rb8 = pygame.image.load("run_baixo8.png")


# correr pra cima
rc0 = pygame.image.load("run_cima0.png")
rc1 = pygame.image.load("run_cima1.png")
rc2 = pygame.image.load("run_cima2.png")
rc3 = pygame.image.load("run_cima3.png")
rc4 = pygame.image.load("run_cima4.png")
rc5 = pygame.image.load("run_cima5.png")
rc6 = pygame.image.load("run_cima6.png")
rc7 = pygame.image.load("run_cima7.png")
rc8 = pygame.image.load("run_cima8.png")


# correr para a direita
rr0 = pygame.image.load("run_right0.png")
rr1 = pygame.image.load("run_right1.png")
rr2 = pygame.image.load("run_right2.png")
rr3 = pygame.image.load("run_right3.png")
rr4 = pygame.image.load("run_right4.png")
rr5 = pygame.image.load("run_right5.png")
rr6 = pygame.image.load("run_right6.png")
rr7 = pygame.image.load("run_right7.png")
rr8 = pygame.image.load("run_right8.png")
rr9 = pygame.image.load("run_right9.png")
rr10 = pygame.image.load("run_right10.png")
rr11 = pygame.image.load("run_right11.png")


# correr para a esquerda
rl0 = pygame.image.load("run_left0.png")
rl1 = pygame.image.load("run_left1.png")
rl2 = pygame.image.load("run_left2.png")
rl3 = pygame.image.load("run_left3.png")
rl4 = pygame.image.load("run_left4.png")
rl5 = pygame.image.load("run_left5.png")
rl6 = pygame.image.load("run_left6.png")
rl7 = pygame.image.load("run_left7.png")
rl8 = pygame.image.load("run_left8.png")
rl9 = pygame.image.load("run_left9.png")
rl10 = pygame.image.load("run_left10.png")
rl11 = pygame.image.load("run_left11.png")

rl0 = pygame.image.load("run_left0.png")
rl1 = pygame.image.load("run_left1.png")
rl2 = pygame.image.load("run_left2.png")
rl3 = pygame.image.load("run_left3.png")
rl4 = pygame.image.load("run_left4.png")
rl5 = pygame.image.load("run_left5.png")
rl6 = pygame.image.load("run_left6.png")
rl7 = pygame.image.load("run_left7.png")
rl8 = pygame.image.load("run_left8.png")
rl9 = pygame.image.load("run_left9.png")
rl10 = pygame.image.load("run_left10.png")
rl11 = pygame.image.load("run_left11.png")

# correr para diagonal baixo e direita
rd_bd0 = pygame.image.load("run_baixo_direita0.png")
rd_bd1 = pygame.image.load("run_baixo_direita1.png")
rd_bd2 = pygame.image.load("run_baixo_direita2.png")
rd_bd3 = pygame.image.load("run_baixo_direita3.png")
rd_bd4 = pygame.image.load("run_baixo_direita4.png")
rd_bd5 = pygame.image.load("run_baixo_direita5.png")
rd_bd6 = pygame.image.load("run_baixo_direita6.png")
rd_bd7 = pygame.image.load("run_baixo_direita7.png")
rd_bd8 = pygame.image.load("run_baixo_direita8.png")
rd_bd9 = pygame.image.load("run_baixo_direita9.png")
rd_bd10 = pygame.image.load("run_baixo_direita10.png")
rd_bd11 = pygame.image.load("run_baixo_direita11.png")

# correr para baixo e esquerda
rd_be0 = pygame.image.load("run_baixo_esquerda0.png")
rd_be1 = pygame.image.load("run_baixo_esquerda1.png")
rd_be2 = pygame.image.load("run_baixo_esquerda2.png")
rd_be3 = pygame.image.load("run_baixo_esquerda3.png")
rd_be4 = pygame.image.load("run_baixo_esquerda4.png")
rd_be5 = pygame.image.load("run_baixo_esquerda5.png")
rd_be6 = pygame.image.load("run_baixo_esquerda6.png")
rd_be7 = pygame.image.load("run_baixo_esquerda7.png")
rd_be8 = pygame.image.load("run_baixo_esquerda8.png")
rd_be9 = pygame.image.load("run_baixo_esquerda9.png")
rd_be10 = pygame.image.load("run_baixo_esquerda10.png")
rd_be11 = pygame.image.load("run_baixo_esquerda11.png")

# LISTAS DE ANIMAÇÕES E CONTAGENS PARA ELAS

slime_frente_animacao = [sf0, sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8, sf9, sf10]



slime_costas_animacao = [sc0, sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8, sc9, sc10]



# CLASSE ARCHER À SER USADA NO BONECO DO JOGADOR
class Archer(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = rb0
		self.rect = self.image.get_rect()
		self.rect.centerx = width/2
		self.rect.centery = height/2
		self.atirando = False
		self.velocidade = 7

	def draw(self, s):
		s.blit(self.image, self.rect)

	def nao_saia_da_tela(self):
		if self.rect.left <= 0:
			self.rect.left = 0
	
		if self.rect.right >= width:
			self.rect.right = width

		if self.rect.top <=0:
			self.rect.top = 0
		
		if self.rect.bottom >= height:
			self.rect.bottom = height

		class Flecha(pygame.sprite.Sprite):
			def __init__(self, x, y, im, lado):
				pygame.sprite.Sprite.__init__(self)
				self.image = im
				self.rect = self.image.get_rect()
				self.lado_que_ela_aponta = lado
				self.rect.centery = y
				self.rect.centerx = x
				self.baixo_item_animacao = 0
				self.esquerda_item_animacao = 0
				self.direita_item_animacao = 0
				self.cima_item_animacao = 0
				self.velocidade = 7

			def update(self):
				# Para a flecha que vai para baixo:
				if self.lado_que_ela_aponta == "baixo":

					if self.baixo_item_animacao == len(flecha_baixo_animacao):
						self.baixo_item_animacao = 0

					self.image = flecha_baixo_animacao[self.baixo_item_animacao]

					self.rect.y += self.velocidade

					self.baixo_item_animacao += 1

				# Para a flecha que vai para a esquerda:
				if self.lado_que_ela_aponta == "esquerda":

					if self.esquerda_item_animacao == len(flecha_esquerda_animacao):
						self.esquerda_item_animacao = 0

					self.image = flecha_esquerda_animacao[self.esquerda_item_animacao]

					self.rect.x -= self.velocidade

					self.esquerda_item_animacao += 1

				# Para a flecha que vai para a direita:
				if self.lado_que_ela_aponta == "direita":

					if self.direita_item_animacao == len(flecha_direita_animacao):
						self.direita_item_animacao = 0

					self.image = flecha_direita_animacao[self.direita_item_animacao]

					self.rect.x += self.velocidade

					self.direita_item_animacao += 1

				# Para a flecha que vai para cima:
				if self.lado_que_ela_aponta == "cima":

					if self.cima_item_animacao == len(flecha_cima_animacao):
						self.cima_item_animacao = 0

					self.image = flecha_cima_animacao[self.cima_item_animacao]

					self.rect.y -= self.velocidade

					self.cima_item_animacao += 1

				# Se sair da tela desaparece:
				if self.rect.top > height or self.rect.bottom < 0 or self.rect.left > width or self.rect.right < 0:
					self.kill()

# CLASSE SLIME À SER USADA NOS INIMIGOS
class Slime(pygame.sprite.Sprite):
	def __init__(self, playerx, slime_centerx, slime_centery):
		pygame.sprite.Sprite.__init__(self)
		if slime_centerx <= playerx:
			self.image = sf0
		else:
			self.image = sc0
		self.rect = self.image.get_rect()
		self.rect.centerx = slime_centerx
		self.rect.centery = slime_centery
		self.item_animacao = 0
		self.lado_que_o_slime_esta_virado = "lado"
		self.velocidade = 5


	def update(self, playerx, playery):
		if self.item_animacao == len(slime_frente_animacao): # Neste if, tanto faz utilizar para a comparação o len da lista slime_frente_animacao quanto a len do slime_costas_animacao, pois ambas as listas possuem o mesmo tamanho
			self.item_animacao = 0 # Zerar o item de animação para que a animação do slime se reinicie

		if self.rect.centerx < playerx:
			self.lado_que_o_slime_esta_virado = "frente"
			self.rect.centerx += 1

		elif self.rect.centerx > playerx:
			self.lado_que_o_slime_esta_virado = "costas"
			self.rect.centerx -= 1

		if self.rect.centery > playery:
			self.rect.centery -= 1

		elif self.rect.centery < playery:
			self.rect.centery += 1

		if self.lado_que_o_slime_esta_virado == "frente":
			self.image = slime_frente_animacao[self.item_animacao]

		elif self.lado_que_o_slime_esta_virado == "costas":
			self.image = slime_costas_animacao[self.item_animacao]
			

		self.item_animacao += 1



tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Testes com imagens")
flechas = pygame.sprite.Group()
run_baixo_animacao = [rb0, rb1, rb2, rb3, rb4, rb5, rb6, rb7, rb8]

run_baixo_item = 0


run_cima_animacao = [rc0, rc1, rc2, rc3, rc4, rc5, rc6, rc7, rc8]

run_cima_item = 0


run_right_animacao = [rr0, rr1, rr2, rr3, rr4, rr5, rr6, rr7, rr8, rr9, rr10, rr11]

run_right_item = 0


run_left_animacao = [rl0, rl1, rl2, rl3, rl4, rl5, rl6, rl7, rl8, rl9, rl10, rl11]

run_left_item = 0


run_baixo_direita_animacao = [rd_bd0, rd_bd1, rd_bd2, rd_bd3, rd_bd4, rd_bd5, rd_bd6, rd_bd7, rd_bd8, rd_bd9, rd_bd10, rd_bd11]

run_baixo_direita_item = 0


run_baixo_esquerda_animacao = [rd_be0, rd_be1, rd_be2, rd_be3, rd_be4, rd_be5, rd_be6, rd_be7, rd_be8, rd_be9, rd_be10, rd_be11]

run_baixo_esquerda_item = 0

lado_que_o_boneco_do_jogador_esta_virado = "lado_que_o_boneco_do_jogador_esta_virado"

contagem_de_gerar_inimigos = 0


inimigos = pygame.sprite.Group()


player = Archer()


rodando = True

while rodando:
	clock.tick(30)
	# Input

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			rodando = False

			if e.type == pygame.KEYUP and player.atirando == False:
				if e.key == pygame.K_s:
					player.atirando = True
					player.lado_do_tiro = "baixo"

				elif e.key == pygame.K_a:
					player.atirando = True
					player.lado_do_tiro = "esquerda"

				elif e.key == pygame.K_d:
					player.atirando = True
					player.lado_do_tiro = "direita"

				elif e.key == pygame.K_w:
					player.atirando = True
					player.lado_do_tiro = "cima"

		# CHECAR SE O ARQUEIRO ESTÁ ATIRANDO UMA FLECHA
		if player.atirando == True:

			# 1. Zerar os itens de contagem das outras animações
			# 2. Exibir o frame atual da animação de tiro, especificado pelo tiro_item
			# 3. Adicionar += 1 ao tiro_item
			# 4. Se o valor de tiro_item for igual ao valor do tamanho da lista de animação de tiros, zera a contagem de animação do arqueiro atirando, cria o objeto da flecha, adiciona ela ao grupo de sprites de flechas e desabilita o estado atirando do player

			run_cima_item = 0
			run_baixo_item = 0

			run_right_item = 0
			run_left_item = 0

			run_baixo_direita_item = 0
			run_baixo_esquerda_item = 0

			run_cima_direita_item = 0
			run_cima_esquerda_item = 0

			# Jogador atirando pra baixo
			if player.lado_do_tiro == "baixo":

				player.image = tiro_baixo_animacao[
					tiro_baixo_item]  # A imagem do jogador neste frame será o item atual da lista de animação dele atirando. Neste caso, para baixo.

				tiro_baixo_item += 1  # Item aumentado para avançar para o próximo frame da animação

				# Zerar o item da animação, parar ela e gerar um objeto flecha
				if tiro_baixo_item == len(tiro_baixo_animacao):
					tiro_baixo_item = 0
					flecha = Flecha(player.rect.centerx, player.rect.centery, fb0, player.lado_do_tiro)
					flechas.add(flecha)
					player.atirando = False

			# Jogador atirando para a esquerda
			if player.lado_do_tiro == "esquerda":

				player.image = tiro_esquerda_animacao[
					tiro_esquerda_item]  # exibe o frame atual da animação de atirar para a esquerda

				if tiro_esquerda_animacao[
					tiro_esquerda_item] == te10:  # A flecha será criada assim que a animação de tiro atingir o elemento te10 da lista tiro_esquerda_animacao
					flecha = Flecha(player.rect.centerx, player.rect.centery, fl0, player.lado_do_tiro)
					flechas.add(flecha)

				tiro_esquerda_item += 1

				if tiro_esquerda_item == len(tiro_esquerda_animacao):
					tiro_esquerda_item = 0
					player.atirando = False

			# Jogador atirando para a direita
			if player.lado_do_tiro == "direita":

				player.image = tiro_direita_animacao[tiro_direita_item]

				if tiro_direita_animacao[tiro_direita_item] == td11:
					flecha = Flecha(player.rect.centerx, player.rect.centery, fd0, player.lado_do_tiro)
					flechas.add(flecha)

				tiro_direita_item += 1

				if tiro_direita_item == len(tiro_direita_animacao):
					tiro_direita_item = 0
					player.atirando = False

			# Jogador atirando para cima
			if player.lado_do_tiro == "cima":

				player.image = tiro_cima_animacao[tiro_cima_item]

				tiro_cima_item += 1

				if tiro_cima_item == len(tiro_cima_animacao):
					tiro_cima_item = 0
					flecha = Flecha(player.rect.centerx, player.rect.centery, fc0, player.lado_do_tiro)
					flechas.add(flecha)
					player.atirando = False

	kp = pygame.key.get_pressed()

	botoes_usados_no_jogo = (kp[pygame.K_UP], kp[pygame.K_DOWN], kp[pygame.K_RIGHT], kp[pygame.K_LEFT])
	# Update

	if not any(botoes_usados_no_jogo):  # se nenhum dos botoes usados no jogo forem pressionados

		run_cima_item = 0
		run_baixo_item = 0

		if lado_que_o_boneco_do_jogador_esta_virado == "cima":
			# Inserir aqui os códigos para animação idle para cima
			player.image = rc0

		elif lado_que_o_boneco_do_jogador_esta_virado == "baixo":
			# Inserir aqui os códigos para animação idle para baixo
			player.image = rb0

		elif lado_que_o_boneco_do_jogador_esta_virado == "direito":
			# Inserir aqui os códigos para animação idle para direita
			player.image = rr0

		elif lado_que_o_boneco_do_jogador_esta_virado == "esquerdo":
			# Inserir aqui os códigos para animação idle para esquerda
			player.image = rl0

		# os dois elifs comentados abaixo não funcionam, pois a variável "lado_que_o_boneco_do_jogador_esta_virado" nunca recebe os valores "baixo_direita" e "baixo_esquerda" nessa sessão. Provavelmente por uma questão de frames

		# elif lado_que_o_boneco_do_jogador_esta_virado == "baixo_direita":
		# player.image = rd_bd0

		# elif lado_que_o_boneco_do_jogador_esta_virado == "baixo_esquerda":
		# player.image = rd_be0


	else:
		# zerar o item e o count das animacoes idle

		# Ciclo básico:

		# 1. Zerar as contagens das outras animações
		# 2. Zerar a contagem da animação atual, caso o valor atual dela for igual ao tamanho da lista da animação atual
		# 3. Mudar a imagem do jogador de acordo com o elemento da lista da animação atual especificado pelo valor atual da contagem de animação
		# 4. Alterar a posição do rect do boneco do jogador
		# 5. Adicionar +1 à contagem de animação
		# 6. Registrar na variável "lado_que_o_boneco_do_jogador_esta_virado" uma string que indica para qual direção o jogador estava virado naquele momento

		# DIAGONAIS:

		# BAIXO E DIREITA
		if kp[pygame.K_DOWN] and kp[pygame.K_RIGHT]:

			run_cima_item = 0
			run_baixo_item = 0

			run_right_item = 0
			run_left_item = 0

			run_baixo_esquerda_item = 0

			if run_baixo_direita_item == len(run_baixo_direita_animacao):
				run_baixo_direita_item = 0

			player.image = run_baixo_direita_animacao[run_baixo_direita_item]

			player.rect.y += player.velocidade
			player.rect.x += player.velocidade

			run_baixo_direita_item += 1

			lado_que_o_boneco_do_jogador_esta_virado = "baixo_direita"

		# BAIXO E ESQUERDA
		elif kp[pygame.K_DOWN] and kp[pygame.K_LEFT]:

			run_cima_item = 0
			run_baixo_item = 0

			run_right_item = 0
			run_left_item = 0

			run_baixo_direita_item = 0

			if run_baixo_esquerda_item == len(run_baixo_esquerda_animacao):
				run_baixo_esquerda_item = 0

			player.image = run_baixo_esquerda_animacao[run_baixo_esquerda_item]

			player.rect.y += player.velocidade
			player.rect.x -= player.velocidade

			run_baixo_esquerda_item += 1

			lado_que_o_boneco_do_jogador_esta_virado = "baixo_esquerda"


		# LADOS:


		# CIMA
		elif kp[pygame.K_UP]:

			run_baixo_item = 0

			run_right_item = 0
			run_left_item = 0

			run_baixo_direita_item = 0
			run_baixo_esquerda_item = 0

			if run_cima_item == len(run_cima_animacao):
				run_cima_item = 0

			player.image = run_cima_animacao[run_cima_item]

			player.rect.y -= player.velocidade

			run_cima_item += 1

			lado_que_o_boneco_do_jogador_esta_virado = "cima"


		# BAIXO
		elif kp[pygame.K_DOWN]:

			run_cima_item = 0

			run_right_item = 0
			run_left_item = 0

			run_baixo_direita_item = 0
			run_baixo_esquerda_item = 0

			if run_baixo_item == len(run_baixo_animacao):
				run_baixo_item = 0

			player.image = run_baixo_animacao[run_baixo_item]

			player.rect.y += player.velocidade

			run_baixo_item += 1

			lado_que_o_boneco_do_jogador_esta_virado = "baixo"


		# DIREITA
		elif kp[pygame.K_RIGHT]:

			run_cima_item = 0
			run_baixo_item = 0

			run_left_item = 0

			run_baixo_direita_item = 0
			run_baixo_esquerda_item = 0

			if run_right_item == len(run_right_animacao):
				run_right_item = 0

			player.image = run_right_animacao[run_right_item]

			player.rect.x += player.velocidade

			run_right_item += 1

			lado_que_o_boneco_do_jogador_esta_virado = "direito"


		# ESQUERDA
		elif kp[pygame.K_LEFT]:

			run_cima_item = 0
			run_baixo_item = 0

			run_right_item = 0

			run_baixo_direita_item = 0
			run_baixo_esquerda_item = 0

			if run_left_item == len(run_left_animacao):
				run_left_item = 0

			player.image = run_left_animacao[run_left_item]

			player.rect.x -= player.velocidade

			run_left_item += 1

			lado_que_o_boneco_do_jogador_esta_virado = "esquerdo"

	contagem_de_gerar_inimigos += 1

	# GERAÇÃO DE INIMIGOS
	if contagem_de_gerar_inimigos == 100:
		take = random.randint(1,4)
		if take == 1:
			inimigo = Slime(player.rect.x, -6, random.randrange(0, height)) # Da esquerda

		elif take == 2:
			inimigo = Slime(player.rect.x, random.randrange(0, width), -6) # De cima

		elif take == 3:
			inimigo = Slime(player.rect.x, width+6, random.randrange(0, height)) # Da direita

		elif take == 4:
			inimigo = Slime(player.rect.x, random.randrange(0, width), height+6) # De baixo

		inimigos.add(inimigo)

		contagem_de_gerar_inimigos = 0

	flechas.update()
	inimigos.update(player.rect.centerx, player.rect.centery)

	hits = pygame.sprite.spritecollide(player, inimigos, True)

	pygame.display.update()

	# Draw
	tela.blit(fundo, [0,0]) # Preencher a tela de preto
	player.draw(tela)
	flechas.draw(tela)
	inimigos.draw(tela)


zlib_compress("fundo.jpeg")  # Comprime a imagem de fundo




