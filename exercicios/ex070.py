total_preço = contador_mil = preço_barato = contador = 0
produto_barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total_preço += preço 
    contador += 1
    if preço > 1000:
        contador_mil += 1
    if contador == 1 or preço < preço_barato:
        preço_barato = preço 
        produto_barato = nome
    continua = ' '
    while continua not in 'SN':
       continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
    
print(f'O valor total dos produtos é R${total_preço:.2f}')
if contador_mil > 1:
    print(f'{contador_mil} produtos custam mais que R$1000.')
else:
    print(f'{contador_mil} produto custa mais que R$1000.')   
print(f'O produto mais barato é o(a) {produto_barato}, custando R${preço_barato:.2f}')





""" total = cmil = menor = cont = 0
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

 Enquando o usuário não digitar Sim ou Nâo, o loop da resposta vai continuar. o upper é pra deixar tudo maiúsculo e o strip[0] é pra pegar a primeira letra da palavra, pois como eu coloquei de condição so as letras S e N, com o strip o input so vai reconhecer as primeiras letras caso o usuário digite as palavras Sim ou Não ao invés das letras """ 














