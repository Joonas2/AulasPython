'''fun lambda: e uma forma de utilizar uma funcao mais simples'''

produto = 1000

def imposto(valor):
    return valor * 0.3

print(imposto(produto))


#Lambda parametro: parametroRecebido * 0.3
'''Lambda vai receber um parametro antes dos dois pontos, depois pegar esse parametro e realizar o que foi dito depois '''

calcularImposto = lambda valor: valor * 0.3

print(calcularImposto(produto))