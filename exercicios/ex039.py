from datetime import date
print('Já está na hora de se alistar?')
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
    
if idade < 18:
    falta = 18 - idade
    print('Você ainda tem {} ano(s) livre'.format(falta))
elif idade == 18:
    print('Está na hora de servir o país! Se aliste!')
else:
    passou = idade - 18
    print('Você está {} ano(s) atrasado prara se alistar'.format(passou))


