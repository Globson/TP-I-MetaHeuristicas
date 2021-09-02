'''
Samuel Pedro Campos Sena - EF3494
Trabalho prático 1 - CCF480 - MetaHeurísticas
'''
from numpy.random import seed, rand, randn
from numpy import sin, sqrt, asarray
from ILS import ils, iterated_local_search, objetivo
from HC import hc

def objetivo1(v):
    x, y = v
    return (sin(x+y) + pow(x-y, 2) - 1.5*x + 2.5*y + 1)


def objetivo2(v):
    x, y = v
    return (-(y+47)*sin(sqrt(abs(x/2 + (y+47)))) - x*sin(sqrt(abs(x-y+47))))


#1
#a) -1.5<=x<=4 e -3<=y<=4
#b) -1<=x<=0 e -2<=y<=-1
Resultados1A_ILS = []
Resultados1A_HC = []
Resultados1B_ILS = []
Resultados1B_HC = []
#2
#a) -512<=x,y<=512
#b) 511<=x<=512 e 404<=y<=405
Resultados2A_ILS = []
Resultados2A_HC = []
Resultados2B_ILS = []
Resultados2B_HC = []
#fazer 30 vezes para cada funcao objetivo e algoritmo, adicionar em listas correspondentes


# adicionando seed de gerador rand
seed(1)

# define range for input
limites = asarray([[-1.5, 4], 
                    [-3, 4]])

# define the total iterations
iteracoes = 1000

# define the maximum step size
step_size = 0.05

# Quantidade de reinicios aleatorios
reinicios = 30

# perturbation step size
p_size = 1.0

# perform the hill climbing search
melhor, valor = iterated_local_search(objetivo, limites, iteracoes, step_size, reinicios, p_size)
print('Sucesso!')
print('ILS: X: %f Y: %f = %f' % (melhor[0], melhor[1], valor))
melhor, valor = hc(objetivo, limites, iteracoes, step_size)
print('HC: X: %f Y: %f = %f' % (melhor[0],melhor[1], valor))
