# AULA 08 - UTILIZANDO MÓDULOS
import importlib
import math
#  Import > Importa uma biblioteca - import math

#  from math import cos -> Importa somente a funçao cos da biblioteca math

#  math -> Biblioteca de operadores aritméticos {
#    sqrt()  ---> Raiz Quadrada de um numero ------- raiz = math.sqrt(numero)
#    floor() ---> Arredonda o numero para baixo ---- 5,23 fica 5,00
#    ceil() -----> Retorna um valor inteiro ---------------- 5,23 fica 5
#    hypot() ---> Retorna a hipotenusa dos catetos - math.hypot (co, ca)
#    pow() ----> Potencia de um numero ---------------- pow (2, 3) = 2³ = 8
#    radians()-> Converte em graus radianos ---------- print(math.radians(180))
#    cos() -----> Retorne o cosseno em radianos --- print(math.cos(math.radians(x)))
#    sin() ------> Retorne o seno em radianos --------- print(math.sin(math.radians(x)))
#    tan() -----> Retorne a tangente em radianos---- print(math.tan(math.radians(x)))

#  }

#  random -> Gerar numeros pseudoaleatorios {

#      randint() > Retorna um numero inteiro no range --------------- random.randint(1, 10)
#      choice() --> Retorna um elemento aleatório da sequência - random.choice(x)
#      shuffle() > Embaralha a sequência x no lugar ------------------- random.shuffle(y)


# EXERCICIOS

#import math
#num = int(input('Digite um número:'))
#raiz = math.sqrt(num)
#print(f'A raíz de {num} é igual a {raiz:.2f}')
#print()

# OU

#from math import sqrt
#num = int(input('Digite um número: '))
#raiz = sqrt(num)
#print(f'A raíz de {num} é igual a {raiz:.2f}')

#       OU

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raíz de {num} é igual a {(raiz):.2f}')

import emoji
print (emoji.emojize('Olá, mundo :earth_americas:', language='alias'))

import random
num = random.randint(1, 10000)
print (num)



from math import pow

n1= float(input('Digite um número: '))
n2= float(input('Digite outro número: '))

p = pow (n1, n2)

print(f'O número {n1} elevado a {n2} é igual a {p:.1f}')


from math import factorial
def calcular_fatorial (n: object) -> object:
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

n = int(input('Digite um número: '))

f = calcular_fatorial(n)

print(f'O fatorial de {n} é {f}')


from math import sqrt
num = float(input('Digite um número: '))
r = sqrt(num)
print(f'A raíz quadrada de {num} é {r:.2f}')
