
while True:
    n = int(input('Quer ver a tabuáda de qual valor? '))
    print('=+=' * 7)
    for c in range(0, 11):
        print(f'{n} * {c} = {n * c}')
        print('-' * 15)
    print('=+=' * 7)
    if n < 0:
        break
print('Se vira')