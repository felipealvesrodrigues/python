import math
a = float(input('Ângulo: '))
s = math.sin(math.radians(a)) #transformando em radianos pq o seno e os outros são passados em radianos
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('seno: {:.2f}, cosceno: {:.2f}, tangente: {:.2f}'.format(s, c, t))

