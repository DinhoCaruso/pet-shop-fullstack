# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número é PAR.')
else:
    print('O número é ÍMPAR.')

##    OU

num = int(input('Digite um número: '))
print(f'O número é PAR.' if num % 2 == 0 else 'O número é ÍMPAR.')


