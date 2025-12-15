c = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados com o carro? '))
pago = (c * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

#pago = (c * 60) + (km * 0.15) dava pra fazer assim também, bem mais fácil
 
""" pc = c * 60
pkm = km * 0.15
s = pc + pkm """