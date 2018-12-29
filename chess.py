#coding: utf-8
#########################################################
#	Desenvolvedor:	VITOR BRAGA DINIZ		#
# 	Programa:	Jogo de Xadrez			#
#########################################################

'''
OBS1.:  RECOMENDA-SE LER O PROGRAMA DO FIM AO INICIO

OBS2.:  O PROGRAMA SE DIVIDE EM 3 SESSÕES:  SEESÃO DE DEFINIÇÃO DO TABULEIRO, SESSÃO DAS FUNÇÕES NA QUAL OCORRERÁ O JOGO E DAS FUNÇÕES DE ANÁLISE
'''

##############################################################################################################
#---------------------------------------------INICIO DO PROGRAMA---------------------------------------------#
##############################################################################################################

import sys

'''___________________________________________SESSÃO DE DEFINIÇÃO DO TABULEIRO___________________________________________'''

##################### Declaração do estágio inicial do tabuleiro
tabuleiro =   ([['T', 'C', 'B', 'D', 'R', 'B', 'C', 'T'], 		# R ou r = REI
		['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 		# D ou d = RAINHA (DAMA)	
    		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],		# B ou b = BISPO
    		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],		# C ou c = CAVALO
    		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],		# T ou t = TORRE
    		[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],		# P ou p = PEÃO
    		['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 	######### letras minúsculas = pretas			
    		['t', 'c', 'b', 'd', 'r', 'b', 'c', 't']])	######### letras maiúsculas = brancas
##################### FIM Declaração estágio inicial do tabuleiro

#--------------------------------------------------------------------------------------------------------------------------------#
'''___________________________________________FIM DA SESSÃO DE DEFINIÇÃO DO TABULEIRO___________________________________________'''



'''___________________________________________SESSÃO 2: FUNÇÕES DE ANÁLISE___________________________________________'''


##################### Função para analisar o movimento do peao

def movimento_peao(lin_origem, col_origem, lin_chegada, col_chegada, vez):

	global tabuleiro
	t = 0	
	desloc_horiz = col_chegada - col_origem
	desloc_vert  = lin_chegada - lin_origem

	if (abs(desloc_vert) == 1):
		if   (tabuleiro[lin_chegada][col_chegada] != ' ' and desloc_horiz == 0):
			return 0
		elif (tabuleiro[lin_chegada][col_chegada] == ' ' and desloc_horiz == 1):
			return 0
		elif (desloc_horiz > 1 or desloc_horiz < -1):
			return 0
		else:
			if   (vez == "branca" and desloc_vert < 0):
				return 0
			elif (vez == "preta"  and desloc_vert > 0):
				return 0
			else:
				while ((lin_chegada == 7 or lin_chegada == 0) and t == 0):
					tabuleiro[lin_origem][col_origem] = raw_input("Promoção do Peão! Digite a peça para seu peão:\nD - para RAINHA (DAMA)\nT - para TORRE\nC - para CAVALO\nB - para BISPO\n")
					if (tabuleiro[lin_origem][col_origem] == 'd' or tabuleiro[lin_origem][col_origem] == 'D'):
						if (vez == "branca"):
							tabuleiro[lin_origem][col_origem] = 'D'
							t = 1
						else:
							tabuleiro[lin_origem][col_origem] = 'd'
							t = 1				
					if (tabuleiro[lin_origem][col_origem] == 't' or tabuleiro[lin_origem][col_origem] == 'T'):
						if (vez == "branca"):
							tabuleiro[lin_origem][col_origem] = 'T'
							t = 1
						else:
							tabuleiro[lin_origem][col_origem] = 't'
							t = 1
					if (tabuleiro[lin_origem][col_origem] == 'c' or tabuleiro[lin_origem][col_origem] == 'C'):
						if (vez == "branca"):
							tabuleiro[lin_origem][col_origem] = 'C'
							t = 1
						else:
							tabuleiro[lin_origem][col_origem] = 'c'
							t = 1
					if (tabuleiro[lin_origem][col_origem] == 'b' or tabuleiro[lin_origem][col_origem] == 'B'):
						if (vez == "branca"):
							tabuleiro[lin_origem][col_origem] = 'B'
							t = 1
						else:
							tabuleiro[lin_origem][col_origem] = 'b'
							t = 1
				return 1
	
	else:
		if (abs(desloc_vert) == 2 and tabuleiro[lin_chegada][col_chegada] == ' ' and tabuleiro[lin_chegada][col_chegada-1] == ' '):
			if   (desloc_vert < 0 and vez == "preta" and desloc_horiz == 0):
				return 1
			elif (desloc_vert > 0 and vez == "branca" and desloc_horiz == 0):
				return 1
			else:
				return 0

		else:
			return 0

