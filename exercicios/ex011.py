l = int(input('Largura da sua parede em metros: '))
a = int(input('Altura da sua parede em metros: '))
area = l * a 
t = area / 2
print('A área da sua parede é de \033[1;35;43m{}m²\033[m. Serão necessários \033[31m{}\033[m litros de tinta para pintá-la'.format(area, t))