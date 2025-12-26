produto = float(input('Qual o valor do produto desejado? '))
metodo = print('Métodos de pagamento:')
menu = ('Digite 1 para dinheiro/cheque com 10% de desconto.\n'
        'Digite 2 para pagar à vista no cartão com 5% de desconto\n'
        'Digite 3 para pagar em até 2x vezes no cartão sem juros\n'
        'Digite 4 para parcelar em 3x ou mais com 20% de juros')
selecao = int(input(menu + '\nSelecione aqui o método: '))
if selecao == 1:
    pordez = produto - (produto * 0.10) 
    print('Seu produto com desconto ficará por R${:.2f}'.format(pordez))
elif selecao == 2:
    porcinco = produto - produto * 0.05
    print('Seu produto com o desconto ficará por R${:.2f}'.format(porcinco))
elif selecao == 3:
    print('Seu produto ficará por R${:.2f}. Essa opção não contém desconto'.format(produto))
else:
    juros = produto * 0.20 + produto
    print('Seu produto ficará por R${}'.format(juros))