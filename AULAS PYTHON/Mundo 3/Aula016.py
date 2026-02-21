# TUPLAS

# DICA: MUNDO 1 - MANIPULAÇÂO DE STRING (FATIAMENTO)

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'  # ou 0, 1, 2, 3
print(lanche)
print(lanche[2])
print(lanche[0:2]) # Mostra do item 0 até o item 1, ignorando o item 2 (ultimo elemento)
print(lanche[1:]) # Mostra do item 1 até o final
print(lanche[-1]) #mostra o ultimo elemento, os demais seriam -2, -3 e -4
print(len(lanche)) # Diz quantos elementos existem na variável lanche

# lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
# for c in lanche:  # podemos utilizar o FOR para variáveis compostas e não somente com o RANGE
#     print(c)

# "AS TUPLAS SÃO IMUTÁVEIS" - Nunca esquecer isso!!!

# Variáveis compostas, podem ser de 3 tipos:

# (Tuplas) , [Listas] e {Dicionário}


# EXEMPLO PRÁTICO

#lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#print(lanche[-2])
#print(lanche[:-2])
#print(lanche[2:])
#print(lanche[1:3])

#for comida in lanche:                #utilizamos se não precisar da posição
#    print(f'Eu vou comer {comida}')

#for cont in range (0, len(lanche)):   #utilizamos se precisar da posição
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# ou

#for posicao, comida in enumerate(lanche): #utilizamos se precisar da posição
#    print(f'Eu vou comer {comida} na posição {posicao}')

#print('Comi pra caramba!')

#lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#print(sorted(lanche))  #Mostra em ordem alfabética
#print(lanche)

# ----------------------------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c)) # Quantos elementos tem ao todo entre b + a
print(c.count(5)) # QUANTAS VEZES APARECE O NUMERO 5 entre b + a
print(c.index(8)) # Em que posição está o número 8
print(c.index(5, 1)) # Em que posição está o número 5, porém ignorando a primeira posição (DESLOCAMENTO)

# ------------------------------------------------






