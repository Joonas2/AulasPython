#Listas compostas: Listas dentro de listas.
#Criei uma lista e adicionei os dados
dados = list()
dados.append('Pedro')
dados.append(25)

#criei um outra lista que vai receber a lista dados e adicionar no seu primeiro espaço de memoria
pessoa = list()
pessoa.append(dados)
print(pessoa)

print(pessoa[0][1])

galera = [['Jonas', 19], ['Luiz', 27], ['Camila', 17]]
print(galera[0][1])# na posição zero [Jonas, 19], mostre quem esta na posição da posição 1 = 19

teste = list()
teste.append(galera)
galera[0][0] = 'Luiz'
print(teste)

