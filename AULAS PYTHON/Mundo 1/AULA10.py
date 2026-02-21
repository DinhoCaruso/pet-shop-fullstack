# CONDIÇÕES SIMPLES E COMPOSTAS

#carro.siga() -> carro seria o objeto e o comando siga
# é o método (todo método leva parênteses)

#         se carro.esquerda()         senão
#       .......                       .......
#       . carro.siga()                .  carro.siga()
#       . carro.direita()             .  carro.esquerda()
#       . carro.siga()                .  carro.siga()
#       . carro.direita()             .  carro.esquerda()
#       . carro.esquerda()            .  carro.siga()
#       . carro.siga()                .
#       . carro.direita()
#       . carro.siga()
#
#                       carro.pare()


#  se carro.esquerda()          No Pytho = if carro.esquerda():
#    bloco_V_                                   bloco TRUE
#  senão                                   else:
#    bloco_F_                                   bloco FALSE

#tempo=int(input('Quantos anos tem o seu carro?: '))
#if tempo <= 3:
#    print("O seu carro é novo")
#else:
#    print("Você precisa trocar de carro!")
#print ('--FIM--')


# OU da forma simplificada (para casos simplificados somente)

#tempo = int(input('Quantos anos tem seu carro? '))
#print ('carro novo' if tempo <=3 else 'carro velho')
#print('-- FIM --')
# ----------------------------------------------
# EXEMPLO DE CONDICIONAL SIMPLES:
nome=str(input('Qual é seu nome: '))
if nome == 'Osvaldo'or'Ana Clara'or'Noah'or'Beatriz':
    print ('Que nome lindo você tem!')
print(f'Bom dia, {nome}!')
# EXEMPLO DE CONDICIONAL COMPOSTA:

nome=str(input('Qual é seu nome: '))
if nome == 'Osvaldo':
    print ('Que nome lindo você tem!')
else:
    print ('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')

#

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print(f'A sua média foi {m}')
if m >= 6.0:
    print('Você foi aprovado, PARABÉNS!')
else:
    print('Você não alcançou a média, ESTUDE MAIS!')

#### OU   pela CONDIÇÃO SIMPLIFICADA

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('Você foi aprovado, PARABÉNS!' if m >= 6.0 else 'Você não alcançou a média, ESTUDE MAIS!')


