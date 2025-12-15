import math
co = float(input('Tamanho do cateto oposto: '))
ca = float(input('Tamanho do cateto adjacente: '))
""" h = (ca**2 + co**2) 
print('O tamanho da hipotenusa é de {:.2f}' .format(sqrt(h)))
 """
h = math.hypot(co, ca)
print('O tamanho da hipotenusa é de {:.2f}'.format(h))

