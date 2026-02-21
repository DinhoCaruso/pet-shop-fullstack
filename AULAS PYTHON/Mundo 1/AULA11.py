# Cores no Terminal

# ANSI - Escape sequence
# sempre inicia com '\' + um código
# \033[m

#       style     text        back
# \033[   0;       33;         44 m
#                 text

# Style = 0, 1, 4 e 7
# 0 = Sem estilo
# 1 = Bold (negrito)
# 4 = Underline
# 7 = Cor negativa

# Text:                      Back (fundo):
# 30 - branco                     40
# 31 - vermelho                   41
# 32 - verde                      42
# 33 - amarelo                    43
# 34 - azul                       44
# 35 - roxo                       45
# 36 - azul claro                 46
# 37 - cinza (cor padrão)         47

print('Eu tenho a força')
print('\33[31mEu tenho a força')
print('\33[1;34;40mEu tenho a força')
print('\33[1;34;40mEu tenho a força\033[m')
print('\33[4;31;40mEu tenho a força\033[m')























