d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de \033[35m{:.1f}KM\033[m'.format(d))
if d < 200:
    preço = d * 0.50
    print('E o preço da sua passagem será de \033[32mR${:.2f}\033[m'.format(preço))
else: 
    preço = d * 0.45
    print('E o preço da sua passagem será de \033[32mR${:.2f}'.format(preço))