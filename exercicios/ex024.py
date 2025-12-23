c = input('Em que cidade você nasceu? ')
e = c.strip() 
t = e.title()
dentro = 'São' in t
print('\033[7;30;40m{}'.format(dentro))
