'''Transformação de string'''
frase = 'Curso em video python'

#replace = ira substituir a palavra
print('Replase:', frase.replace('python', 'Android\n'))

#upper = transforma em letra maiuscula as letras minusculas
print('Upper:', frase.upper(),'\n')

#lower = transforma em minusculas as letras maiusculas
print('Lower:',frase.lower(),'\n')

#capitalaize = transforma a 1º letra em maiuscula e o resto em minuscula
print('Capitalize:', frase.capitalize(), '\n')

#title = transforma a primeira letra de todas as frases em maiuscula
print('Title:', frase.title(), '\n')

#split = ira dividir a frase em listas, tornando a frase toda em 4 palavras e reindexsando cada letra (aula 09 27 min)
print('Split:', frase.split())

divido = frase.split() #criei uma nova variavel recebendo a lista
print(divido[0]) # quero que imprima o 1 item da lista dividido
print(divido[0][3], '\n') #ira mostrar o 1 item da lista e a 3 letra do item

#join = ira adicionar o que for passado para ele entra as palavras as palavras
print('Join:', ' '.join(frase))
print('*'.join(frase))

print('-'*40)
'''______________________________________________________________________'''

fraseDois = '   Aprenda python   ' #deixei espaços antes e depois da frase

#strip = remove os espaços desnecessarios antes e depois da frase
print('Strip: ', fraseDois, '\n')
print(fraseDois.strip())

#rstrip( começa pela direita) e lstrip (remove da esquerda)
print('Rstrip: ', fraseDois.rstrip(), '\n')
print('Lstrip:', fraseDois.lstrip(), '\n')


#ljust :  justificada em uma sequência de largura de comprimento.
nome ='Jonas salles'
print(nome.ljust(20, '#'))
print(nome.rjust(20, '#'))

