l = int(input('Largura da sua parede em metros: '))
a = int(input('Altura da sua parede em metros: '))
area = l * a 
t = area / 2
print('A área da sua parede é de {}m². Serão necessários {} litros de tinta para pintá-la'.format(area, t))