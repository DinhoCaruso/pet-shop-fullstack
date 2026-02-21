# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
# até 200Km e R$0,45 para viagens mais longas.

print()
d = float(input('A viagem terá quantos Km? '))
p1 = d*0.50
p2 = d*0.45
if d <= 200:
    print(f'O valor da passagem é R$ {p1:.2f}.')
else:
    print(f'O valor da passagem é R$ {p2:.2f}.')
print('Obrigado pela preferência!')











