'''Analise de string'''

frase = 'Curso em video python'

#[3] = ira mostra a letra que se encontra na 3 posição
print(frase[3]) # lembrando que index começa em 0

#len: ira contar numero de caracteres tem na frase
print(len(frase))

#Count: ira contar quantidade de letras 'o' tem na frase
print(frase.count('o'))

#quantidade de letras 'o' tem do 0 ao 13
print(frase.count('o',0,13))

#(find = encontrar) quantas vezes ele encontrou 'deo', e ira mostra a posição da 1º letra
print(frase.find('deo'))
print(frase.find('jonas')) #resultado -1, pois não existe jonas na frase

#in = ira verificar se existe o parametro na frase respondendo true ou false
print('Curso' in frase) #true
print('curso' in frase) #false, pois curso esta com "c" minusculo

#podemos utilizar o in em um IF

if 'curso' in frase:
    print(frase)
