# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NUMEROS E COLOCAR EM UMA LISTA.
# DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES E OS
# VALORES ÍMPARES DIGITADOS, RESPECTIVAMEMTE.

# AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS.

numeros = []
par = []
impar = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
