from numpy import sin ,sqrt
from numpy.random import seed, rand, randn
from numpy import pi, e, cos, sqrt, exp, asarray
from ILS import ils, iterated_local_search, objective
from HC import hc

def func_objetivo1(x, y):
    return (sin(x+y) + pow(x-y, 2) - 1.5*x + 2.5*y + 1)


def func_objetivo2(x, y):
    return (-sin(y+47)*sin(sqrt(abs(x/2 + (y+47)))) - x*sin(sqrt(abs(x-y+47))))


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
#fazer 30 vezes para cad funcao objetivo e algoritmo, adicionar em listas correspondentes


# seed the pseudorandom number generator
seed(1)
# define range for input
bounds = asarray([[-1.5, 4], [-3, 4]])
# define the total iterations
n_iter = 1000
# define the maximum step size
s_size = 0.05
# total number of random restarts
n_restarts = 30
# perturbation step size
p_size = 1.0
# perform the hill climbing search
best, score = iterated_local_search(
    objective, bounds, n_iter, s_size, n_restarts, p_size)
print('Done!')
print('f(%s) = %f' % (best, score))
