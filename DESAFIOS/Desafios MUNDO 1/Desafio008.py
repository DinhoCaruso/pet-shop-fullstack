# DESAFIO 008 - ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM
# CENTÍMETROS E MILÍMETROS

print('=================================')
print('           CONVERSOR             ')
print('=================================')
print()
numero = float(input(' Digite a medida em metros: '))

km = numero / 1000
hm = numero / 100
dam =numero / 10
dm = numero * 10
cm = numero * 100
mm = numero * 1000

print(f'A medida de {numero} metros, corresponde a:')
print(f'{km} km ')
print(f'{hm} hm ')
print(f'{dam} dam ')
print(f'{numero} m ')
print(f'{dm} dm ')
print(f'{cm} cm ')
print(f'{mm} mm ')
print('=================================')


