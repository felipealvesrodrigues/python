valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('[ERRO] Valor duplicado.')
    continua = str(input('Deseja continuar? ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Deseja continuar? ')).upper().strip()[0]
    else: 
        if continua == 'N':
            break
valores.sort()
print(valores)
        