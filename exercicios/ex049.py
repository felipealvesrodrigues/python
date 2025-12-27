n = int(input('Escolha um valor: '))
print('=+=' * 4)
for c in range(0, 10+1):
    print('{} * {} = {}'.format(n, c, n * c))
    print('-' * 11)
print('=+=' * 4)