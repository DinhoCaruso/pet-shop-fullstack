# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai  tentar
# acertar, mostrando no final quantos palpites foram necessários
# para vencer.

from random import randint
computador = randint(0, 10)
contador = 1
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
while jogador != computador:
    jogador = int(input('Errou, tente novamente: '))
    contador += 1
else:
    print(f'Eu pensei no número {computador} e você precisou de {contador} tentativas para acertar')









