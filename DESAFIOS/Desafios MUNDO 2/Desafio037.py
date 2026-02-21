# Escreva um programa que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'O número {num} convertido em binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'O número {num} convertido em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'O número {num} convertido em hexadecimal é {hex(num)[2:]}')
