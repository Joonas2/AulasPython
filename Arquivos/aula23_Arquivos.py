'''Arquivos'''

#Criando um arquivo: metodo open("nome arquivo", "modo de uso")
arquivo = open("arquivo.txt", "a") # Se o arquivo não existir ele ira criar um arquivo na pasta do projeto

"Modo de uso: é o parametro passado ao lado no nome do arquivo"
'r = leitura'
'w = escrita, apagando o que estava escrito anteriormente'
'x = escrita - retoma um erro caso o arquivo ja exista'
'a - escrita - insere novos dados no final do arquivo'
'b - modo binario'
't - modo texto(padrao)'
'+ - atualizar'

#-----------------------------------------------------------
'Escrevendo em um arquivo' \
' método write() que recebe uma string como parâmetro e a insere no arquivo:'
# lembrar de abrir o arquivo antes
arquivo.write('Olá mundo\n')

#Adicionando mais de um parametro
nome = str(input('Nome: ')).strip()
idade = int(input('Idade: '))
arquivo.write(f'{nome}; {idade}')


' método é o writelines() que recebe um objeto iterável (seja uma lista, uma tupla, um dicionário, etc). ' \
'Com este método, várias linhas poderão ser inseridas no arquivo, diferente do método write() que só recebe uma string por vez:'
lista = list()
lista.append('Jonas\n')
lista.append('Nathalia\n')
lista.append('Teka\n')
lista.append('Lelo\n')

arquivo.writelines(lista)

#------------------------------------------------------
'''Lendo dados de arquivos >>>>'OBSERVAÇÃO: DEVEMOS ABRIR O ARQUIVO PASSANDO 'R' COMO MODO DE USO <<<<'''

'método readline() que irá ler uma quantidade N de caracteres da primeira linha passadas como parâmetro:'
arquivo = open("arquivo.txt", "r")
print(arquivo.readline(2))

'método readlines(). Este método irá retornar todas as linhas do arquivo:'
print(arquivo.readlines())