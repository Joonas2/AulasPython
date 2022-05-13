'''Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.'''
def mostraLinha():
    print('-=-' * 20)

mostraLinha()
print('Olá Mundo')
mostraLinha()

#Utilizando parametros!
'''Criamos a função e dentro dos () digitamos o parametro que ela ira receber'''
'''Apos isso, ela executara o que esta dentro da função e ira verificar quando executar o parametro '''
'''E irá imprir a função onde ela foi chamada'''

def titulo(txt):#txt é um parametro passado para a função
    print('=-=' * 20)#vai executar isso apos receber o parametro
    print(txt)
    print('=-=' * 20)

#aqui estamos chamando a função, e passando o parametro para ela
titulo('Valor que o parametro irá receber')#o parametro txt ira receber o que esta digitado aqui
titulo('Parametro dois')

mostraLinha()

def soma(a, b):
    s = a + b
    print(s)

a = int(input('a: '))
b = int(input('b: '))
soma(a, b)

#------------------------------------------------
