n = float(input('Preço do produto: '))
d = n * 0.05 
p = n - d
print('O produto com desconto ficará por R${:.2f}'.format(p))