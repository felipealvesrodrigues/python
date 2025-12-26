casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos você vai pagar? '))
meses = tempo * 12
prestaçao = casa / meses 
trinta = salario * 0.30
if prestaçao > trinta:
    print('As prestações ficarão por \033[32mR${}\033[m.'.format(prestaçao))
    print('\033[31mNEGADO!!! As prestações excedem o valor máximo de 30% do seu salário.\033[m')
else:
    print('\033[32mAPROVADO. Seu empréstimo está em processamento.\033[m')
