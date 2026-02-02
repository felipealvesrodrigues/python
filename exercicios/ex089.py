""" MINHA SOLUÇÃO 
alunos= list()
temp= list()
while True:
    nome= str(input('Nome: '))
    nota1= float(input('Nota 1: '))
    nota2= float(input('Nota 2: '))
    media= (nota1 + nota2) / 2
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    temp.append(media)
    alunos.append(temp[:])
    temp.clear()
    keep= str(input('Deseja continar? [S/N] ')).upper().strip()[0]
    while keep not in 'SN':
        keep= str(input('Deseja continar? [S/N] ')).upper().strip()[0]
    else: 
        if keep == 'N':
            break
print('-=' * 21)
print('No.  NOME          MÉDIA')
for i, aluno in enumerate(alunos):
    print(f'{i}    {alunos[i][0]:10}     {alunos[i][3]}')
notas= int(input('Mostrar notas de qual aluno? (999 interrompe). No.: '))
while notas != 999:
    print(f'Notas de {alunos[notas][0]} são [{alunos[notas][1]}, {alunos[notas][2]}]')
    notas= int(input('Mostrar notas de qual aluno? (999 interrompe). No.: '))
print('-=' * 21)
print('PROGRAMA FINALIZADO')
print('<<< VOLTE SEMPRE >>>')
"""

# GUANABARA
ficha= list()
while True:
    nome= str(input('Nome: '))
    nota1= float(input('Nota 1: '))
    nota2= float(input('Nota 2: '))
    media= (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp= str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 21)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 28)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc= int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
        