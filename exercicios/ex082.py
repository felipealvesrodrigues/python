""" valores = list()
pares = list()
ímpares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continua? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
pos = 0
for pos in range(len(valores)):
    if valores[pos] % 2 == 0:
        pares.append(valores[pos])
    else:
        ímpares.append(valores[pos])
valores.sort()
pares.sort()
ímpares.sort()
print(f'A lista completa é {valores}')
print(f'a lista de pares é {pares}')
print(f'a lista de ímpares é {ímpares}') """

#Resolução guanabara:
valores= list()
pares= list()
ímpares= list()
while True:
    valores.append(int(input('Digite um número: ')))
    continua= str(input('Deseja continua? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
for i, v in enumerate(valores): # esse I com enumerate substitui o pos
    if v % 2 == 0:
        pares.append(valores)
    else:
        ímpares.append(valores)
print('-=' * 20)
valores.sort()
ímpares.sort()
pares.sort()
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
        