##################### FIM Função para analisar o movimento do peao

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função para analisar o movimento da torre

def movimento_torre(lin_origem, col_origem, lin_chegada, col_chegada):

	global tabuleiro
	t = 1
	desloc_horiz = col_chegada - col_origem
	desloc_vert  = lin_chegada - lin_origem

	if   (desloc_horiz != 0 and desloc_vert != 0):
		return 0	
	elif (desloc_horiz != 0):
		for j in range (col_origem+1, col_chegada):
			if (tabuleiro[lin_origem][j] !=  ' '):
				return 0
		return 1
	
	else:
		for i in range (lin_origem+1, lin_chegada):
			if (tabuleiro[i][lin_origem] !=  ' '):
				return 0
		return 1
		
##################### FIM Função para analisar o movimento da torre

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função para analisar o movimento do cavalo

def movimento_cavalo(lin_origem, col_origem, lin_chegada, col_chegada, vez):

	global tabuleiro
	
	desloc_horiz = col_chegada - col_origem
	desloc_vert  = lin_chegada - lin_origem

	if ( (abs(desloc_horiz) != 2 and abs(desloc_horiz) != 1) or (abs(desloc_vert) != 2 and abs(desloc_vert) != 1) ):
		return 0

	elif (abs(desloc_horiz) == abs(desloc_vert) ):
		return 0
	else:
		return 1

##################### FIM Função para analisar o movimento do cavalo

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função para analisar o movimento do bispo

def movimento_bispo(lin_origem, col_origem, lin_chegada, col_chegada):
	global tabuleiro
	
	desloc_horiz = col_chegada - col_origem
	desloc_vert  = lin_chegada - lin_origem

	if (abs(desloc_vert) != abs(desloc_horiz)):
		return 0

	else:
		if (desloc_vert == desloc_horiz):
			if (desloc_vert > 0):
				for i in range (1, desloc_vert):
					if (tabuleiro[lin_origem + 1][col_origem + 1] !=  ' '):
						return 0
			else:
				for i in range (-1, desloc_vert, -1):
					if (tabuleiro[lin_origem + i][col_origem + i] !=  ' '):
						return 0
		else:
			if (desloc_vert > 0):
				for i in range (1, desloc_vert):
					if (tabuleiro[lin_origem + i][col_origem-i] !=  ' '):
						return 0			
			else:
				for i in range (-1, desloc_vert, -1):
					if (tabuleiro[lin_origem+i][lin_origem - i] !=  ' '):
						return 0
		return 1

##################### FIM Função para analisar o movimento do bispo

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função para analisar o movimento da rainha

def movimento_rainha(lin_origem, col_origem, lin_chegada, col_chegada):
		
	desloc_horiz = col_chegada - col_origem
	desloc_vert  = lin_chegada - lin_origem

	if   (abs(desloc_vert) == abs(desloc_horiz)):
		return movimento_bispo(lin_origem, col_origem, lin_chegada, col_chegada)
	elif (desloc_horiz == 0 or desloc_vert == 0):
		return movimento_torre(lin_origem, col_origem, lin_chegada, col_chegada)
	else:
		return 0

