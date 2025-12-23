c = input('Qual seu nome? ')
e = c.strip() 
t = e.title()
dentro = 'Alves' in t
print('Seu nome tem Alves? \033[32m{}'.format(dentro))
