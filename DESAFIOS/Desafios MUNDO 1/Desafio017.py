# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO
# ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO
# DA HIPOTENUSA.
# c2 = a2 + b2 - PITÁGORAS


from math import hypot
co = float(input('Cateto oposto = '))
ca = float(input('Cateto adjacente = '))
hipotenusa = hypot(co, ca)

print(f'O valor da hipotenusa é: {hipotenusa:.2f}')








