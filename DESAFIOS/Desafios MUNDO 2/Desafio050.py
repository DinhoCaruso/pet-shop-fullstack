# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, descon-
# sidere-o.


# COMO EU FIZ:
print()
soma = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma dos números pares digitados é {soma}')
print('-='*20)
print()

# COMO FIZERAM NA CORREÇÃO:

soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares e a soma foi {soma}')



