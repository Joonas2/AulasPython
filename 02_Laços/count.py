'''Count -gera um contador infinito, que e um iterador '''

from itertools import count

contador = count() #gera um contador que inicia em 0
print(next(contador))

'''Count e um contador infinito, entao no for seguinte, ele nao ira parar'''
for valor in contador:
    print(valor, end=' ')

    if valor > 19:
        print()
        break
    '''forma de parar o count'''
print('-=-' * 20)

'''Star = qual valor o contador deve iniciar, step = passos do contador'''
contadorDois = count(start=5, step=2) # ira comecar no valor 5 e pular de dois em dois
for valor in contadorDois:
    print(valor, end=' ')

    if valor > 19:
        print()
        break
print('-=' * 20)

contadorTres = count(start=5, step=0.5)# ira comecar no valor 5 e pular de dois em dois
for valor in contadorTres:
    print(round(valor, 2), end=' - ') #round irá arredondar os valores

    if valor > 10:
        print()
        break

