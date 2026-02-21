# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O
# programa deve perguntar ao usuário se ele quer ou não con-
# tinuar a digitar valores.


resp = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'A média dos valores digitados foi {media:.2f}, o maior valor foi {maior} e o menor {menor}.')

