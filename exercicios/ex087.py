matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par= maior= somacoluna =0
for linha in range(0, 3): # vai mandar por 3 números ((0, 0) até (0, 2)) depois disso, vai adicionar 1 na coluna e vai mandar por mais 3 números ((1, 0) até (1, 2))
    for coluna in range(0, 3):
        matriz[linha][coluna]= int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 21)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end= '')
        if matriz[linha][coluna] % 2 == 0: # aq eu garoteei, era so colocar os dois indices da matriz :(
            par += matriz[linha][coluna]
    print()
print('-=' * 21)
print(f'A soma dos valores pares é {par}')
for linha in range(0, 3):
    somacoluna += matriz[linha][2] # o indice ta como 2 pq todos os valores da teceira coluna estão no indice 2 (da pra ver isso quando o programa é executado), somente a linha varia
print(f'A soma da terceira coluna é {somacoluna }')

for c in range(0, 3): # o raciocinio aq é basicamente a mesma coisa q foi feita com a terceira coluna
    if c == 0 or matriz[1][c] > maior:
        maior= matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')