from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade < 5:
    print('Vaza')
elif idade <= 9:
    print('Competidor(a) mirim')
elif idade <= 14:
    print('Competidor(a) infantil')
elif idade <= 19:
    print('Competidor(a) junior')
elif idade <= 20:
    print('Competidor(a) sênior')
else:
    print('Competidor master')