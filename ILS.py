from numpy.random import seed, rand, randn
from numpy import pi, e, sin, sqrt, exp, asarray
from HC import entre_limites


#ILS

#Utilizando hillclimbing para busca local em ILS
def hillclimbing(objetivo, limites, iteracoes, Tam_passoHC, solucao_inicial):
	solucao = solucao_inicial
	# Calculando valor da solucao inicial
	valor_solucao = objetivo(solucao)
	# Modificação
	for i in range(iteracoes):
		candidato = None
		while candidato is None or not entre_limites(candidato, limites):
			candidato = solucao + randn(len(limites)) * Tam_passoHC #Tamanho do passo (Pertubação)
		# Calculando valor de candidato
		valor_candidato = objetivo(candidato)
		# Verificando se candidato é melhor
		if valor_candidato <= valor_solucao:
			# Armazenando nova solução melhor
			solucao, valor_solucao = candidato, valor_candidato
	return [solucao, valor_solucao]

def ils(objetivo, limites, iteracoes, Tam_passoHC, reinicios, Tam_P):
	# definindo ponto de partida inicial
	inicial = None
	li = limites[:,0]
	ls = limites[:,1]
	while inicial is None or not entre_limites(inicial, limites): #verificando se melhor não esta vazio e dentro dos limites
		inicial = (ls - li) * rand(len(limites)) + li #gerando valor inicial aleatoriamente
	# Calculando valor do ponto inicial
	#valor_inicial = objetivo(inicial)
	#encontrando melhor local para ponto de partida inicial utilizando HC
	melhor , valor_melhor = hillclimbing(objetivo, limites, iteracoes, Tam_passoHC, inicial)
	# reinicios 
	for n in range(reinicios):
		# gerando um ponto inicial de cada reinicio como uma versão perturbada do último melhor
		ponto_inicial = None
		while ponto_inicial is None or not entre_limites(ponto_inicial, limites): #verificando se candidato não esta vazio e dentro dos limites
			ponto_inicial = melhor + randn(len(limites)) * Tam_P #Pertubando 
		#Utilizando hillclimbing para busca local em ILS
		solucao, valor = hillclimbing(objetivo, limites, iteracoes, Tam_passoHC, ponto_inicial)
		# Verificando se solução encontrada é melhor que melhor atual
		if valor < valor_melhor:
			melhor, valor_melhor = solucao, valor
			#print("-> Reinicio: ",n,"-> Melhor: X =  ", melhor[0], " , Y = ", melhor[1],"-> Valor:", valor_melhor)
	return [melhor, valor_melhor]