##################### FIM Função para analisar o movimento da rainha

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função para analisar o movimento do rei

def movimento_rei(lin_origem, col_origem, lin_chegada, col_chegada, vez):
	global tabuleiro
	
	rei_adversario = 1	#Verificador de se o rei adversário está nas casas vizinhas da casa de chegada ==> 1 = ok // 0 = não
	desloc_horiz = col_chegada - col_origem
	desloc_vert  = lin_chegada - lin_origem
	
	if (abs(desloc_vert) == 1 or abs(desloc_horiz) == 1):
		if (vez == "branca"):
			for i in range (-1, 2, 1):
				for j in range (-1, 2, 1):
					rei_adversario = rei_adversario and (tabuleiro[lin_chegada + i][col_chegada + j] != 'r')		
		else:
			for i in range (-1, 2, 1):
				for j in range (-1, 2, 1):
					rei_adversario = rei_adversario and (tabuleiro[lin_chegada + i][col_chegada + j] != 'R')
		if (rei_adversario == 1):			
			return movimento_rainha(lin_origem, col_origem, lin_chegada, col_chegada)
		else:
			return 0

	else:
		if (vez == "branca"):
			if   (tabuleiro[0][0] == 'T' and desloc_horiz == -2):         #JOGADA ESPECIAL: ROQUE
				for j in range(1,4):
					if (tabuleiro[0][j] != ' '):
						return 0
					else:
						tabuleiro[0][3] = 'T'
						tabuleiro[0][0] = ' '
						return 1
			elif (tabuleiro[0][7] =='T' and desloc_horiz == 2):
				for j in range(5,7):
					if (tabuleiro[0][j] != ' '):
						return 0
					else:
						tabuleiro[0][5] = 'T'
						tabuleiro[0][7] = ' '
						return 1
			else:
				return 0

		else:
			if   (tabuleiro[7][0] == 't' and desloc_horiz == -2):         
				for j in range(1,4):
					if (tabuleiro[7][j] != ' '):
						return 0
					else:
						tabuleiro[7][3] = 'T'
						tabuleiro[7][0] = ' '
						return 1
			elif (tabuleiro[0][7] =='T' and desloc_horiz == 2):
				for j in range(5,7):
					if (tabuleiro[7][j] != ' '):
						return 0
					else:
						tabuleiro[7][5] = 'T'
						tabuleiro[7][7] = ' '
						return 1
			else:
				return 0

			
	

##################### FIM Função para analisar o movimento do rei

#--------------------------------------------------------------------------------------------------------------------------------#


##################### Função para analisar a casa de origem da peça em movimento

def analise_origem(lin_origem, col_origem, vez): 

	global tabuleiro
	
	if   (tabuleiro[lin_origem][col_origem] == ' '):
		return 0
	elif (ord(tabuleiro[lin_origem][col_origem]) > 90  and vez == "branca"):	#ascii maior que 90 e minuscula, logo preto
		return 0
	elif (ord(tabuleiro[lin_origem][col_origem]) <= 90 and vez == "preta" ):
		return 0
	else:
		return 1

##################### FIM Função para analisar a casa de origem da peça em movimento

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função para analisar o movimento em si

