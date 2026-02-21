# Crie um programa que tenha uma TUPLA única com nomes de produtos e seus respectivos preços,
# na sequência.

# No final, mostre uma listagem de preços, organizando os dados em forma TABULAR.

listagem = ('Pão', 5.00, 'Requeijão', 7.90, 'Amaciante', 17.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:.>7.2f}')
print('-'*40)
#print(f'{listagem[0]}..........R$  {listagem[1]:.2f}')