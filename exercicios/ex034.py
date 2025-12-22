salario = float(input('Qual o seu salário? '))
if salario <= 1250.00:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)
    
print('Seu novo salário será de R${:.2f}'.format(aumento))