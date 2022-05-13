#As tuplas são variáveis compostas e imutáveis (não é possivel fazer mudanças nelas) que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
#devemos definir quantos valores seram adicionados nela
#Utilizamos () para definir um tupla
# Dentro da tupla, podemos ter dados de tipos diferentes ex: in, str
lanche = ('pizza', 'pastel', 'refri', 'chocolate') #Tupla lanche com 4 valores.
print(lanche)
#_________________________________________________________________________________
print(sorted(lanche))#Ira imprimir em ordem alfabetica
print(lanche.index('pizza'))# Index: mostra em qual posição esta o parametro passado
# del(lanche) #ira apagar a tupla toda
print('-=-'* 20)

#_________________________________________________________________________________
print(lanche[2])# ira imprimir Refri, pois o primeiro valor esta na posição zero

print(lanche[0:2]) #ira imprimir do lanche zero(pizza)e o lanche um (pastel), pois e sempre -1

print(lanche[1:])#ira imprimir do lanche um(pastel) ate o ultimo lanche(chocolate)

print(lanche[-1])#ira imprimir o ultimo lanche
#______________________________________________________________________________

print('\nUtilizando o for:')
for comida in lanche: #c ira receber as variaiveis de lanche
    print(comida)
print('-=-'*20, end='\n')

for c in range(0, len(lanche)):#Len ira contar quantas variaveis tem em lanche, que sera o parametro para for
    print(f'{c}) {lanche[c]}')#ira imprimir lanche na posição c

print('-=-'*20, end='\n')

for c in range(len(lanche), 0, -1):#Len ira contar quantas variaveis existem e será o inicio, ira até o zero, diminuindo um
    print(f'{c -1}) {lanche[c-1]}')

print('-'* 20)
for posição, comida in enumerate(lanche):#enumerate vai passar a posição e a comida
    print(posição, comida)

print('-=-'* 20)
#--------------------------------------------------

for comida in lanche:
    print(f'{comida:.<30}')
    print(f'{comida:.>30}')