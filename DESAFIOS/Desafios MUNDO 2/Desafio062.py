# Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerra quando ele disser
# que quer mostrar '0 TERMOS'.

print('GERADOR DE PA')
print('-='*10)
primeiro = int(input('Digite o valor do termo: '))
razão = int(input('Digite o valor da razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')




