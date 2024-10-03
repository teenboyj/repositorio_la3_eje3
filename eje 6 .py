from math import sqrt
print('programa para calcular el indice wind chill')
V=float(input('ingrese la velocidad del viento: '))
T=float(input('ingrese la temperatura en grados celsius: '))
WCI=(10*sqrt(V)-V+10.5)*(33-T)
print('el indice wind chill es {0:.2f}'.format(WCI))
