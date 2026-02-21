# [VARIÁVEL CONTADORA] PARTE 7

# Dados dois números inteiros p (>=0) e q (>0), exibir o quociente da
# divisão inteira de p por q sem usar operadores de divisão e multiplicação.
# ex: quantas vezes subtraimos p de q: (p - q =)

#p = int(input('p: '))
#q = int(input('q: '))
#contador = 0

#while p>=q:
 #   p = p - q #p -= q mesma coisa
  #  contador += 1
#print(f'O quociente da divisão é {contador}')

# Variável Acumuladora

# Dados diversos números inteiros, exibir a média dos números lidos.
# A entrada termina com a leitura do número -1 que não deve ser contabilizado.

#soma = 0
#qtd = 0

#n = int(input('Digite um número: '))
#while n != -1:
#    soma += n
#    qtd += 1
#    n = int(input('Digite outro número'))
#print(f'Média {soma/qtd}')

# [Variável FLAG BOOLEANA]
# Crie um programa que peça ao usuário preços de produtos comprados até
# que ele decida encerrar a compra. O programa, ao final, deve exibir o total gasto.

total = 0
quero_comprar = True
while quero_comprar:
    preco = float(input('Preço: '))
    total += preco
    opcao = input('Continuar comprando (s/n)?')
    if opcao != 's':
        quero_comprar = False
print(f'Total da compra R$ {total:.2f}')

































