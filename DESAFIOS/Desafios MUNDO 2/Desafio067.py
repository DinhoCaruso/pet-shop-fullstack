# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.

# Quer ver a tabuada de qual valor?:
# -------------------------------
# 3 x 1 = 3
# -------------------------------
# Quer ver a tabuada de qual valor?
# PROGRAMA TABUADA ENCERRADO. Volte sempre!

print ('=-'*20)
print ('------' 'PROGRAMA TABUADA' '------')
print ('=-'*20)
n = int(input('Quer ver a tabuada de qual valor?: '))
print ('=-'*20)
while n >= 0:
    print(f'''{n} x 1 = {n * 1}
{n} x 2 = {n * 2} 
{n} x 3 = {n * 3}
{n} x 4 = {n * 4}
{n} x 5 = {n * 5}
{n} x 6 = {n * 6}
{n} x 7 = {n * 7}
{n} x 8 = {n * 8}
{n} x 9 = {n * 9}
{n} x 10 = {n * 10}''')
    print('=-' * 20)
    n = int(input('Quer ver a tabuada de qual valor?: '))
    print('=-' * 20)
    if n <= 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
print ('=-'*20)
