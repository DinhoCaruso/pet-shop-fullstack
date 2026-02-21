# Crie uma TUPLA preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro, na ordem de
# coloção. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.


cont = ('América-MG', 'Avaí', 'Operário', 'Vila Nova', 'Sport',
        'Santos', 'Goiás', 'Coritiba', 'Mirassol', 'Ceará',
        'Botafogo SP', 'Novorizontino', 'Paysandu', 'Chapecoense',
        'CRB', 'Ponte Preta', 'Amazonas FC', 'Brusque', 'Ituano',
        'Guarani')

print(f'Os 5 primeiros colocados da série B são {cont[0:5]}')
print(f'Os 4 últimos colocados da série B são {cont[16:20]}')
print(f'Os times participantes são {sorted(cont)}')
print(f'A Chapecoense está na posição {cont.index('CRB')} da tabela.')
print(len(cont))







