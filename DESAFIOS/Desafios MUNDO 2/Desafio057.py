# Faça um programa que leia o sexo de uma pessoa, mas só
# aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter
# um valor correto.

#while True:
#    sexo = str(input('Digite o seu sexo: [M] [F]? ')).upper().strip()
#   if sexo == 'F' or sexo == 'M':
#        break
#    else:
#        print('Por favor, digite apenas uma das opções acima\n')
#print('Obrigado')

# ------------------------------------------------------------------

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')









