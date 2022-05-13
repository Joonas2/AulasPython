def linhas(txt):
    print('-=' * 20)
    print(txt.center(40))
    print('-=' * 20)

preco_produtos = [100, 150, 100, 5500]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

#calcular o valor do imposto dos produtos que e  30% e adicionar em uma lista
'''Forma tradicional'''
impostos = []
for intens in preco_produtos:
    impostos.append(intens * 0.3)
print(impostos)

'''Usando list'''

imposto = [preco * 0.3 for preco in preco_produtos]
print(imposto)




linhas('Lista principal')
listaUm = [1, 2, 3, 4, 5, 6, 7]
print(listaUm)
print()


#______________________________________________________________________________________________________________
linhas('Multiplicando valor por dois')
'''Criei a segunda lista, que quero que receba o valor * 2 da listaUm'''

#for: ira pegar cada valor da lista um, e passar para o que vem antes
multiplicandoPorDois = [valor * 2 for valor in listaUm]
print(multiplicandoPorDois)
print()



#______________________________________________________________________________________________________________
linhas('Alterando Letras')
'''a lista alterar vai receber as var da lista nome e alterar letra a por @'''
nomes = ['Jonas', 'Nathi', 'Teka', 'Lelo']
alterar = [letra.replace('a', '@') for letra in nomes]
print(alterar)
print()


#______________________________________________________________________________________________________________
linhas('Numeros pares')
numeros = list(range(0, 100)) #gerando uma lista ordenada de 0 a 100
print(numeros)

'''Criar uma lista que receba todos os valores pares'''
pares =[v for v in numeros if v % 2 ==0] #para cada valor em numeros, se for par, ira passar para v
print(pares)
print()

#______________________________________________________________________________________________________________
linhas('Divisiveis por 3 e por 8')
divisiveis = [v for v in numeros if v % 3 ==0 if v % 8 ==0]
'''for = para cada valor na lista numeros'''
'''if = se valor for divisivel por 3 e se valor for divisivel por 8 '''
'''entao passa os valores para v'''
print(divisiveis)

