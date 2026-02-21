# Faça um programa que leia um número qualquer e mostre o seu
# fatorial.

# Ex:
# 5!=5x4x3x2x1=120

#from math import factorial
#num = int(input('Digite um valor: '))
#fat = factorial(num)
#print (f'O fatorial de {num} é {fat}.')


# ou

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c  # ou f *= c
    c -= 1
print(f'{f}')




