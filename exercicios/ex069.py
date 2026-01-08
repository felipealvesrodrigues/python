c18 = 0
cm = 0
c20 = 0
while True:
    print('-' * 19)
    print('CADASTRE UMA PESSOA')
    print('-' * 19)
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F] ')).upper()
    while s != 'F' and s != 'M':
        s = str(input('Sexo: [M/F] ')).upper()
    if i > 18:
        c18 += 1
    if s == 'M':
        cm += 1
    if s == 'F' and i < 20:
        c20 += 1
    print('-' * 19)
    continua = str(input('Quer continuar? [S/N] ')).upper()
    while continua != 'N' and continua != 'S':
        continua = str(input('Quer continuar? [S/N] ')).upper()
    if continua == 'N':
        break
print(f'Foram cadastradas {c18} pessoas com mais de 18 anos, {cm} homens e {c20} mulheres abaixo de 20 anos.' )

