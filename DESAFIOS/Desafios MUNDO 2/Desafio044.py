# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:

# À vista dinheiro / cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

import random
compra = float(input('Total da compra: R$'))
print('''Selecione a Opção de Pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

metodo = int(input('Qual é a opção?: '))
if metodo == 1:
    print(f'O total da compra foi R$ {compra:.2f} e com o desconto de 10% ficou R$ {compra-compra*0.10:.2f}')
elif metodo == 2:
    print(f'O total da compra foi R$ {compra:.2f} e com o desconto de 5% ficou R$ {compra - compra * 0.05:.2f}')
elif metodo == 3:
    print(f'O total da compra foi R$ {compra:.2f} dividido em 2x de R$ {compra / 2:.2f}')
elif metodo == 4:
    parcela = int(input('Você pode escolher de 3 até 12 parcelas com juros: '))
    print(f'O total da compra foi R$ {compra:.2f} dividido em {parcela}x de R$ {(compra+compra*0.20) / parcela:.2f}')

print('Obrigado pela preferência e volte sempre!')







