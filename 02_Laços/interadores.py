'''Interadores = Um iterador e sempre um iteravel, mas que produz um valor a cada vez que a usado como argumento da funcao nativa next().'''

nome ='Jonas' #Var Jonas e uma sequecia de str (iteravel)
for letra in nome:
    print(letra)
print('-=' * 20)

'''Criando um interado'''
iterador = iter(nome)


'''Consumindo os valores do iterador, apos ser consumido o valor, eles acabam'''
print(next(iterador)) #aqui ele ira entergar a primeira variavel da sequencia nome
print(next(iterador))#ira entergar a segunda variavel da sequencia nome
print(next(iterador))

'''Podemos notar que o iterado seria o trabalho do for, so que passando um iteravel de cada vez'''
print('-=' * 20)

#obs: utizamos 3 iteraveis da palavra nome (JON) no interador, agora se passamos o iterador para um for ele so retornara o valor restante
'''a partir do momento em que os valores do iterador foram consumidos, eles acabam'''

for valor in iterador:
    print(valor)

