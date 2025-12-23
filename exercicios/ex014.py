t = float(input('Informe a temperatura em °C: '))
f = t * 1.8 + 32
r = print('A temperatura de \033[7;30m{}°C\033[m corresponde a \033[1;44m{:.1f}°F.'.format(t, f))