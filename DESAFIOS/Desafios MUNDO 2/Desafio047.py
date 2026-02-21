# Crie um programa que mostre na tela todos os números pares que estão no
# intervalo entre 1 e 50.


for c in range(2,51,2):
    print (c, end=' ')
print('Acabou')

#OU


for n in range(2,51,2):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')

# OU outro contexto, para somar todos os pares:
print()
soma = 0
for n in range(2,51,2):
    if n % 2 == 0:
        soma = soma + n
print(f'A soma de todos os valores pares é {soma}')
print()

print(2+4+6+8+10+12+14+16+18+20+22+24+26+28+30+32+34+36+38+40+42+44+46+48+50)






