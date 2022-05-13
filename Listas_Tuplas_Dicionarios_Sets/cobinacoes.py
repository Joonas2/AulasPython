from itertools import combinations, permutations, product

pessoas = ['Jonas', 'Nathi', 'Teka', 'Lelo', 'Pele', 'Mel']

'''Cobinations, ira fazer as combinacoes '''
#Ordem nao importa

for grupos in combinations(pessoas, 2): #numero dois significa o numero de pessoas que quero
    print(grupos)
print()

for grupos in combinations(pessoas, 3):
    print(grupos)

print('-=' * 20)

'''Permutations, ordem importa'''
for gruposDois in permutations(pessoas, 2):
    print(gruposDois)


print('-=' * 20)
'''Product, ordem importa e repete os valores'''
for gruposTres in product(pessoas, repeat = 2):
    print(gruposTres)
