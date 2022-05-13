#Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
#Nos dicionarios podemos adiconar nomes para posição que está a variavel, diferentemente das listas que usavam index por numero da posição

#Declarando um dicionario
dados = dict()
#dados = {}

#adicionando elementos
dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo'] = 'M' #não utiliozamos o append em dicionarios.

#Imprimindo elementos
print(dados['nome']) #Nome sera o index, inves de ser 0, 1, 2.
print(dados['idade'])
print(f'O {dados["nome"]} tem {dados["idade"]}') #para imprimir utilizando o fstrig devemos declarar a chaves em apas duplas
print()

#----------------------------------------------
filmes = {'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'}

#Valores, Chaves, itens
#Valores = são as variaveis que adicionamos no dicionario.
print(filmes.values())

#chaves = são os index das variaveis (nome, ano, diretor)
print(filmes.keys())

#Itens = itens e tudo que tem dentro do dicionario (chaves e valores)
print(filmes.items())
print()
#for
for k, v in filmes.items(): # Como se fosse o enumerate
    print(f'O {k} é {v}') #Cada laço, ele vai pegando um chave e imprimi o valor, depois vai para proxima chave
