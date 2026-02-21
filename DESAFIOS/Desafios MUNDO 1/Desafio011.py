# DESAFIO 011 - FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS,
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA
# LITRO DE TINTA, PINTA UMA ÁREA DE 2m2.

print()
l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
area = a * l
tinta = area / 2
print()
print(f'Você precisa de aproximadamente {tinta:.1f} litros de tinta para pintar uma área total de {area} m²')











