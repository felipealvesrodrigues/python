import random
c = 0
while True:
    ip = str(input('Ímpar ou par: '))
    r = random.randint(0, 1000)
    if ip == 'par' and r % 2 == 0 or ip == 'impar' and r % 2 != 0:
        print('Ganhou')
        c += 1
        print(r)
    elif ip == 'impar' and r % 2 == 0 or ip == 'par' and r % 2 != 0:
        print('Perdeu')
        print(r)
        break
print(f'Você ganhou {c} vez(es) consecutivas')
