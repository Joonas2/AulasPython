variavel = ['Jonas', 'Nathi', 'Teka', 'Lelo']

for valor in variavel:
    if valor.startswith('J'): #startswith - ira verificar se algum dos parametros passado come�a com J
        print(f'{valor}')
    else:
        print('Erro')

