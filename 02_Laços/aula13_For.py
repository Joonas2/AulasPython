#Continue - pula pro proximo laço
#break - termina o laço



#Ira começar no 1 e vai imprimir ate 9
for c in range(1, 10):#range =  Range: cria uma estrutura ordenada seguindo a ordem que for passada
    print(c, end=' ')

print('\n', '-=-' * 20)

#ira começar no 10 e vai imprimir ate 0, tirando - 1 a cada laço
for c in range (10, 0, -1):
    print(c, end=' ')
print('\n', '-=-'* 20)

# recebendo o valor do teclado
n = int(input('Digite um numero: '))
for c in range(0, n + 1):
    print(c)
print('\n', '-=-'* 20)


#recebendo inicio, fim e passo
"""i = int(input('Digite o Inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite os passos: '))

for c in range(i, f, p):
    print(c)
"""
lista = ['Jonas', 'Nathalia', 'Teka', 'Pele', 'Lelo']
for pos, pessoa in enumerate(lista):
    print(f'Na posição {pos} temos alocado a variavel {pessoa}')