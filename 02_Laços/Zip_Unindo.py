'''Zip - unindo iteraveis'''

estados = ['RS', 'SC', 'PR', 'SP']
cidades = ['Porto Alegre', 'Floripa', 'Cascavel', 'Santos']

#Zip ira unir as duas listas, criando um iterador
brasil = zip(estados, cidades)

'''Podemos tentar imprimir brasil, porem brasil nao e uma lista, mas podemos tranforma-la em uma lista, ou dicionario'''
#print(list(brasil))
#print(dict(brasil))

'''Como tambem podemos unir a lista, ja passando para dicionario '''
br = dict(zip(estados, cidades)) #estados = key, cidades = values
print(br)
print('-=' * 20)

'''Somandos numeros de duas listas'''
a = [1, 2, 3, 4, 5, 6]
b = [9, 8, 7, 6, 4, 5]

unindo = list(zip(a, b))

soma = [x + y for x, y in zip(a, b)]
print(unindo)
print(soma)


