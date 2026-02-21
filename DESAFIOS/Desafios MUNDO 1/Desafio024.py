# Crie um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome "Santo".


cidade = str(input('Em que cidade você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')

#00000

cidade = input('Digite o nome da cidade: ').upper().split()
print(cidade)

busca='SANTO'

if busca in cidade:
    print(' Tem a palavra santo no nome')
else:
    print('Não tem a palavra santo no nome')

