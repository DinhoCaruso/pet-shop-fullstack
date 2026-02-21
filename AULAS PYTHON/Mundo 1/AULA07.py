#====== OPERADORES ARITMÉTICOS ======

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# % Resto da Divisão (RESTO PARA O MÓDULO)

#====== ORDEM DE PRECEDÊNCIA ======

# 1. ()
# 2. **
# 3. * / // e %
# 4. + -

# Exemplos:
#     5 + 3 * 2
#     5 + 6
#      == 11
# ----------------------------------
#  3 * 5 + 4 ** 2                 3 * (5 + 4) ** 2
#  3 * 5 + 16                     3 * 9 ** 2
#  15 + 16                        3 * 81
#   == 31                          == 243

#nome = input('Qual é seu nome?')
#print (f'Prazer em te conhecer {nome:*^22}!')
print()
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1// n2
e = n1 ** n2
print (f'A soma é {s}, o produto é {m}, a divisão {d:.3f},', end=' ')
print (f'divisão inteira {di} e a potência {e}.')


