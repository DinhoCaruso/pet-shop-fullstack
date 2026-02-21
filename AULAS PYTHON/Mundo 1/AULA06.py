#TIPOS PRIMITIVOS E SAÍDA DE DADOS
# int = números inteiros ( 7, -4, 0, 9875)
# float = números reais ou de ponto flutuante (4.5, 0.076, -15.223, 7.0)
# bool = valores lógicos ou booleanos (TRUE ou FALSE) sempre escrever com a 1ra letra maiúscula
# str = palavras ('OLÁ')
#______________________________________________________________________________________
#n1 = int(input('Digite um número:'))
#n2 = int(input('Digite outro número:'))
#soma = n1 + n2
#print (f'A soma entre {n1} e {n2} vale {soma}, até a próxima!')

#n = input('Digite algo: ')
#print(n.isalnum())

#====== DESAFIO 003 ======
# CRIE UM PROGRAMA QUE LEIA DOIS NÚMEROS E MOSTRE A SOMA ENTRE ELES.

numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite um outro número: '))
soma = numero_um + numero_dois
print(f'A soma dos números {numero_um} e {numero_dois} é igual a {soma}!')


n = input('Digite algo: ')
print (n.isalpha())
print()
#### DESAFIO 04
# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU
# TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?' , a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúscula? ', a.isupper())
print('Está em minúscula?', a.islower())
print('Está capitalizada? ', a.istitle())






