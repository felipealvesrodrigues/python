altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2
print('seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso. Come!')
elif imc < 25:
    print('Você está com o peso ideal!! Parabéns!!')
elif imc < 30:
    print('Você está acima do peso. Emagreça!')
elif imc < 40:
    print('Você está obeso!! Cuidado.')
else:
    print('Você está com obesidade mórbida! Nem tenta emagrecer, não vai dar tempo')