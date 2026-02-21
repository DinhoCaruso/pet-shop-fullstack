# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras aotodo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

n = str(input('Digite o seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas é: {n.upper()}')
print(f'Seu nome em minúsculas é: {n.lower()}')
print(f'Seu nome tem ao todo {n.__len__()-n.count(' ')} letras')
print(f'Seu primeiro nome tem {n.find(' ')} letras')





