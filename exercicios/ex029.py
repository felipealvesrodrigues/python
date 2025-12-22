v = float(input('Qual a velocidade que seu veículo estava? '))
if v > 80:
    multa = (v - 80) * 7
    print('MULTADO! Você estava acima da velocidade permitida na via.')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija sempre com segurança!')
