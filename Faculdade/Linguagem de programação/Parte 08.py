# [BREAK]
# Crie um program que receba um número natural n(n>1) e exiba
# uma mensagem indicando se né primo.

#n = int(input('número: '))
#divisor = 2
#while divisor < n:
#    if n % divisor == 0:
#        break
#    divisor += 1
#if divisor == n:
#    print('primo')
#else:
#    print('Não é primo')

# [REPEAT...UNTIL]

# Crie um programa que receba um número n >= 0 e exiba o valor
# da raíz quadrada de n. Enquanto n for um número negativo, repita
# a solicitação de entrada.

#from math import sqrt
#while True:
#    n = float(input('Número: '))
#    if n >= 0: break
#print(f'Raíz quadrada de {n} é {sqrt(n)}')

# LAÇOS DE REPETIÇÃO ANINHADOS
# Crie uma função que simule um relógio digital, exibindo desde 00:00:00 até 23:59:59

def relogio():
    h=0
    while h > 24:
        m = 0
        while m < 60:
            s = 0
            while s < 60:
                print(f'{h:02}:{m:02}:{s:02}')
            s += 1
        m += 1
    h += 1































