#x = 0
#while x <= 10:
    #y = 0
    #while y <= 10:
        #print(f'{x} x {y} = {x * y}')
        #y += 1
    #print ()
    #x += 1
vale_presente = float(input('Valor?'))

while vale_presente > 0:
    mercadoria = float(input('Mercadoria?'))
    if mercadoria > vale_presente:
        print ('Muito caro! Escolha outra mercadoria')
        continue
    vale_presente -= mercadoria
print ('Obrigado pela compra!')
