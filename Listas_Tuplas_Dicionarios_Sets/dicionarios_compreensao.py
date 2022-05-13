def linhas(txt):
    print('-=' * 20)
    print(txt.center(40))
    print('-=' * 20)

linhas('Lista principal')
lista = [('chave', 'valor'), ('chave2', 'valor2'),]
print(lista)
print()


linhas('Trabalhando')
d1 = {chave: valor for chave, valor in lista}
print(d1)
print()

linhas('Aumentando as letras')
d2 = {chave.upper(): valor.upper() for chave, valor in lista}
print(d2)