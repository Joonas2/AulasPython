#listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
#listas = []
#listas são mutaveis

lanche = ['Hamburguer', 'Suco', 'Pizza', 'pudin']
print(lanche)

#Dessa forma, ira substituir o que ta na posição 3 e colocar picole nela
lanche[3] = 'picole'
print(lanche)

#append = ira adicionar uma variavel a mais, na ultima poscição
lanche.append('Biscoito')
print(lanche)

#insert = passamos a posição que queremos adicionar, e ele vai colocar nela, empurando as outras varaveias para o lado
lanche.insert(0, 'dog')
print(lanche)

#ira organizar a lista em ordem alfabetica, numerica
lanche.sort()
lanche.sort(reverse=True) #Ira organiza a lista de tras para frente

#Apagar elementos
#del lanche[3] #ira apagar a variavel na posição passada
print(lanche)

lanche.pop() #pode ser utilizado para apagar o ultimo elemrnto da lista
lanche.pop(3) #mesma função do del

lanche.remove('Suco') #ira remover o parametro passado pelo nome, e ira mover a outras variaveis mudando elas de posição,
# quem tava na posição depois do suco, vai para posição do suco

print('-=-'*20)

#Conjuntos
listaA = [2, 3, 4, 5]
listaB = listaA #aqui B esta recebendo os valores de A
print(listaA)
print(listaB)
print('\n', '-=-'* 20)

# +, extend
listaC = [1, 2, 3, 4, 5, 9]
listaD = [9, 8, 7, 6, 5, 4]
listaE = listaC + listaD
print(listaE)
print('\n', '-=-'* 20)

#extend
listaG = [1, 2, 3, 4, 5, 9]
listaH = [9, 8, 7, 6, 5, 4]
listaG.extend(listaH)
print(listaG)
print(listaH)

print('\n', '-=-'* 20)


#Agora se alterar algo em B, também vamos alterar a lista A.
listaB[0] = 10
print(listaA)
print(listaB)
print('\n', '-=-'* 20)

#copia de uma lista sem quem LISTA A seja altera quando mudar a lista B
original = [10, 9, 8, 7]
copia = original[:] #agora a se alterar a lista copia, não vamos alterar os valores da original
print(original)
print(copia)
print('\n', '-=-'* 20)

copia[0] = 20
print(original)
print(copia)