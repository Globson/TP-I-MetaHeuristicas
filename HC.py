from numpy.random import seed, rand, randn

#HC

def entre_limites(ponto, limites):
	#  Para cada linha, isto é, x e y, verificamos os intervalos.
	for d in range(len(limites)):
		# verificando se está fora dos limites 
		if ponto[d] < limites[d, 0] or ponto[d] > limites[d, 1]:
			return False
	return True

def hc(objetivo, limites, iteracoes, Tam_passo):
	# Inicialização
	ls = limites[:,1] #Limite Superior
	li = limites[:,0] #Limite Inferior
	solucao = None
	while solucao is None or not entre_limites(solucao, limites): #verificando se solucao não esta vazia ou fora dos limites
		solucao = (ls - li) * rand(len(limites)) + li #Vi = (LSi - LIi) * ri +Lii
	# Calculando valor da solucao inicial
	valor_solucao = objetivo(solucao)
	# Modificação
	for i in range(iteracoes):
		candidato = None
		while candidato is None or not entre_limites(candidato, limites): #verificando se candidato não esta vazio e dentro dos limites
			candidato = solucao + randn(len(limites)) * Tam_passo #Tamanho do passo (Pertubação)
		# Calculando valor de candidato
		valor_candidato = objetivo(candidato)
		# Verificando se candidato é melhor
		if valor_candidato <= valor_solucao:
			# Armazenando nova solução melhor
			solucao, valor_solucao = candidato, valor_candidato
			#print("-> Iteracao: ", i, " ->X:", solucao[0], " ->Y: ", solucao[1], "-> Valor:", valor_solucao)
	return [solucao, valor_solucao]
