# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

t = int(input('Digite o valor do termo: '))
r = int(input('Digite o valor da razão: '))
decimo = t + (10 - 1) * r
for c in range (t, decimo + r, r):
    print(f'{c}', end=' → ')
print('ACABOU')


