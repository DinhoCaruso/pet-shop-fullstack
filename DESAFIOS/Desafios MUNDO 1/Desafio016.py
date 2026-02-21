#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E
# MOSTRE NA TELA A SUA PORÇÃO INTEIRA.

# ex: digite um número: 6.127
#     O número 6.127 tem a parte inteira 6.

import math
numero = float(input('Digite um número: '))
parte_inteira = math.floor (numero)
print (f'O número {numero} tem a parte inteira {parte_inteira}')
