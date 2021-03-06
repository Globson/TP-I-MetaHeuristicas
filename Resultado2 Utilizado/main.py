'''
Samuel Pedro Campos Sena - EF3494
Trabalho prático 1 - CCF480 - MetaHeurísticas
'''

'''
numpy.random.randn gera amostras a partir da distribuição normal, 
enquanto numpy.random.rand a partir de uma distribuição uniforme (no intervalo [0,1)).
'''
import matplotlib.pyplot as plt
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
seed()

# definindo limites
limites1a = asarray([[-1.5, 4.], 
                    [-3., 4.]])

limites1b = asarray([[-1., 0.],
                     [-2., -1.]])

limites2c = asarray([[-512., 512.],
                     [-512., 512.]])  

limites2d = asarray([[511., 512.],
                     [404., 405.]])
# Definindo quantidade de iterações
iteracoes = 1000

# Definindo tamanho do passo (pertubação) para HC
Tam_passoHC = 0.05

# Quantidade de reinicios em ILS (tentativa de buscas em novas bacias)
reinicios = 50

# Tamanho da pertubacao do ILS
Tam_P = 0.5

'''
melhor, valor = ils(objetivo1, limites1a, iteracoes, Tam_passoHC, reinicios, Tam_P)
print("ILS: X: ",melhor[0]," Y: ",melhor[1]," = ",valor)
melhor, valor = hc(objetivo1, limites1a, iteracoes, Tam_passoHC)
print("HC: X: ",melhor[0]," Y: ",melhor[1]," = ",valor)
'''
archive = open('Resultados.txt', 'w')
archive.write("\nConfiguracoes:")
archive.write("\nIteracoes no HC: " + str(iteracoes))
archive.write("\nTamanho do passo no HC: " + str(Tam_passoHC))
archive.write("\nQuantidade de reinicios no ILS: " + str(reinicios))
archive.write("\nTamanho da pertubação no ILS: " + str(Tam_P))
archive.write("\n\nRealizando 30 iteracoes dos algoritmos...")
print("Configuracoes:")
print("Iteracoes no HC: ", iteracoes)
print("Tamanho do passo no HC: ",Tam_passoHC)
print("Quantidade de reinicios no ILS: ", reinicios)
print("Tamanho da pertubação no ILS: ", Tam_P)
print("\nRealizando 30 iteracoes dos algoritmos...")
for i in range(30):
    _ , valor = ils(objetivo1, limites1a, iteracoes, Tam_passoHC, reinicios, Tam_P)
    Resultados1A_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo1, limites1a, iteracoes, Tam_passoHC)   
    Resultados1A_HC.append(valor)
    _ , valor = ils(objetivo1, limites1b, iteracoes, Tam_passoHC, reinicios, Tam_P)
    Resultados1B_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo1, limites1b, iteracoes, Tam_passoHC)   
    Resultados1B_HC.append(valor)
    _ , valor = ils(objetivo2, limites2c, iteracoes, Tam_passoHC, reinicios, Tam_P)
    Resultados2C_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo2, limites2c, iteracoes, Tam_passoHC)   
    Resultados2C_HC.append(valor)
    _ , valor = ils(objetivo2, limites2d, iteracoes, Tam_passoHC, reinicios, Tam_P)
    Resultados2D_ILS.append(valor)
    _ , valor = melhor, valor = hc(objetivo2, limites2d, iteracoes, Tam_passoHC)   
    Resultados2D_HC.append(valor)
archive.write("\n----------------------")
archive.write("\n1 - a)")
archive.write("\nHC: ")
archive.write("\nMin: " + str(min(Resultados1A_HC)))
archive.write("\nMax: " + str(max(Resultados1A_HC)))
archive.write("\nStd: " + str(std(Resultados1A_HC)))
archive.write("\nMedia: " + str(mean(Resultados1A_HC)))
print("1 - a)")
print("HC: ")
print("Min: ",min(Resultados1A_HC))
print("Max: ",max(Resultados1A_HC))
print("Std: ",std(Resultados1A_HC))
print("Media: ",mean(Resultados1A_HC))
plt.boxplot(Resultados1A_HC)
plt.title("Resultado 1 a) - HC")
plt.savefig('plots/1A_HC.png', format='png')
#plt.show()

archive.write("\n\nILS: ")
archive.write("\nMin: " + str(min(Resultados1A_ILS)))
archive.write("\nMax: " + str(max(Resultados1A_ILS)))
archive.write("\nStd: " + str(std(Resultados1A_ILS)))
archive.write("\nMedia: " + str(mean(Resultados1A_ILS)))
archive.write("\n----------------------")
print("ILS: ")
print("Min: ", min(Resultados1A_ILS))
print("Max: ", max(Resultados1A_ILS))
print("Std: ", std(Resultados1A_ILS))
print("Media: ", mean(Resultados1A_ILS))
plt.clf()
plt.boxplot(Resultados1A_ILS)
plt.title("Resultado 1 a) - ILS")
plt.savefig('plots/1A_ILS.png', format='png')
#plt.show()


