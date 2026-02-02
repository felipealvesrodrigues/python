""" 
MINHA SOLUÇÃO

numeros= list()
par= list()
impar= list()
for c in range(1, 8):
    n= int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
        
par.sort()
impar.sort()
numeros.append(par[:])
numeros.append(impar[:])
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram: {numeros[1]}') 
"""
#GUANABARA
núm= [[], []]
valor= 0
for c in range(1, 8):
    valor= int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 21)
núm[0].sort()
núm[1].sort()
print(f'Valores pares digitados: {núm[0]}')
print(f'Valores ímpares digitados: {núm[1]}')