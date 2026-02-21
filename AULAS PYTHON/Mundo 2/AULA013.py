#         ESTRUTURA DE REPETIÇÃO FOR
# 1ra. SITUAÇÃO:
#
# laço c no intervalo(1,10)
#   passo
# pega
#
# no PYTHON:
# for c in range(1,10):
#   passo
# pega
# -------------------------------------------------------------------------------------------
# 2da. SITUAÇÃO - COM OBSTÁCULO
#
# laço c no intervalo (0,3)
#   passo
#   pula
# passo
# pega
#
# no PYTHON:
#
# for c in range (0,3):
#   passo
#   pula
# passo
# pega
# -----------------------------------------------------------------------------------------------
# 3ra SITUAÇÃO - (ESTRUTURA DE CONTROLE CONDICIONAL)
# ANINHANDO:
#
# laço c no intervalo (0,3)
#   se moeda
#       pega
#   passo
#   pula
# passo
# pega
#
# NO PYTHON:
#
# for c in range (0,3):
#   if moeda:
#       pega
#   passo
#   pula
# passo
# pega
#
# EXEMPLO PRÁTICO:

for c in range(2,8,2):
    print(c)
print('FIM')

#ou
print()
n = int(input('Digite um número: '))
for c in range (0, n+1, 2):
    print(c)
print('FIM')

# OU
print()
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')