def analise_movimento(lin_origem, col_origem, lin_chegada, col_chegada, vez):
	
	global tabuleiro

	if   (tabuleiro[lin_origem][col_origem] == 'p' or tabuleiro[lin_origem][col_origem] == 'P'): 
		return (movimento_peao(lin_origem, col_origem, lin_chegada, col_chegada, vez))		#ANALISA MOVIMENTO DE PEAO

	elif (tabuleiro[lin_origem][col_origem] == 't' or tabuleiro[lin_origem][col_origem] == 'T'):
		return (movimento_torre(lin_origem, col_origem, lin_chegada, col_chegada))		#ANALISA MOVIMENTO DE TORRE

	elif (tabuleiro[lin_origem][col_origem] == 'c' or tabuleiro[lin_origem][col_origem] == 'C'):
		return (movimento_cavalo(lin_origem, col_origem, lin_chegada, col_chegada, vez))       #ANALISA MOVIMENTO DE CAVALO

	elif (tabuleiro[lin_origem][col_origem] == 'b' or tabuleiro[lin_origem][col_origem] == 'B'):
		return (movimento_bispo(lin_origem, col_origem, lin_chegada, col_chegada))		#ANALISA MOVIMENTO DE BISPO

	elif (tabuleiro[lin_origem][col_origem] == 'd' or tabuleiro[lin_origem][col_origem] == 'D'):
		return (movimento_rainha(lin_origem, col_origem, lin_chegada, col_chegada))       #ANALISA MOVIMENTO DE RAINHA

	else:	
		return (movimento_rei(lin_origem, col_origem, lin_chegada, col_chegada, vez))		#ANALISA MOVIMENTO DE REI

##################### FIM Função para analisar o movimento em si

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função para analisar a casa de chegada da peça em movimento

def analise_chegada (lin_chegada, col_chegada, vez):
	
	global tabuleiro
	
	if   (tabuleiro[lin_chegada][col_chegada] == ' '):
		return 1
	elif (ord(tabuleiro[lin_chegada][col_chegada]) > 90  and vez == "branca"):	#ascii maior que 90 e minuscula, logo preto
		return 1
	elif (ord(tabuleiro[lin_chegada][col_chegada]) <= 90 and vez == "preta" ):
		return 1
	else:
		return 0


##################### FIM Função para analisar a casa de chegada da peça em movimento

'''___________________________________________FIM DA SESSÃO 2___________________________________________'''

#--------------------------------------------------------------------------------------------------------------------------------#

'''_________________________________________SESSÃO 1: FUNÇÕES NAS QUAIS OCORRE O JOGO_________________________________________'''

##################### Função para mover a peça

def mover(movimento, vez):
	global tabuleiro

	col_origem  = -1	#coluna de origem
	col_chegada = -1	#coluna de chegada
	lin_origem  = -1	#linha de origem
	lin_chegada = -1	#linha de chegada

	for i in range (0, 4, 2):			#primeiro for para track as colunas de origem e chegada
		if   (movimento[i] == 'a'): 
			if (i == 0):
				col_origem  = 0
			else: 
				col_chegada = 0
		elif (movimento[i] == 'b'): 
			if (i == 0):
				col_origem  = 1
			else: 
				col_chegada = 1
	
		elif (movimento[i] == 'c'): 
			if (i == 0):
				col_origem  = 2
			else: 
				col_chegada = 2
		elif (movimento[i] == 'd'): 
			if (i == 0):
				col_origem  = 3
			else: 
				col_chegada = 3
   
		elif (movimento[i] == 'e'): 
			if (i == 0):
				col_origem  = 4
			else: 
				col_chegada = 4
		elif (movimento[i] == 'f'): 
			if (i == 0):
				col_origem  = 5
			else: 
				col_chegada = 5
		elif (movimento[i] == 'g'): 
			if (i == 0):
				col_origem  = 6
			else: 
				col_chegada = 6
		
		elif (movimento[i] == 'h'): 
			if (i == 0):
				col_origem  = 7
			else: 
				col_chegada = 7

		else : 
			return 0
		

	for i in range (1, 4, 2):			#segundo for para track as linhas de origem e chegada
		if   (movimento[i] == '1'): 
			if (i == 1):
				lin_origem  = 0
			else: 
				lin_chegada = 0
		elif (movimento[i] == '2'): 
			if (i == 1):
				lin_origem  = 1
			else: 
				lin_chegada = 1
		elif (movimento[i] == '3'): 
			if (i == 1):
				lin_origem  = 2
			else: 
				lin_chegada = 2
		elif (movimento[i] == '4'): 
			if (i == 1):
				lin_origem  = 3
			else: 
				lin_chegada = 3   
		elif (movimento[i] == '5'): 
			if (i == 1):
				lin_origem  = 4
			else: 
				lin_chegada = 4
		elif (movimento[i] == '6'): 
			if (i == 1):
				lin_origem  = 5
			else: 
				lin_chegada = 5
		elif (movimento[i] == '7'): 
			if (i == 1):
				lin_origem  = 6
			else: 
				lin_chegada = 6	
		elif (movimento[i] == '8'): 
			if (i == 1):
				lin_origem  = 7
			else: 
				lin_chegada = 7

		else : 
			return 0

	if (lin_origem == lin_chegada and col_origem == col_chegada):
		return 0

	if (analise_origem(lin_origem, col_origem, vez) == 1): 					  
		if (analise_movimento(lin_origem, col_origem, lin_chegada, col_chegada, vez) == 1):
			if (analise_chegada (lin_chegada, col_chegada, vez) == 1):		  
				tabuleiro[lin_chegada][col_chegada] = tabuleiro[lin_origem][col_origem]
				tabuleiro[lin_origem][col_origem]   = ' ' 
				return 1
			else:
				return 0
		else:
			return 0
	else:
		return 0

