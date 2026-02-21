# Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar o valor 999, que é
# a condição de parada. No final, mostre quantos números foram digi-
# tados e qual foi a soma entre eles (desconsiderando o flag).

# EX. de exibição
# Digite um valor (999 para parar):
# A soma dos 3 valores foi 12!


valor = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        valor += 1
    soma = soma + n
print(f'A soma dos {valor} valores foi {soma}!')



#soma = soma + n
#    n += 1