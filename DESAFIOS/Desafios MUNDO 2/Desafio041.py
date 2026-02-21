# A Confederaçao Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo
# com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print(f'Você tem {idade} anos e está na gategoria MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos e está na gategoria INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos e está na gategoria JÚNIOR')
else:
    print(f'Você tem {idade} anos e está na gategoria MASTER')






