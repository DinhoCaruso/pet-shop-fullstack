# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.
#
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

casa = float(input('Valor da casa: '))
salario = float(input('Quanto é o seu salário? '))
anos = int(input('Em quantos anos quer financiar? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos,\na prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')












