dado = list()
um = list()
dois = list()



for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    um.append(dado)# aqui estou recebendo uma copia do dado, tirando a conexão dos dois
    dois.append(dado[:])


print(f'Impresão de Dado e quantidade de variaveis {len(dado)}:{dado}')
print(f'Impresão sem copia, com conexão: {um}')
print(f'Impresão da copia dos dados da galera: {dois}')


dadosDois = list()
galera = list()

print('\n')

for p in range(0, 3):
    dadosDois.append(str(input('Nome: ')))
    dadosDois.append(int(input('Idade: ')))
    galera.append(dadosDois[:])#recebendo uma copia
    dadosDois.clear()#limpando as variaveis de dado, para não armazenar varias vezes

print(galera)