##################### FIM Função para mover a peca

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função para analisar se há xeque-mate

def xequemate():
	global tabuleiro
	rei = 0
	for i in range (0,8):
		for j in range (0,8):
			if (tabuleiro[i][j] == 'R' or tabuleiro[i][j] == 'r'):
				rei += 1
	if (rei != 2):
		return True
	else:
		return False
##################### FIM Função para analisar se há xeque-mate

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função print tabuleiro na tela

def print_tabuleiro():
	global tabuleiro
	print "  - - - - - - - -"
	sys.stdout.write ("8")
	for i in range (7, -1,-1):
		for j in range (0,8):
			if (j == 0):
				sys.stdout.write ('|')
			sys.stdout.write (tabuleiro[i][j] + '|')

			if (j == 7 and i != 0):
				sys.stdout.write ("\n%d" % (i))
			if (i == 0 and j == 7):
				print " \n  - - - - - - - -"				
				print "  a b c d e f g h"

##################### FIM Função print tabuleiro na tela

#--------------------------------------------------------------------------------------------------------------------------------#

##################### Função em que ocorre o jogo

def jogo():
	
	print """\n-------------Instruções:-------------\nLetras Maiúsculas representam as peças brancas e as minúsculas, as pretas\nPara jogar basta indicar a casa de origem da peça e a casa de destino da seguinte forma: b1c3 = peça da casa b1 vai para a casa c3\nh7h5 = peça da casa h7 vai para a casa h5\na1d4 = peça da casa a1 vai para a casa d4\nOBS.: SEMPRE EM LETRAS MINÚSCULAS\n-------------------------------------\n"""

	print_tabuleiro()	

	movimento  = "null"	# Movimento da peça
	xeque_mate =  False 	# Há xeque-mate?
	vez        = "branca"	# Quem está na vez?

	while (xeque_mate == False):
		
		if (vez == "branca"): #Se a vez for das brancas
			print "Brancas:"
		else:			#senao
			print "Pretas:"
			
		movimento = raw_input()
		while (mover (movimento, vez) == 0):
			print "MOVIMENTO INVÁLIDO!"
		
			if (vez == "branca"):
				print "Brancas:"
				movimento = raw_input()
			else:
				print "pretas:"
				movimento = raw_input()
		if (vez == "branca"):
			vez = "preta"
		else:
			vez = "branca"
			
		print_tabuleiro()	
		xeque_mate = xequemate()

jogo()

##################### FIM Função em que ocorre o jogo

'''___________________________________________FIM DA SESSÃO 1___________________________________________'''


