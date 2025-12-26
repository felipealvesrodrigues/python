n = int(input('Digite um número: '))
print('Escolha um método de conversão:')
menu = ('Digite 1 para binário\n'
      'Digite 2 para octal\n'
      'Digite 3 para hexadecimal')
conversao = int(input(menu + '\nQual sua escolha? '))
if conversao == 1:
    print(bin(n))
elif conversao == 2:
    print(oct(n))
elif conversao == 3:
    print(hex(n))
else: 
    print('\033[31mPor favor, digite uma opção válida\033[m')