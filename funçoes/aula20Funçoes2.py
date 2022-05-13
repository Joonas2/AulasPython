'''Quando não sabemos a quantidade de parametros que sera passado. ex:'''
#desenpacotamento
def contador(* num): # utilizamos os * para receber os valores, e ele irá jogar os valores dentro de num
    print(num) #ele irá criar uma tupla e adicionar os valores nela, sem ser necessario passar a quantidade de parametros

contador(4, 5, 6, 7)
contador(6, 8, 7, 6)
contador(5, 6, 7)
print()
#dobrando os numeros de uma lista
def dobra(lista): #parametro lista recebera os valores da lista valores
    pos = 0
    while pos < len(valores):
        lista[pos] = lista[pos] * 2 #dobrando o valor da variavel na posição[]
        pos = pos + 1

valores = [1, 2, 3, 5, 8, 9]
dobra(valores) #chamei a função dobra, e passei como parametro a lista valores
print(valores)