#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE Km PERCORRIDOS POR UM CARRO
#ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO
#A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0.15 por Km RODADO.

d = float(input('Quantos dias alugados?'))
k = float(input('Quantos Km rodados?'))

dias_alugados = d * 60
km_rodados = k * 0.15
total = dias_alugados + km_rodados

print(f'O total a pagar é de R${total:.2f}')



