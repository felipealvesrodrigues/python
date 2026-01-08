c = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} número(s) e a soma deles é {s}')
