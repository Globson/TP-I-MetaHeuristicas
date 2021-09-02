from numpy.random import seed, rand, randn

#HC

def entre_limites(ponto, limites):
	# enumerando as dimensões do array de limites
	for d in range(len(limites)):
		# verificando se está fora dos limites para a dimensão d
		if ponto[d] < limites[d, 0] or ponto[d] > limites[d, 1]:
			return False
	return True

def hc(objetivo, limites, iteracoes, step_size):
	# Inicialização
	solucao = None
	while solucao is None or not entre_limites(solucao, limites):
		solucao = (limites[:, 1] - limites[:, 0]) * rand(len(limites)) + limites[:, 0]
	# Calculando valor da solucao inicial
	valor_solucao = objetivo(solucao)
	# Modificação
	for i in range(iteracoes):
		# take a step
		candidato = None
		while candidato is None or not entre_limites(candidato, limites):
			candidato = solucao + randn(len(limites)) * step_size
		# Calculando valor de candidato
		valor_candidato = objetivo(candidato)
		# Verificando se candidato é melhor
		if valor_candidato <= valor_solucao:
			# Armazenando novas soluções
			solucao, valor_solucao = candidato, valor_candidato
			#print("-> Iteracao: ", i, " ->X:", solucao[0], " ->Y: ", solucao[1], "-> Valor:", valor_solucao)
	return [solucao, valor_solucao]
