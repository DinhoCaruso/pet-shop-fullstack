# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS e GUARDE-OS EM UMA LISTA.
# NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.

valores = []
maior=0
menor=0
for c in range (0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}... ', end='')
print()

