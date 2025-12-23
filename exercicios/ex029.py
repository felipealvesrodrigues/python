v = float(input('Qual a velocidade que seu veículo estava? '))
if v > 80:
    multa = (v - 80) * 7
    print('\033[1;31mMULTADO! Você estava acima da velocidade permitida na via.')
    print('Você deve pagar uma multa de\033[m \033[32mR${:.2f}\033[m'.format(multa))
print('\033[32mTenha um bom dia! Dirija sempre com segurança!')
