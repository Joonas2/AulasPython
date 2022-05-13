
#Validação de um numero digitado pelo usuario
while True:
    numero = input('Digite um numero: ')

    if not numero.isnumeric():
        print('Digite uma valor numerico')
        continue
    else:
        break


#____________________________________________________________
variavel = ['Jonas', 'Nathi', 'Teka', 'Lelo']

for valor in variavel:
    if valor.startswith('J'): #startswith - ira verificar se algum dos parametros passado começa com J
        print(f'{valor}')
    else:
        print('Erro')
