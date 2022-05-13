'''brasil = list()
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Parana', 'sigla': 'PR'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)#Ira mostra os dois estados
print(brasil[0])#Ira mostra o estado que esta na posição zero
print(brasil[0]['uf'])#Ira mostra o estado que esta na posição zero, e sua UF'''

#Utilizando For
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())#em lista devemos utilizar a função copy para criar uma copia, e  não [:]

for e in brasil: #for para lista, assim ira imprimir o que tem em cada posição
    for k, v in e.items():#for para o dicionario pegando na posição das lista "e" a chave e o valor que está no dicionario
        print(f'{k} é {v}')