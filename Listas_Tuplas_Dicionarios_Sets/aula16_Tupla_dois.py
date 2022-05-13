a = (1, 2, 3, 5)
b = (4, 6, 7 , 8, 5)
c = a + b #não ira fazer a soma, e sim a união de A + B
print(c)

print(f'Index: {c.index(5)}') #ira mostrar em qual posição esta o n 5 =3
print(f'Index {c.index(5, 4)}' )#ira mostrar em qual posição esta o n 5, a partir da posição 4
print(f'Sorted:  {sorted(c)}')
print(f'O menor valor foi {min(c)}')
print(f'O maior valor foi {max(c)}')
print('\n')
