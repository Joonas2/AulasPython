'''Variavel global e variavel local'''
'''Quando uma varivavel fica fora de uma função ela é global, quando uma var fica dentro de uma função ela é local'''

def teste(x, y):
    a = 0  #local, mesmo criando variavel fora, o valor não ira mudar
    global b #vai rceber o valor do B, global
    print(f'Valor de A: {a} dentro')
    print(f'Valor de B: {b} dentro')
    print()


a = 10 #global
b = 20

teste(a, b)
print(f'Valor de A: {a} fora')
print(f'Valor de B: {b} fora')

#para que A (Local)receba o valor de A (global) devo adicionar o Global antes