# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.


salario = float(input('Digite o seu salário R$: '))
if salario >= 1250:
    print(f'O seu novo salário é R$ {salario*0.10+salario:.2f} com 10% de aumento.')
else:
    print(f'O seu novo salário é R$ {salario*0.15+salario:.2f} com 15% de aumento.')

