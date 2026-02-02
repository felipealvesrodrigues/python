""" MEU
aluno= dict()
aluno['Nome']= str(input('Nome: '))
aluno['Média']= float(input(f'Média de {aluno["Nome"]}: '))
aluno['Situação']= 'unknow'
if aluno['Média'] >= 7:
    aluno['Situação']= 'aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação']= 'recuperação'
elif aluno['Média'] < 5:
    aluno['Situação']= 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
"""


#GUANABARA
aluno= dict()
aluno['Nome']= str(input('Nome: '))
aluno['Média']= float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação']= 'aprovado'
elif 5 <= aluno['Média'] < 7:
     aluno['Média']= 'recuperação'
else:
    aluno['Média']= 'reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')