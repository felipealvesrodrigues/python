""" teste= list()
teste.append('Gustavo')
teste.append(40)
galera= list()
galera.append(teste[:])
teste[0]= 'Maria'
teste[1]= 22
galera.append(teste[:])
print(galera) """


""" galera= [['Ana', 19], ['João', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[0][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.') """

galera= list()
dado= list()
totmaior= totmenor= 0
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Se eu não colocasse um cópia aqui [:], quando eu desse clear alí em baixo, no print mostraria tudo vazio tbm >:( 
    dado.clear()
    
#print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'Temos {totmaior} de maior e {totmenor} de menor')