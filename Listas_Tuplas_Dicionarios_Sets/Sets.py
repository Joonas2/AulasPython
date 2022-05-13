'''sets (conjuntos), utilizamos {} para declarar igual fazemos com dicionarios'''
#nao tem as keys, somente valores
#nao tem index, entao nao posso acessar diretamente um valor dele
#nao aceitam elementos duplicados

def linha():
    print('-=' * 20)

#declarando um set
s1 = {1, 2, 3, 4, 5}
s2 = set()
print(s1)
print(s2)
linha()

#adicionando valores em um set
s2.add(1)
s2.add(6)
s2.add(5)
s2.add(9)
print(s2)
linha()

#adicionando valor com update - ele vai separa a palavra python igual faz slipt, alem de nao obedecer ordem
valor = set()
valor.update('Python')
print(valor)
linha()

#removendo valores
s2.discard(6)
print(s2)
linha()

#sets nao aceitam elementos duplicados !!!
#exemplo de uso, lista com varios elementos duplicados, passamos ela como um set para remover os duplicados

l1 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3]
l1 = set(l1) #transformei minha lista em set, para remover os valores duplicados
print(l1)

l1 = list(l1) #transformei minha lista em uma lista novamente
print(l1)
linha()

#uniao de sets: utilizamos a | para unir dois sets, ele ira excluir os elementos repetidos
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}
c = a | b
print(c)
linha()

# intersecao = utilizamos o & para fazer a intersecao
d = a & b
print(d)
linha()

#diferente: utilizamos o - para descobrir o elemento diferente
'''A ordem importa nessa funcao'''
f = a - b #elementos que estao em "a" e nao estao em "b"
g = b - a #elementos que estao em "b" e nao estao em "a"
print(f)
print(g)
linha()

# Uniao removendo a intercesao: utilizamos o ^ para unir os sets, removendo os elementos iguais
h = a ^ b
print(h)

