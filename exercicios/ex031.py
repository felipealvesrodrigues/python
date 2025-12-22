d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}KM'.format(d))
if d < 200:
    preço = d * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
else: 
    preço = d * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))