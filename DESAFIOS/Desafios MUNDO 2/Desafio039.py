# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nascimento = int(input('Qual é o ano do seu nascimento?: '))
idade = (atual - nascimento)
if idade < 18:
    print('Ainda não é o momento para você se alistar.')
    print(f'O ano do seu alistamento será em {nascimento + 18}')
elif idade > 18:
    print('Já passou do tempo para o alistamento.')
    print(f'O seu alistamento, deveria ter sido no ano de {nascimento + 18}')
else:
    print('Já é a hora de se alistar.')
    print(f'Você neste ano de {atual}, completa {atual-nascimento}')















