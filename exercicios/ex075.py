num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite um último número: ')))

print(f'Você digitou os valores{num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es).')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else: 
    print('O valor 3 não foi encontrado.')
print('Os valores pares digitador foram: ', end= '')
for valor in num:
    if valor % 2 == 0:
        print(valor, end= ' ')