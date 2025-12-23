s = float(input('Qual seu salário? '))
a = s * 0.15
sf = s + a 
print('Seu salário com aumento ficará \033[32mR${:.2f}'.format(sf))