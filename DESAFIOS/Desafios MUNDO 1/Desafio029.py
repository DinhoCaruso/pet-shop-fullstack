# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade: '))
m = (vel-80)*7
v = (vel-80)
if vel > 80:
    print(f'Você ultrapassou {v} km do limite de velocidade e foi multado em R${m:.2f}!')
    print()
    print('Obs: R$7,00 = cada Km acima do limite de velocidade.')
else:
    print('Continue sendo esse exemplo de condutor! =)')
print('Tenha um excelente dia!')














