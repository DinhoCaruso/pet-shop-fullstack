# Escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma sequência
# de fibonacci.

# Ex:
# 0 → 1 → 1 → 2 → 3 → 5 → 8

# fn = fn-1 + fn-2

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('~'*30)













