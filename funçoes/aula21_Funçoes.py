
#Interactive Help - digitamos help() é o comando dentro, para saber quais suas funções
'help(print)'

#Docstring: colocamos um manual dentro da função, digitamos 3 vezes aspas duplas.
#depois chamaos o help(soma), ira mostrar o manual da função
def soma(a, b):
    """
    :param a: valor
    :param b: valor
    :return: soma de a + b
    Def criada por Jonas Salles
    """
    s = a + b
    print(s)
soma(10, 20)
'help(soma) = irá mostra a docstring'

#_______________________________________________________

#Parametro opcional em uma função.
#Adicionamos o parametro = 0

def somaDois(a = 0, b = 0, c = 0):
    s = a + b + c
    print(s)

somaDois(10, 20, 30) # aqui os tres parametros recebem valores
somaDois(10, 15) # aqui somente dois parametros recebem valores

print()
"Return"
print('Return')
def somaTres(a = 0, b = 0, c = 0):
    s = a + b + c
    return s #ira retornar o valor de s onde for chamada a função somaTres

r1 = somaTres(10, 20, 30) #r1 recebeu o valor de "s"
print(r1)
print(f'o Valor da soma é {somaTres(10, 20, 30)}')
