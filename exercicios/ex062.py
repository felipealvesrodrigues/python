primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
total = 0
c = 1
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(termo, end= ' -> ') 
        termo += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos vpcê quer mostrar a mais? '))
print(total)
print('FIM')










"""primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(termo, end= ' -> ')
    termo += razão
    c += 1
print('PAUSA')
continua = int(input('Quantos termos você quer mostrar a mais? '))

while continua != 0:
    c = 0
    while c < continua:
        print(termo, end= ' -> ')
        termo += razão
        c += 1
        if c == continua:
            c = 0
            print('PAUSA')
            continua = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM') """
# esse é o meu código


























""" continua = str(input('\nDeseja continuar? [S/N] ')).upper()


if continua == 'S':
    c = 0
    plus = int(input('Quantos termos você quer mostrar a mais? '))
    if plus != 0:
        while c < plus:
            print(termo, end= ' -> ')
            termo += razão
            c += 1 """

""" if continua == 'S':
    print('PAUSA')
    plus = int(input('Quantos termos você quer mostrar a mais? '))
    if plus != 0:
        c = 0
        while c <= plus:
            print(termo, end= ' -> ')
            termo += razão
            c += 1
            if c == plus:
                c = 100000000000000000000000000000000000
    if plus == 0:
        c = 0
        print('Fim') """

""" if plus != 0:
        c = 0
        while c <= plus:
            print(termo, end= ' -> ')
            termo += razão
            c += 1
            if c == plus:
                c = 11   """         

""" while c == 11:
    print('PAUSA')
    plus = int(input('Quantos termos você quer mostrar a mais? '))
    if plus == 0:
        print('FIM')
    else:
        c = 0
        while c <= plus:
            print(termo, end= ' -> ')
            termo += razão
            c += 1
            if c == plus:
                c = 11 """

