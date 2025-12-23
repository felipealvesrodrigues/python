import math
a = float(input('Ângulo: '))
s = math.sin(math.radians(a)) #transformando em radianos pq o seno e os outros são passados em radianos
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('seno: \033[1;35m{:.2f}\033[m, cosceno: \033[1;35m{:.2f}\033[m, tangente: \033[1;35m{:.2f}\033[m'.format(s, c, t))

