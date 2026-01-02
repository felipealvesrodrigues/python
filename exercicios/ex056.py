nomeVelho = 0
velho = 0
idadeMulher = 0
for p in range(1, 5):
    print('----- {}ª -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    if p == 1:
        media = idade
    else: 
        media = idade + media
    if p == 1 and sexo == 'M':
        velho = idade
        nomeVelho = nome
    else:
        if idade > velho and sexo == 'M':
            velho = idade
            nomeVelho = nome
    if sexo == 'F' and idade < 20:
        idadeMulher = idadeMulher + 1       
print('A média de idade do grupo é de {:.1f} anos'.format(media // p))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomeVelho))
print('São {} mulher(es) com menos de 20 anos'.format(idadeMulher))





