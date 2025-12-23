from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para sanalisar o ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} \033[32mé\033[m bissexto'.format(ano))
else: 
    print('O ano {} \033[31mnão\033[m é bissexto'.format(ano))