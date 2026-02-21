# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE
# NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.


angulo = float(input(' Digite o ângulo: '))
from math import cos, sin, tan, radians
c = cos(radians(angulo))
s = sin(radians(angulo))
t = tan(radians(angulo))
print (f' O COSSENO de {angulo} graus é {c:.2f}\n o SENO é {s:.2f}\n e a TANGENTE é {t:.2f}')












