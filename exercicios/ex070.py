total = cmil = menor = cont = 0
barato = ''
while True: 
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1 
    total += preço
    if preço > 1000:
        cmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e ele custa R${menor:.2f}')





















""" soma = cmil = barato = 0
nomeb = ''
while True:
    nome = str(input('Nome do Produto: '))
    p = float(input('Preço: '))
    c = str(input('Quer continuar? [S/N] ')).upper()
    soma += p
    barato = p
    if p > 1000:
        cmil += 1
    if p < barato:
        barato = p
    while p > barato:
        nomeb = nome
    while c != 'N' and c != 'S':
        c = str(input('Quer continuar? [S/N] ')).upper()
    if c == 'N':
        break
print(soma, cmil, nomeb)
     """
    
