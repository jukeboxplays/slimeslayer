# -*- coding: utf-8 -*-

import pygame
pygame.init()

width = 800
height = 600

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

clock = pygame.time.Clock()

# CARREGAMENTO DE IMAGENS

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


# CLASSE ARCHER À SER USADA NO BONECO DO JOGADOR
class Archer(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = rb0
		self.rect = self.image.get_rect()
		self.rect.centerx = width/2
		self.rect.centery = height/2
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




tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Testes com imagens")


# LISTAS DE ANIMAÇÕES E CONTAGENS PARA ELAS

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


# VARIÁVEL ONDE ESTARÁ O BONECO QUE O JOGADOR IRÁ CONTROLAR
player = Archer()


lado_que_o_boneco_do_jogador_esta_virado = "lado_que_o_boneco_do_jogador_esta_virado"


rodando = True

while rodando:
	
	clock.tick(30)

	# Input

	eventos_do_pygame = pygame.event.get()

	for e in eventos_do_pygame:
		if e.type == pygame.QUIT:
			rodando = False


	kp = pygame.key.get_pressed()

	botoes_usados_no_jogo = (kp[pygame.K_UP], kp[pygame.K_DOWN], kp[pygame.K_RIGHT], kp[pygame.K_LEFT]) 
	# Esta pequena tupla foi criada com o intuito de fazer com q o num lock ligado não interferisse mais no código :)



	# MOVIMENTAÇÃO DO PERSONAGEM DO JOGADOR

	if not any(botoes_usados_no_jogo): #se nenhum dos botoes usados no jogo forem pressionados

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

		#elif lado_que_o_boneco_do_jogador_esta_virado == "baixo_direita":
			#player.image = rd_bd0

		#elif lado_que_o_boneco_do_jogador_esta_virado == "baixo_esquerda":
			#player.image = rd_be0


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
			
			


	# Update
	player.nao_saia_da_tela()
	pygame.display.update()
	# Render/Draw
	tela.fill(black)
	player.draw(tela)

pygame.quit()
