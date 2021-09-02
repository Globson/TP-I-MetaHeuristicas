'''
Samuel Pedro Campos Sena - EF3494
Trabalho prático 1 - CCF480 - MetaHeurísticas
'''
from numpy.random import seed, rand, randn
from numpy import sin, sqrt, asarray, mean, std
from ILS import ils
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
Resultados2C_ILS = []
Resultados2C_HC = []
Resultados2D_ILS = []
Resultados2D_HC = []
#fazer 30 vezes para cada funcao objetivo e algoritmo, adicionar em listas correspondentes


# adicionando seed de gerador rand
seed(1)

# definindo limites
limites1a = asarray([[-1.5, 4.], 
                    [-3., 4.]])

limites1b = asarray([[-1., 0.],
                     [-2., -1.]])

limites2c = asarray([[-512., 512.],
                     [-512., 512.]])  

limites2d = asarray([[511., 512.],
                     [404., 405.]])
# define the total iterations
iteracoes = 1000

# define the maximum step size
step_size = 1

# Quantidade de reinicios aleatorios
reinicios = 30

# Tamanho da pertubacao
Tam_P = 1.0 #padrao

# perform the hill climbing search
melhor, valor = ils(objetivo2, limites2c, iteracoes, step_size, reinicios, Tam_P)
print('Sucesso!')
print('ILS: X: %f Y: %f = %f' % (melhor[0], melhor[1], valor))
melhor, valor = hc(objetivo2, limites2c, iteracoes, step_size)
print('HC: X: %f Y: %f = %f' % (melhor[0],melhor[1], valor))

'''
for i in range(30):
    _ , valor = iterated_local_search(objetivo1, limites1a, iteracoes, step_size, reinicios, Tam_P)
    Resultados1A_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo1, limites1a, iteracoes, step_size)   
    Resultados1A_HC.append(valor)
    _ , valor = iterated_local_search(objetivo1, limites1b, iteracoes, step_size, reinicios, Tam_P)
    Resultados1B_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo1, limites1b, iteracoes, step_size)   
    Resultados1B_HC.append(valor)
    _ , valor = iterated_local_search(objetivo2, limites2c, iteracoes, step_size, reinicios, Tam_P)
    Resultados2C_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo2, limites2c, iteracoes, step_size)   
    Resultados2C_HC.append(valor)
    _ , valor = iterated_local_search(objetivo2, limites2d, iteracoes, step_size, reinicios, Tam_P)
    Resultados2D_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo2, limites2d, iteracoes, step_size)   
    Resultados2D_HC.append(valor)

print("1 - a)")
print("HC: ")
print("Min: ",min(Resultados1A_HC))
print("Max: ",max(Resultados1A_HC))
print("Std: ",std(Resultados1A_HC))
print("Media: ",mean(Resultados1A_HC))
print("ILS: ")
print("Min: ", min(Resultados1A_ILS))
print("Max: ", max(Resultados1A_ILS))
print("Std: ", std(Resultados1A_ILS))
print("Media: ", mean(Resultados1A_ILS))

print("1 - b)")
print("HC: ")
print("Min: ",min(Resultados1B_HC))
print("Max: ",max(Resultados1B_HC))
print("Std: ",std(Resultados1B_HC))
print("Media: ",mean(Resultados1B_HC))
print("ILS: ")
print("Min: ", min(Resultados1B_ILS))
print("Max: ", max(Resultados1B_ILS))
print("Std: ", std(Resultados1B_ILS))
print("Media: ", mean(Resultados1B_ILS))

print("2 - c)")
print("HC: ")
print("Min: ",min(Resultados2C_HC))
print("Max: ",max(Resultados2C_HC))
print("Std: ",std(Resultados2C_HC))
print("Media: ",mean(Resultados2C_HC))
print("ILS: ")
print("Min: ", min(Resultados2C_ILS))
print("Max: ", max(Resultados2C_ILS))
print("Std: ", std(Resultados2C_ILS))
print("Media: ", mean(Resultados2C_ILS))

print("2 - d)")
print("HC: ")
print("Min: ",min(Resultados2D_HC))
print("Max: ",max(Resultados2D_HC))
print("Std: ",std(Resultados2D_HC))
print("Media: ",mean(Resultados2D_HC))
print("ILS: ")
print("Min: ", min(Resultados2D_ILS))
print("Max: ", max(Resultados2D_ILS))
print("Std: ", std(Resultados2D_ILS))
print("Media: ", mean(Resultados2D_ILS))
'''