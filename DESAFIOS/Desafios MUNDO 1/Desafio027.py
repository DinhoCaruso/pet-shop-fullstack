# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida
# o primeiro e o último nome separadamente.

# Ex:
# Ana Maria de Souza
# primeiro = Ana
# último = Souza

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print (f'Seu primeiro nome é {nome[0]}')
print (f'Seu ultimo nome é {nome[len(nome)-1]}')








