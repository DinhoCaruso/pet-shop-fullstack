# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:

# Equilátero = todos os lados iguais
# Isósceles = dois lados iguais
# Escaleno = todos os lados diferentes


#a = float(input('Reta 1: '))
#b = float(input('Reta 2: '))
#c = float(input('Reta 3: '))

#if a == b == c:
#    print('As medidas formam um triângulo Equilátero')
#elif a != (b == c) and b != (a == c) and c != (a == b):
#    print('As medidas formam um triângulo Isósceles')
#elif a != b != c:
#    print('As medidas formam um triângulo Escaleno')


a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
if a < b + c and b < a + c and c < a + b:
    print('As medidas formam um triângulo')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não forma um triângulo. ')