archive.write("\n1 - b)")
archive.write("\nHC: ")
archive.write("\nMin: " + str(min(Resultados1B_HC)))
archive.write("\nMax: " + str(max(Resultados1B_HC)))
archive.write("\nStd: " + str(std(Resultados1B_HC)))
archive.write("\nMedia: " + str(mean(Resultados1B_HC)))
print("1 - b)")
print("HC: ")
print("Min: ",min(Resultados1B_HC))
print("Max: ",max(Resultados1B_HC))
print("Std: ",std(Resultados1B_HC))
print("Media: ",mean(Resultados1B_HC))
plt.clf()
plt.boxplot(Resultados1B_HC)
plt.title("Resultado 1 b) - HC")
plt.savefig('plots/1B_HC.png', format='png')
#plt.show()

archive.write("\n\nILS: ")
archive.write("\nMin: " + str(min(Resultados1B_ILS)))
archive.write("\nMax: " + str(max(Resultados1B_ILS)))
archive.write("\nStd: " + str(std(Resultados1B_ILS)))
archive.write("\nMedia: " + str(mean(Resultados1B_ILS)))
archive.write("\n----------------------")
print("ILS: ")
print("Min: ", min(Resultados1B_ILS))
print("Max: ", max(Resultados1B_ILS))
print("Std: ", std(Resultados1B_ILS))
print("Media: ", mean(Resultados1B_ILS))
plt.clf()
plt.boxplot(Resultados1B_ILS)
plt.title("Resultado 1 b) - ILS")
plt.savefig('plots/1B_ILS.png', format='png')
#plt.show()

archive.write("\n2 - c)")
archive.write("\nHC: ")
archive.write("\nMin: " + str(min(Resultados2C_HC)))
archive.write("\nMax: " + str(max(Resultados2C_HC)))
archive.write("\nStd: " + str(std(Resultados2C_HC)))
archive.write("\nMedia: " + str(mean(Resultados2C_HC)))
print("2 - c)")
print("HC: ")
print("Min: ",min(Resultados2C_HC))
print("Max: ",max(Resultados2C_HC))
print("Std: ",std(Resultados2C_HC))
print("Media: ",mean(Resultados2C_HC))
plt.clf()
plt.boxplot(Resultados2C_HC)
plt.title("Resultado 2 c) - HC")
plt.savefig('plots/2C_HC.png', format='png')
#plt.show()

archive.write("\n\nILS: ")
archive.write("\nMin: " + str(min(Resultados2C_ILS)))
archive.write("\nMax: " + str(max(Resultados2C_ILS)))
archive.write("\nStd: " + str(std(Resultados2C_ILS)))
archive.write("\nMedia: " + str(mean(Resultados2C_ILS)))
archive.write("\n----------------------")
print("ILS: ")
print("Min: ", min(Resultados2C_ILS))
print("Max: ", max(Resultados2C_ILS))
print("Std: ", std(Resultados2C_ILS))
print("Media: ", mean(Resultados2C_ILS))
plt.clf()
plt.boxplot(Resultados2C_ILS)
plt.title("Resultado 2 c) - ILS")
plt.savefig('plots/2C_ILS.png', format='png')
#plt.show()


archive.write("\n2 - d)")
archive.write("\nHC: ")
archive.write("\nMin: " + str(min(Resultados2D_HC)))
archive.write("\nMax: " + str(max(Resultados2D_HC)))
archive.write("\nStd: " + str(std(Resultados2D_HC)))
archive.write("\nMedia: " + str(mean(Resultados2D_HC)))
print("2 - d)")
print("HC: ")
print("Min: ",min(Resultados2D_HC))
print("Max: ",max(Resultados2D_HC))
print("Std: ",std(Resultados2D_HC))
print("Media: ",mean(Resultados2D_HC))
plt.clf()
plt.boxplot(Resultados2D_HC)
plt.title("Resultado 2 d) - HC")
plt.savefig('plots/2D_HC.png', format='png')
#plt.show()

archive.write("\n\nILS: ")
archive.write("\nMin: " + str(min(Resultados2D_ILS)))
archive.write("\nMax: " + str(max(Resultados2D_ILS)))
archive.write("\nStd: " + str(std(Resultados2D_ILS)))
archive.write("\nMedia: " + str(mean(Resultados2D_ILS)))
archive.write("\n----------------------")
print("ILS: ")
print("Min: ", min(Resultados2D_ILS))
print("Max: ", max(Resultados2D_ILS))
print("Std: ", std(Resultados2D_ILS))
print("Media: ", mean(Resultados2D_ILS))
plt.clf()
plt.boxplot(Resultados2D_ILS)
plt.title("Resultado 2 d) - ILS")
plt.savefig('plots/2D_ILS.png', format='png')
#plt.show()
archive.close()

'''
print(Resultados1A_HC)
print(Resultados1A_ILS)
print(Resultados1B_HC)
print(Resultados1B_ILS)
print(Resultados2C_HC)
print(Resultados2C_ILS)
print(Resultados2D_HC)
print(Resultados2D_ILS)
'''
