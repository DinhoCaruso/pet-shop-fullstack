# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.


print ('Olá humano, eu o desafio para que tente adivinhar um número que escolhi entre 0 e 5')
print ('Você está disposto a aceitar o desafio?')
desafio = str(input('S ou N: ')).upper()
if desafio == 'S':
    n = int(input('Digite um número entre 0 e 5: '))
    if n == 1:
        print('PARABÉNS Humano, você acertou!')
    else:
        print('HAHAHA, errado! Tente novamente mais tarde seu burro')
else:
    print('Seu covarde, SUMA DAQUI!')


# OU

from random import randint
computador = randint(0,5) #Faz o computador "PENSAR"
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
if jogador == computador:
    print(f'Eu pensei no número {computador}. Parabéns, você acertou!')
else:
    print(f'Eu pensei no número {computador}. Você errou, tente novamente.')




