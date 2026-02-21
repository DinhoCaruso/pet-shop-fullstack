# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA
# LISTA. CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDOS TODOS OS
# VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE.

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não irei adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
números.sort()
print(f'Os valores digitados foram {números}')