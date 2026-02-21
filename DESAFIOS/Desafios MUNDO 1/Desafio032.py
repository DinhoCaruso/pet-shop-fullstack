# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.


from datetime import date #incremento do exercicio
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
bissexto = ano
if ano == 0:     #incremento
    ano = date.today().year     #incremento
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')













