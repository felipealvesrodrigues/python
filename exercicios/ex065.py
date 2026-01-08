n = int(input('Digite um número: '))
continua = str(input('Quer continuar? [S/N] ')).upper()
c = 1
s = maior = menor = n
while continua == 'S':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    continua = str(input('Quer continuar? ')).upper()
    
print('Você digitou {} números e a média foi {:.2f}'.format(c, s / c))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
