from numpy.random import seed, rand, randn
from numpy import pi, e, sin, sqrt, exp, asarray
from HC import entre_limites

def ils():
    return


#ILS

# Funcao objetivo
def objetivo(v):
	x, y = v
	return (sin(x+y) + pow(x-y, 2) - 1.5*x + 2.5*y + 1)


def hillclimbing(objetivo, limites, iteracoes, step_size, solucao_inicial):
	# Armazenando solucao inicial em variavel
	solucao = solucao_inicial
	# Calculando valor da solucao inicial
	valor_solucao = objetivo(solucao)
	# executando hillclimbing
	for i in range(iteracoes):
		# take a step
		candidato = None
		while candidato is None or not entre_limites(candidato, limites):
			candidato = solucao + randn(len(limites)) * step_size
		# Calculando valor de candidato
		valor_candidato = objetivo(candidato)
		# Verificando se candidato é melhor
		if valor_candidato <= valor_solucao:
			# Armazene novas soluções
			solucao, valor_solucao = candidato, valor_candidato
	return [solucao, valor_solucao]

# iterated local search algorithm

def iterated_local_search(objetivo, limites, n_iter, step_size, reinicios, p_size):
	# definindo ponto de partida
	melhor = None
	while melhor is None or not entre_limites(melhor, limites):
		melhor = limites[:, 0] + rand(len(limites)) * (limites[:, 1] - limites[:, 0])
	# Calculando valor do ponto inicial
	valor_melhor = objetivo(melhor)
	# Enumerando reinicios 
	for n in range(reinicios):
		# gerando um ponto inicial como uma versão perturbada do último melhor
		start_pt = None
		while start_pt is None or not entre_limites(start_pt, limites):
			start_pt = melhor + randn(len(limites)) * p_size
		# perform a stochastic hill climbing search
		solucao, valor_solucao_encontrada = hillclimbing(objetivo, limites, n_iter, step_size, start_pt)
		# Verificando se solução encontrada é melhor que melhor atual
		if valor_solucao_encontrada < valor_melhor:
			melhor, valor_melhor = solucao, valor_solucao_encontrada
			#print("-> Reinicio: ",n,"-> Melhor: X =  ", melhor[0], " , Y = ", melhor[1],"-> Valor:", valor_melhor)
	return [melhor, valor_melhor]


