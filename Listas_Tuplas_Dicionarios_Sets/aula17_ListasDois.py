#Criando utilizando Range: cria uma estrutura ordenada
valores = list(range(0, 10))
print(valores)
print('\n', '-=-'* 20)


valoresDois = [] #criei uma lista vazia
valoresDois.append(9) #posição 0 adicioneio o 9
valoresDois.append(15) #posição 1 adicionei o 15
valoresDois.append(7)

for valor in valoresDois: #(para cada valor em valores)
    print(f'{valor}...', end='')

print('\n', '-=-'* 20)

for pos, valor in enumerate(valoresDois): #enumerate ira pegar a posição e quem está naquela posição
    print(f'Na {pos} temos o valor {valor}')

print('\n', '-=-'* 20)

lista = ['Jonas', 'Nathalia', 'Teka', 'Pele', 'Lelo']
for pos, pessoa in enumerate(lista):
    print(f'Na posição {pos} temos alocado a variavel {pessoa}')
print('\n', '-=-'* 20)


#Adicionando valores a lista pelo For
numeros = list()

for pos in range(0, 5):
    numeros.append(int(input('Digite os numeros: ')))

for pos, var in enumerate(numeros):
    print(f'Na posição {pos} temos o valor {var}')



