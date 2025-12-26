n1 = float(input('Escreva nota da primeira etapa: '))
n2 = float(input('Escreva nota da segunda etapa: '))
m = (n1 + n2) / 2
print('Sua média é \033[1m{:.1f}'.format(m))
if m < 5:
    print('Você foi \033[1;31mREPROVADO\033[m')
elif m < 6.9:
    print('Você está de \033[33mRECUPERAÇÃO\033[m')
else: 
    print('Você foi \033[32mAPROVADO\033[m')