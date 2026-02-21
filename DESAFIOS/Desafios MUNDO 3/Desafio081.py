# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
# DEPOIS DISSO, MOSTRE:

# A) QUANTOS NÚMEROS FORAM DIGITADOS.
# B) A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE.
# C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA.

numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')