# DESAFIO 005 - FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO
# E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR:

print ('Desafio 005')

numero = int(input('Digite um número por favor: '))
numero_antecessor = (numero - 1)
numero_sucessor = (numero + 1)

print(f'O número antecessor é {numero_antecessor} e o número sucessor é {numero_sucessor}.')

#OU PODEMOS SIMPLIFICAR PARA:

numero = int(input('Digite um número por favor: '))
print(f'O número antecessor é {numero-1} e o número sucessor é {numero +1}.')


# DESAFIO 006 - CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE
#O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

numero = float(input('Digite um número por favor: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero **(1/2)

print(f'O dobro do número escolhido é {dobro}, o triplo é {triplo}', end=' ')
print(f'e a sua raíz quadrada é {raiz_quadrada:.2f}')

# OU

numero = float(input('Digite um número por favor: '))
print(f'O dobro do número escolhido é {numero * 2}, o triplo é {numero * 3}', end=' ')
print(f'e a sua raíz quadrada é {numero **(1/2):.2f}')

# OU

numero = float(input('Digite um número por favor: '))
print(f'O dobro do número escolhido é {numero * 2}, o triplo é {numero * 3}', end=' ')
print(f'e a sua raíz quadrada é {pow (numero, (1/2)):.2f}')



