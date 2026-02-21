def troca (lista):
    for i in range(3):
        if lista [i] >= 0:
            lista[i] = 1
        else:
            lista[i] = 0
    return lista

lista = [0] * 3
for i in range(3):
    lista [i] = int(input('Digite um valor: '))
print (lista)
troca(lista)
print (lista)










