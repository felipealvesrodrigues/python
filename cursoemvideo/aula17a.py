""" num = [4, 6, 2, 9, 0, 0, 2]
num[2] = 11
num.append(7) 
num.sort()
num.insert(4, 6)
num.remove(6)
print(num)
#print(f'Essa lista tem {len(num)} elementos')
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
     """
     
""" valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista') """

a = [2,3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')