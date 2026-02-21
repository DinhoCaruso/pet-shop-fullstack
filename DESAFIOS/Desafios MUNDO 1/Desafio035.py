# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

# Ex:
#
# r1
# r2
# r3
# Existe um princípio matemático para a formação de um triângulo: Qual será?
# b + c > a
# a + c > b
# a + b > c

a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
if a < b + c and b < a + c and c < a + b:
    print('As medidas formam triângulo')

else:
    print('Não forma um triângulo. ')













